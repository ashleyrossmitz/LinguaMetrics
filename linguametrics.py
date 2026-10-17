import os
import time
import sqlite3
import sys
from datetime import datetime, timedelta

ACTIVITIES = {
    1: "listening",
    2: "reading",
    3: "viewing"
}

DATABASE_FILE = "statistics.db"

ERRORS = {
    "OperationalError": "Error: the database is busy, access is denied, or the file is corrupted.",
    "IntegrityError": "Error: invalid data.",
    "DatabaseError": "Error: the database is corrupted.",
    "Error": "Failed to open the database. The program cannot run."
}

# ------- UTILITIES -------

def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")
    
def prompt_int_in_range(prompt: str, min_value: int, max_value: int) -> int:
    '''Checks whether the entered message is a number and whether it falls within the required range of numbers.'''
    
    while True:
        try:
            user_choice = int(input(prompt))
            if min_value <= user_choice <= max_value:
                return user_choice
            else:
                print(f"Input error. Enter a number from {min_value} to {max_value}. Try again.")
        except ValueError:
            print("Error. You entered a non-integer number. Try again.")

def init_db() -> None:
    """Creates a table if it doesn't exist."""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        with conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS statistics (
                    id INTEGER PRIMARY KEY,
                    activity TEXT NOT NULL,
                    duration REAL NOT NULL,
                    date TEXT NOT NULL,
                    language TEXT NOT NULL
                )        
            """)
    except sqlite3.Error:
        print(ERRORS["Error"])
        sys.exit(1)
    finally:
        if conn:
            conn.close()
        
def add_session(session_record: dict) -> str:
    """Adds session data to the SQLite table."""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        with conn:
            conn.execute(
                "INSERT INTO statistics (activity, duration, date, language) VALUES (?, ?, ?, ?)",
                (session_record['activity'], session_record['duration'], session_record['date'], session_record['language'])
            )
        return "ok"
    except sqlite3.IntegrityError:
            return "IntegrityError"
    except sqlite3.OperationalError:
        return "OperationalError"
    except sqlite3.DatabaseError:
        return "DatabaseError"
    finally:
        if conn:
            conn.close()
            
def load_period_totals(period: int) -> dict:
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cur = conn.cursor()
        match period:
            case 1:
                cur.execute("""
                    SELECT activity, SUM(duration)
                    FROM statistics
                    WHERE date = ?
                    GROUP BY activity            
                """, (datetime.now().strftime("%Y-%m-%d"),))
            case 2:
                cur.execute("""
                    SELECT activity, SUM(duration)
                    FROM statistics
                    WHERE date >= ?
                    GROUP BY activity            
                """, ((datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d"),))
            case 3:
                cur.execute("SELECT activity, SUM(duration) FROM statistics GROUP BY activity")
        rows = cur.fetchall()
        return {activity: total for activity, total in rows}
    finally:
        if conn:
            conn.close()
            
def load_lastest_session() -> list:
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cur = conn.cursor()
        cur.execute("SELECT activity, duration, date FROM statistics ORDER BY id DESC LIMIT 3")
        rows = cur.fetchall()
        if rows:
            return [{"activity": row[0], "duration": row[1], "date": row[2]} for row in rows]
        else:
            return []
    finally:
        if conn:
            conn.close()

# ------- CORE -------

def measure_time(start_msg: str, stop_msg: str) -> float:
    '''Counts the duration between two Enter presses.'''
    input(start_msg)
    start_time = time.perf_counter()
    input(stop_msg)
    stop_time = time.perf_counter()
    return stop_time - start_time
    
def build_session_record(activity_code: int) -> dict:
    """Collects data for a single session: activity, duration, date."""
    if activity_code not in ACTIVITIES:
        raise ValueError(f"Unknown activity: {activity_code}")
    
    clear_screen()
    
    duration = measure_time(
        "Press <Enter> to start timer ...",
        "Press <Enter> to stop timer ..."
    )
    date = datetime.now().strftime("%Y-%m-%d")
    
    language = "English"
    
    return {"activity": ACTIVITIES[activity_code], "duration": duration, "date": date, "language": language}
    
def record_session() -> None:
    activity = choose_activity()
    session_record = build_session_record(activity)
    status = add_session(session_record)
    
    if status == "ok":
        print(f"\nSession saved: {session_record['activity']} — {round(session_record['duration'], 2)}")
    else:
        if status == "OperationalError":
            print(ERRORS["OperationalError"])
        elif status == "IntegrityError":
            print(ERRORS["IntegrityError"])
        elif status == "DatabaseError":
            print(ERRORS["DatabaseError"])
        print(f"\nData of the last session: {session_record['activity']} — {round(session_record['duration'], 2)}, date: {session_record['date']}")
        
    input("\nPress <Enter> to return to the main menu ...")
    
def show_statistics() -> None:
    period = choose_period()
    
    clear_screen()
    print_statistics_screen()
    
    activity_totals = load_period_totals(period)
    if activity_totals:
        match period:
            case 1: print("Statistics for today:\n")
            case 2: print("Statistics for the week:\n")
            case 3: print("Statistics for all time:\n")
        
        for activity, total in activity_totals.items():
            print(f"{activity.capitalize()} - {round(total, 2)} seconds")
        
        print("\nLast sessions:\n")
        print(f"{'Activity':^15} | {'Duration':^10} | {'Date':^15}")
        print("-" * 15, "-" * 10, "-" * 15, sep=" | ")
        for session in load_lastest_session():
            print(f"{session['activity']:>15} | {round(session['duration'], 2):<10} | {session['date']:<15}")
    else:
        print("No statistics available for the selected period.")
        
    input("\nPress <Enter> to return to the main menu ...")
    
# ------- UI -------

def print_main_menu() -> None:
    print("-" * 15, "LinguaMetrics", "-" * 15)
    print("\n1. Start session"
          "\n2. Statistics"
          "\n3. Exit\n")

def print_statistics_screen() -> None:
    clear_screen()
    print("-" * 15, "STATISTICS", "-" * 15)
    print()

def choose_activity() -> int:
    clear_screen()
    print("-" * 15, "ACTIVITIES", "-" * 15)
    
    for code, name in ACTIVITIES.items():
        print(f"{code}. {name.capitalize()}")
    
    return prompt_int_in_range("\nSelect an activity: ", 1, len(ACTIVITIES))

def choose_period() -> int:
    clear_screen()
    print("-" * 10, "STATISTICS FOR THE PERIOD", "-" * 10)
    print("\n1. Today"
          "\n2. For the week"
          "\n3. For all time")
    
    return prompt_int_in_range("\nSelect a period: ", 1, 3)

# ------- LAUNCH -------

def main() -> None:
    init_db()
    while True:
        clear_screen()
        print_main_menu()
        
        choice = prompt_int_in_range("Select an action (1-3): ", 1, 3)
        
        if choice == 1:
            record_session()
        elif choice == 2:
            show_statistics()
        elif choice == 3:
            break

if __name__ == "__main__":
    main()
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

DB = "statistics.db"

ERRORS = {
    "OperationalError": "Error: the database is busy, access is denied, or the file is corrupted.",
    "IntegrityError": "Error: invalid data.",
    "DatabaseError": "Error: the database is corrupted.",
    "Error": "Failed to open the database. The program cannot run."
}

# ------- UTILITIES -------

def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")
    
def input_in_range(req: str, a: int, b: int) -> int:
    '''Checks whether the entered message is a number and whether it falls within the required range of numbers.'''
    
    while True:
        try:
            user_choice = int(input(req))
            if a <= user_choice <= b:
                return user_choice
            else:
                print(f"Input error. Enter a number from {a} to {b}. Try again.")
        except ValueError:
            print("Error. You entered a non-integer number. Try again.")

def init_db() -> None:
    """Creates a table if it doesn't exist."""
    conn = None
    try:
        conn = sqlite3.connect(DB)
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
        
def add_session(session_data: dict) -> str:
    """Adds session data to the SQLite table."""
    conn = None
    try:
        conn = sqlite3.connect(DB)
        with conn:
            conn.execute(
                "INSERT INTO statistics (activity, duration, date, language) VALUES (?, ?, ?, ?)",
                (session_data['activity'], session_data['duration'], session_data['date'], session_data['language'])
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
            
def load_statistics(period: int) -> dict:
    conn = None
    try:
        conn = sqlite3.connect(DB)
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

# ------- CORE -------

def measure_time(start_msg: str, stop_msg: str) -> float:
    '''Counts the duration between two Enter presses.'''
    input(start_msg)
    start = time.perf_counter()
    input(stop_msg)
    stop = time.perf_counter()
    return stop - start
    
def build_session_data(activity_code: int) -> dict:
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
    
def run_session() -> None:
    activity = show_activity_menu()
    data = build_session_data(activity)
    result_of_addition = add_session(data)
    
    if result_of_addition == "ok":
        print(f"\nSession saved: {data['activity']} — {round(data['duration'], 2)}")
    else:
        if result_of_addition == "OperationalError":
            print(ERRORS["OperationalError"])
        elif result_of_addition == "IntegrityError":
            print(ERRORS["IntegrityError"])
        elif result_of_addition == "DatabaseError":
            print(ERRORS["DatabaseError"])
        print(f"\nData of the last session: {data['activity']} — {round(data['duration'], 2)}, date: {data['date']}")
        
    input("\nPress <Enter> to return to the main menu ...")
    
def show_statistics() -> str:
    period = select_period_menu()
    match period:
        case 1:
            period_data = load_statistics(1)
        case 2:
            period_data = load_statistics(2)
        case 3:
            period_data = load_statistics(3)
    print(period_data)
    input()
    
# ------- UI -------

def main_menu() -> None:
    print("-" * 15, "LinguaMetrics", "-" * 15)
    print("\n1. Start session"
          "\n2. Statistics"
          "\n3. Exit\n")

def statistics_menu() -> None:
    clear_screen()
    print("-" * 15, "STATISTICS", "-" * 15)
    input("\nPress <Enter> to return to the main menu ...")

def show_activity_menu() -> int:
    clear_screen()
    print("-" * 15, "ACTIVITIES", "-" * 15)
    
    for code, name in ACTIVITIES.items():
        print(f"{code}. {name.capitalize()}")
    
    return input_in_range("\nSelect an activity: ", 1, len(ACTIVITIES))

def select_period_menu() -> int:
    clear_screen()
    print("-" * 10, "STATISTICS FOR THE PERIOD", "-" * 10)
    print("\n1. Today"
          "\n2. For the week"
          "\n3. For all time")
    
    return input_in_range("\nSelect a period: ", 1, 3)

# ------- LAUNCH -------

def main() -> None:
    init_db()
    while True:
        clear_screen()
        main_menu()
        
        choice = input_in_range("Select an action (1-3): ", 1, 3)
        
        if choice == 1:
            run_session()
        elif choice == 2:
            show_statistics()
        elif choice == 3:
            break

if __name__ == "__main__":
    main()
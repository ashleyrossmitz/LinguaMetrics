import os
import time
import sqlite3
from datetime import datetime

ACTIVITIES = {
    1: "listening",
    2: "reading",
    3: "viewing"
}

DB = "statistics.db"

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
    with sqlite3.connect(DB) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS statistics (
                id INTEGER PRIMARY KEY,
                activity TEXT NOT NULL,
                duration REAL,
                date TEXT NOT NULL
            )        
        """)
        
def add_session(session_data: dict) -> None:
    """Adds session data to the SQLite table."""
    with sqlite3.connect(DB) as conn:
        conn.execute(
            "INSERT INTO statistics (activity, time, date) VALUES (?, ?, ?)",
            (session_data['activity'], session_data['duration'], session_data['date'])
        )

# ------- CORE -------

def timer() -> dict:
    '''Measure the time between two Enter key presses and return the session dictionary.'''
    
    clear_screen()
    
    input("Press <Enter> to start timer ...")
    start = time.perf_counter()
    
    input("Press <Enter> to stop timer ...")
    stop = time.perf_counter()
    
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    clear_screen()
    
    return {
        "date": date, 
        "duration": stop - start
        }
    
def build_session_data(activity_code: int) -> dict:
    if activity_code not in ACTIVITIES:
        raise ValueError(f"Unknown activity: {activity_code}")
    data = timer()
    return data | {"activity": ACTIVITIES[activity_code]}
    
def run_session() -> None:
    activity = show_activity_menu()
    data = build_session_data(activity)
    
    add_session(data)
    
    input("\nPress <Enter> to return to the main menu ...")
    
# ------- UI -------

def main_menu() -> None:
    print("-" * 15, "LinguaMetrics", "-" * 15)
    print("\n1. Start session"
          "\n2. Statistics"
          "\n3. Exit\n")

def stats_menu() -> None:
    print("-" * 15, "STATISTICS", "-" * 15)
    input("\nPress <Enter> to return to the main menu ...")

def show_activity_menu() -> int:
    clear_screen()
    print("-" * 15, "ACTIVITIES", "-" * 15)
    print("\n1. Listening"
          "\n2. Reading"
          "\n3. Viewing")
    return input_in_range("\nSelect an activity (1-3): ", 1, 3)

# ------- LAUNCH -------

def main() -> None:
    while True:
        init_db()
        clear_screen()
        main_menu()
        
        choice = input_in_range("Select an action (1-3): ", 1, 3)
        
        if choice == 1:
            run_session()
        elif choice == 2:
            stats_menu()
        elif choice == 3:
            break

if __name__ == "__main__":
    main()
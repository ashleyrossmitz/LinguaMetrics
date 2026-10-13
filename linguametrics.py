# import json
import os
import time
from datetime import datetime

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    
def user_input(req, a, b):
    while True:
        try:
            user_choice = int(input(req))
            if a <= user_choice <= b:
                return user_choice
            else:
                print(f"Input error. Enter a number from {a} to {b}. Try again.")
        except ValueError:
            print("Error. You entered a non-integer number. Try again.")

def save_stats():
    pass

def load_stats():
    pass

# ------- CORE -------

def timer() -> dict:
    clear_screen()
    
    input("Press <Enter> to start timer ...")
    start = time.perf_counter()
    
    input("Press <Enter> to stop timer ...")
    stop = time.perf_counter()
    
    date = datetime.now().strftime("%d.%m.%Y %H:%M")
    
    clear_screen()
    
    return {
        "date": date, 
        "time": stop - start
        }
    
def session(activity) -> dict:
    data = timer()
    match activity:
        case 1:
            return data | {"activity": "listening"}
        case 2:
            return data | {"activity": "reading"}
        case 3:
            return data | {"activity": "viewing"}
        case _:
            raise ValueError(f"Unknown activity: {activity}")
    
def run_session():
    activity = show_activity_menu()
    data = session(activity)
    save_stats(data)
    print(f"Session saved: {data}")
    input("\nPress <Enter> to return to the main menu ...")
    
# ------- UI -------

def main_menu():
    print("-" * 15, " LinguaMetrics ", "-" * 15)
    print("\n1. Start session"
          "\n2. Statistics"
          "\n3. Exit\n")

def stats_menu():
    pass

def show_activity_menu() -> int:
    clear_screen()
    print("-" * 15, "ACTIVITIES", "-" * 15)
    print("\n1. Listening"
          "\n2. Reading"
          "\n3. Viewing")
    return user_input("\nSelect an activity (1-3): ", 1, 3)

# ------- LAUNCH -------

def main():
    while True:
        clear_screen()
        main_menu()
        
        choice = user_input("Select an action (1-3): ", 1, 3)
        
        if choice == 1:
            run_session()
        elif choice == 2:
            stats_menu()
        elif choice == 3:
            break

if __name__ == "__main__":
    main()
# import json
import os
import msvcrt
import time
from datetime import datetime

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def save_stats():
    pass

def load_stats():
    pass

# ------- CORE -------

def timer():
    clear_screen()
    print("Press any key to start timer ...")
    msvcrt.getch()
    
    start = time.perf_counter()
    
    print("Press any key to stop timer ...")
    msvcrt.getch()
        
    stop = time.perf_counter()
    
    date = datetime.now().strftime("%d.%m.%Y %H:%M")
    
    clear_screen()
    
    return {
        "date": date, 
        "time": stop - start
        }
    
def session(activity):
    data = timer()
    match activity:
        case 1:
            return data | {"activity": "listening"}
        case 2:
            return data | {"activity": "reading"}
        case 3:
            return data | {"activity": "viewing"}
        case _:
            return {}
    
# ------- UI -------

def main_menu():
    print("-" * 15, " LinguaMetrics ", "-" * 15)
    print("\n1. Start session"
          "\n2. Statistics"
          "\n3. Exit\n")

def stats_menu():
    pass

def activity_menu():
    clear_screen()
    print("-" * 15, "ACTIVITIES", "-" * 15)
    print("\n1. Listening"
          "\n2. Reading"
          "\n3. Viewing")
    data = session(int(input("\nSelect an activity (1-3): ")))
    print(data)
    input()

# ------- LAUNCH -------

def main():
    while True:
        clear_screen()
        main_menu()
        
        choice = int(input("Select an action (1-3): "))
        
        if choice == 1:
            activity_menu()
        elif choice == 2:
            stats_menu()
        elif choice == 3:
            break

if __name__ == "__main__":
    main()
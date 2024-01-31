import pandas as pd
from tabulate import tabulate
from datetime import datetime
from habit_tracker import track_habit, Habit

def main():
    habits: list[Habit] = [
        track_habit('Laziness', datetime(2024, 1, 30, 22), cost=2, minutes_used=5) 
    ]

    df = pd.DataFrame(habits)

    print(tabulate(df, headers='keys', tablefmt='psql'))

if __name__ == "__main__":
    main()


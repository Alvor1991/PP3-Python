import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
from collections import defaultdict  
import prettytable

# Google Sheets setup
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('fitness_tracker')

def view_workout_logs():
    """
    View workout logs from the terminal.
    """
    print("Viewing workout logs...\n")
    worksheet = SHEET.worksheet("workout")
    data = worksheet.get_all_values()
    for row in data[1:]:
        print(", ".join(row))  # Print each row of workout data
    print("\n")

def view_progress():
    """
    View progress from the terminal.
    """
    print("Viewing progress...\n")
    worksheet = SHEET.worksheet("progress")
    data = worksheet.get_all_values()
    for row in data[1:]:
        print(", ".join(row))  # Print each row of progress data
    print("\n")

def get_workout_data():
    """
    Get workout data input from the user.
    Run a loop to collect valid data from the user via the terminal.
    """
    while True:
        print("\nEnter workout details:")
        print("Format: [Day] [Month], Distance (km), Duration (h:mm)")
        print("Example: 3 March, 20, 1:30")

        data_str = input("Enter workout details here: ")
        workout_data = data_str.split(",")

        if validate_workout_data(workout_data):
            print("Workout data is valid!")
            break

    return workout_data

def validate_workout_data(data):
    """
    Validate workout data input.
    """
    if len(data) != 3:
        print("Invalid data: Exactly 3 values required.")
        return False
    
    # Validate workout date format (Day Month)
    try:
        workout_date = datetime.strptime(data[0].strip(), "%d %B")
    except ValueError:
        print("Invalid workout date format. Please use Day Month format (e.g., 3 March).")
        return False
    
    # Validate distance (should be a positive number)
    try:
        distance = float(data[1])
        if distance <= 0:
            raise ValueError("Distance must be a positive number.")
    except ValueError:
        print("Invalid distance. Please enter a valid number.")
        return False
    
    # Validate duration format (h:mm)
    duration_parts = data[2].split(":")
    if len(duration_parts) != 2:
        print("Invalid duration format. Please use h:mm format.")
        return False
    try:
        hours = int(duration_parts[0])
        minutes = int(duration_parts[1])
        if hours < 0 or minutes < 0 or minutes >= 60:
            raise ValueError("Invalid duration values.")
    except ValueError:
        print("Invalid duration values. Please use positive integers for hours and minutes.")
        return False

    return True

def update_workout(data):
    """
    Update the workout log with the provided data.
    """
    print("\nUpdating workout log...")
    worksheet = SHEET.worksheet("workout")
    worksheet.append_row(data)
    print("Workout log updated successfully.")

def calculate_progress():
    """
    Calculate progress based on the workout data collected over time.
    """
    worksheet = SHEET.worksheet("workout")
    data = worksheet.get_all_values()[1:]  # Skipping header row
    grouped_data = defaultdict(lambda: {"distance": 0, "duration": [], "count": 0})

    # Group data by month and calculate total distance and duration for each month
    for row in data:
        date_str = row[0].strip()
        # Adjust date string to include the day if only month is provided
        if len(date_str.split()) == 1:
            date_str = f"1 {date_str}"  # Assuming first day of the month
        workout_date = datetime.strptime(date_str, "%d %B")
        month = workout_date.strftime("%B")
        distance = float(row[1])
        duration = row[2]
        grouped_data[month]["distance"] += distance
        grouped_data[month]["duration"].append(duration)
        grouped_data[month]["count"] += 1

    # Calculate average pace for each month
    for month, info in grouped_data.items():
        durations = info["duration"]
        total_duration_minutes = sum(int(d.split(":")[0]) * 60 + int(d.split(":")[1]) for d in durations)
        total_distance = info["distance"]
        if total_duration_minutes == 0 or total_distance == 0:
            grouped_data[month]["average_pace"] = "N/A"
        else:
            average_pace_minutes_per_km = total_duration_minutes / total_distance
            average_pace_minutes = int(average_pace_minutes_per_km)
            average_pace_seconds = int((average_pace_minutes_per_km - average_pace_minutes) * 60)
            grouped_data[month]["average_pace"] = f"{average_pace_minutes:02}:{average_pace_seconds:02}"

    return grouped_data

def update_progress():
    """
    Update the progress sheet with the calculated progress for each month.
    """
    print("\nUpdating progress sheet...")
    worksheet = SHEET.worksheet("progress")

    # Calculate progress
    progress_data = calculate_progress()

    # Update progress sheet for each month
    for month, info in progress_data.items():
        month_cells = worksheet.findall(month)
        if month_cells:
            row_index = month_cells[0].row
            worksheet.update_cell(row_index, 2, info["distance"])  # Update total distance
            worksheet.update_cell(row_index, 3, info["average_pace"])  # Update average pace
        else:
            print(f"Error: Month {month} not found in progress sheet.")

    print("Progress sheet updated successfully.")

def display_workout_logs(data):
    """
    Display workout logs along with a brief description.
    """
    print("\nWorkout Logs:")
    print("Date: The date of the workout.")
    print("Distance (km): The distance covered during the workout, in kilometers.")
    print("Duration (hh:mm): The duration of the workout, in hours and minutes.")

    if len(data) > 1:
        print("\n")  # Add a newline above the table
        table = prettytable.PrettyTable(["Date", "Distance (km)", "Duration (hh:mm)"])
        for row in data[1:]:
            table.add_row(row)
        print(table)
        print()  # Add a single newline below the table
    else:
        print("No workout logs available.")

    print("\nWhat would you like to do next?")
    print("1. Back to main menu")
    print("2. Exit")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        return 'main_menu'
    elif choice == '2':
        return 'exit'
    else:
        print("Invalid choice. Returning to main menu.")
        return 'main_menu'


def display_progress(data):
    """
    Display progress along with a brief description.
    """
    print("\nProgress:")
    print("Month: The month for which progress is calculated.")
    print("Total Distance (km): The total distance covered in the month, in kilometers.")
    print("Average Pace (mm:ss): The average pace for the month, in minutes and seconds per kilometer.")

    if data:
        print("\n")  # Add a newline above the table
        table = prettytable.PrettyTable(["Month", "Total Distance (km)", "Average Pace (mm:ss)"])
        for month, info in data.items():
            table.add_row([month, info["distance"], info["average_pace"]])
        print(table)
        print()  # Add a single newline below the table
    else:
        print("No progress data available.")

    print("\nWhat would you like to do next?")
    print("1. Back to main menu")
    print("2. Exit")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        return 'main_menu'
    elif choice == '2':
        return 'exit'
    else:
        print("Invalid choice. Returning to main menu.")
        return 'main_menu'

def print_menu():
    """
    Print the main menu options.
    """
    print("Main Menu:")
    print("1. Enter workout data")
    print("2. View workout logs")
    print("3. View progress")
    print("4. Exit")

def main():
    """
    Main function to run the marathon tracker app.
    """
    print("Welcome to the Marathon Tracker App. The Fitness Tracker is a specialized application designed to assist me in training for a Marathon.\n")

    while True:
        print_menu()
        choice = input("\nEnter your choice (1, 2, 3, or 4): ")

        if choice == '1':
            workout_data = get_workout_data()
            update_workout(workout_data)
            update_progress()

            while True:
                print("\nWhat would you like to do next?")
                print("1. Enter another workout")
                print("2. Back to main menu")
                next_choice = input("Enter your choice (1 or 2): ")
                if next_choice == '1':
                    workout_data = get_workout_data()
                    update_workout(workout_data)
                    update_progress()
                elif next_choice == '2':
                    break
                else:
                    print("Invalid choice. Please choose 1 or 2.")

        elif choice == '2':
            data = SHEET.worksheet("workout").get_all_values()
            display_workout_logs(data)
        elif choice == '3':
            progress_data = calculate_progress()
            display_progress(progress_data)
        elif choice == '4':
            print("Exiting the Marathon Tracker App. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")

        print()  # Add a newline before the main menu

if __name__ == '__main__':
    main()

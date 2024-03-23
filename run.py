import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
from collections import defaultdict 

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


def get_workout_data():
    """
    Get workout data input from the user.
    Run a loop to collect valid data from the user via the terminal.
    """
    while True:
        print("Please enter workout details:")
        print("Format: Month, Distance (km), Duration (hh:mm)")
        print("Example: March, 20, 01:30\n")

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
    
    # Validate distance (should be a positive number)
    try:
        distance = float(data[1])
        if distance <= 0:
            raise ValueError("Distance must be a positive number.")
    except ValueError:
        print("Invalid distance. Please enter a valid number.")
        return False
    
    # Validate duration format (hh:mm)
    duration_parts = data[2].split(":")
    if len(duration_parts) != 2:
        print("Invalid duration format. Please use hh:mm format.")
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
    print("Updating workout log...\n")
    worksheet = SHEET.worksheet("workout")
    worksheet.append_row(data)
    print("Workout log updated successfully.\n")

def calculate_progress():
    """
    Calculate progress based on the workout data collected over time.
    """
    worksheet = SHEET.worksheet("workout")
    data = worksheet.get_all_values()[1:]  # Skipping header row
    grouped_data = defaultdict(float)

    # Group data by month and calculate total distance for each month
    for row in data:
        month = row[0].strip().capitalize()
        distance = float(row[1])
        grouped_data[month] += distance

    return grouped_data

def update_progress():
    """
    Update the progress sheet with the calculated progress for each month.
    """
    print("Updating progress sheet...\n")
    worksheet = SHEET.worksheet("progress")

    # Calculate progress
    progress_data = calculate_progress()

    # Update progress sheet for each month
    for month, total_distance in progress_data.items():
        month_cells = worksheet.findall(month)
        if month_cells:
            row_index = month_cells[0].row
            worksheet.update_cell(row_index, 2, total_distance)  # Update total distance
        else:
            print(f"Error: Month {month} not found in progress sheet.")

    print("Progress sheet updated successfully.\n")

def main():
    """
    Main function to run the marathon tracker app.
    """
    print("Welcome to the Marathon Tracker App\n")
    workout_data = get_workout_data()
    update_workout(workout_data)

    # Update progress sheet
    update_progress()

if __name__ == '__main__':
    main()


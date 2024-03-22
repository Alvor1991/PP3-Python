import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

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
        print("Format: Date, Distance (km), Duration (hh:mm), Pace (min/km)")
        print("Example: 15/03/24, 20, 01:30, 05:30\n")

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
    if len(data) != 4:
        print("Invalid data: Exactly 4 values required.")
        return False

    # Validate date format
    try:
        datetime.strptime(data[0], '%d/%m/%y')
    except ValueError:
        print("Invalid date format. Please use DD/MM/YY format.")
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
    
    # Validate pace format (mm:ss)
    pace_parts = data[3].split(":")
    if len(pace_parts) != 2:
        print("Invalid pace format. Please use mm:ss format.")
        return False
    try:
        minutes = int(pace_parts[0])
        seconds = int(pace_parts[1])
        if minutes < 0 or seconds < 0 or seconds >= 60:
            raise ValueError("Invalid pace values.")
    except ValueError:
        print("Invalid pace values. Please use positive integers for minutes and seconds.")
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
    data = worksheet.get_all_values()

    # Calculate total distance covered
    total_distance = sum(float(row[1]) for row in data[1:])  # Skipping header row

    # Calculate average duration
    durations = [row[2] for row in data[1:]]  # Skipping header row
    total_duration = sum(map(lambda x: int(x.split(':')[0]) * 60 + int(x.split(':')[1]), durations))
    average_duration_minutes = total_duration / len(durations)
    average_duration_hours = average_duration_minutes // 60
    average_duration_minutes %= 60
    average_duration = f"{int(average_duration_hours):02}:{int(average_duration_minutes):02}"

    return total_distance, average_duration


# Function to calculate average duration
def calculate_average_duration():
    """
    Calculate average duration of workouts.
    """
    worksheet = SHEET.worksheet("workout")
    data = worksheet.get_all_values()

    total_duration_minutes = sum(int(row[2].split(':')[0]) * 60 + int(row[2].split(':')[1]) for row in data[1:])
    total_workouts = len(data) - 1  # Exclude header row
    average_duration_minutes = total_duration_minutes / total_workouts
    average_duration_hours = int(average_duration_minutes / 60)
    average_duration_minutes %= 60

    return f"{average_duration_hours:02}:{average_duration_minutes:02}"

# Update the update_progress function
def update_progress(month, total_distance, average_duration):
    """
    Update the progress sheet with the calculated progress.
    """
    print("Updating progress sheet...\n")
    worksheet = SHEET.worksheet("progress")
    worksheet.append_row([month, total_distance, average_duration])
    print("Progress sheet updated successfully.\n")

def main():
    """
    Main function to run the marathon tracker app.
    """
    print("Welcome to the Marathon Tracker App\n")
    workout_data = get_workout_data()
    update_workout(workout_data)

    # Extract month from workout data
    workout_date = datetime.strptime(workout_data[0], '%d/%m/%y')
    month = workout_date.strftime('%B') 

    # Calculate progress
    total_distance, average_duration = calculate_progress()

    # Update progress sheet
    update_progress(month, total_distance, average_duration)

if __name__ == '__main__':
    main()
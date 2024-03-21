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

def update_workout_log(data):
    """
    Update the workout log with the provided data.
    """
    print("Updating workout log...\n")
    worksheet = SHEET.worksheet("workout_log")
    worksheet.append_row(data)
    print("Workout log updated successfully.\n")

# Training Data Function
def get_training_data():
    """
    Get training data input from the user.
    Run a loop to collect valid data from the user via the terminal.
    """
    while True:
        print("Please enter training details:")
        print("Format: Date, Distance (km), Duration (hh:mm)")
        print("Example: 15/03/24, 10, 01:00\n")

        data_str = input("Enter training details here: ")
        training_data = data_str.split(",")

        if validate_training_data(training_data):
            print("Training data is valid!")
            break

    return training_data

def validate_training_data(data):
    """
    Validate training data input.
    """
    if len(data) != 3:
        print("Invalid data: Exactly 3 values required.")
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

    return True

def update_training(data):
    """
    Update the training schedule with the provided data.
    """
    print("Updating training schedule...\n")
    worksheet = SHEET.worksheet("training")
    worksheet.append_row(data)
    print("Training schedule updated successfully.\n")


def get_progress_data():
    """
    Get progress data input from the user.
    Run a loop to collect valid data from the user via the terminal.
    """
    while True:
        print("Please enter progress details:")
        print("Format: Month, Total Miles, Average Pace (mm:ss)")
        print("Example: January, 50, 08:00\n")

        data_str = input("Enter progress details here: ")
        progress_data = data_str.split(",")

        if validate_progress_data(progress_data):
            print("Progress data is valid!")
            break

    return progress_data


def validate_progress_data(data):
    """
    Validate progress data input.
    """
    if len(data) != 3:
        print("Invalid data: Exactly 3 values required.")
        return False

    # Validate month
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    if data[0].strip().title() not in months:
        print("Invalid month. Please enter a valid month name.")
        return False
    
    # Validate total miles
    try:
        total_miles = float(data[1])
        if total_miles < 0:
            raise ValueError("Total miles must be a non-negative number.")
    except ValueError:
        print("Invalid total miles. Please enter a valid number.")
        return False
    
    # Validate average pace format (mm:ss)
    pace_parts = data[2].strip().split(":")
    if len(pace_parts) != 2:
        print("Invalid average pace format. Please use mm:ss format.")
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

def update_progress(data):
    """
    Update the progress sheet with the provided data.
    """
    print("Updating progress sheet...\n")
    worksheet = SHEET.worksheet("progress")
    worksheet.append_row(data)
    print("Progress sheet updated successfully.\n")





def main():
    """
    Main function to run the marathon tracker app.
    """
    print("Welcome to the Marathon Tracker App\n")
    workout_data = get_workout_data()
    update_workout_log(workout_data)


if __name__ == '__main__':
    main()

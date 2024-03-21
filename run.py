import gspread
from google.oauth2.service_account import Credentials

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
        print("Example: 2024-03-15, 20, 45:00, 9:00\n")

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

    # Leaving room for additional validation logic here

    return True

def update_workout_log(data):
    """
    Update the workout log with the provided data.
    """
    print("Updating workout log...\n")
    worksheet = SHEET.worksheet("workout_log")
    worksheet.append_row(data)
    print("Workout log updated successfully.\n")

def main():
    """
    Main function to run the marathon tracker app.
    """
    print("Welcome to the Marathon Tracker App\n")
    workout_data = get_workout_data()
    update_workout_log(workout_data)


if __name__ == '__main__':
    main()

# Fitness Tracker

![Fitness Tracker mockup image](assets/readme-files/mockup-image.png)

The Fitness Tracker is a personalized application designed to streamline my marathon training journey. Developed with simplicity and functionality in mind, this tracker serves as my dedicated tool for logging workouts, tracking progress, and staying motivated as I prepare for my upcoming marathon.

The Fitness Tracker utilizes Google Sheets as a central repository for storing workout logs and tracking progress data. The gspread library is integrated into the application to enable seamless interaction with Google Sheets, allowing for real-time updates and easy access to training data.

Visit the deployed application [here](https://macro-calculator.onrender.com).

## Table of Contents
1. [User Experience (UX)](#user-experience-UX)
    1. [Project Goals](#project-goals)
    2. [User Stories](#user-stories)
    3. [Color Scheme](#color-scheme)
    4. [Data Model](#data-model)
    5. [Flowchart](#flowchart)
2. [Features](#features)
    1. [Main Menu](main-menu)
    2. [Enter Workout Data](#enter-workout-data)
    3. [View Workout Logs](#view-workout)
    4. [View Progress](#view-progress)
    5. [Exit Program](#exit-program)
3. [Technologies Used](#technologies-used)
    1. [Language Used](#language-used)
    2. [Frameworks, Libraries and Programs Used](#frameworks-libraries-and-programs-used)
4. [Testing](#testing)
    1. [Testing User Stories](#testing-user-stories)
    2. [Code Validation](#code-validation)
    3. [Manual Testing](#manual-testing)
5. [Deployment](#deployment)
6. [Credits](#credits)
7. [Acknowledgements](#acknowledgements)

***

## User Experience (UX)

### Project Goals

The Marathon Tracker project aims to provide a user-friendly and efficient tool for managing and tracking marathon training progress. The following goals have been established to ensure the application meets its intended purpose:

* Clarity and accessibility - present the tracker in a clear and understandable manner.

* Intuitive workflow - design each step of the tracker to be intuitive and straightforward.

* Input validation - implement robust input validation mechanisms to ensure accurate and error-free data entry.

* Continuous operation - log workouts and view progress at any time until I choose to exit the application.

### User Stories

* As a user, I want to log my workouts.

* As a user, I want to view my workout log.

* As a user, I want to view my progress each month.

* As a user, I want the workouts and progress to be presented clearly.

* As a user, I want to understand the main objective of the program clearly to know its purpose.

* As a user, I want each step to be easy to comprehend, ensuring I provide the correct input without confusion.

* As a user, I expect clear feedback if I input incorrect data, helping me rectify mistakes efficiently.

### Color Scheme

### Data Model

User input data, such as workout details and preferences, are collected through the terminal interface and stored as variables for processing.

Input validation mechanisms ensure the accuracy and integrity of the data provided by the user.

Calculations, such as progress tracking and average pace computation, are performed using stored variables and presented in a clear and understandable format for the user.

The program's logic utilizes conditionals and loops to facilitate user interactions and data processing seamlessly.

### Flowchart

![Fitness Tracker Flowchart](assets/readme-files/flowchart.jpg)

[Back to top ⇧](#fitness-tracker)

## Features

### Main Menu

* Users are presented with a main menu displaying different options.

* Users can input their choice (1, 2, 3, or 4) to navigate through the program.

![Main Menu](assets/readme-files/main-menu.png)

### Enter Workout Data

Users can enter workout details including the date, distance (in kilometers), and duration (in hours and minutes).

![User Input](assets/readme-files/enter-workout.png)

### View Workout Logs

#### Structured Display

* Users can view their workout logs directly from the terminal.

* Workout logs are displayed in a structured format including the date, distance, and duration of each workout.

![Display Logs](assets/readme-files/workout-table.png)

#### Navigation Options

Users can choose to go back to the main menu or exit the program after viewing workout logs.

![Navigation Options](assets/readme-files/sub-menu.png)

### View Progress

#### Structured Display

* Users can view their progress directly from the terminal.

* Progress is displayed in a structured format including the month, total distance and average pace. 

* Progress data is automatically calculated based on the workout data collected.

* This allows users to monitor their progress over time, including total distance covered per month and average pace per month.

![Display Progress](assets/readme-files/progress-table.png)

#### Navigation Options

Users can choose to go back to the main menu or exit the program after viewing progress.

![Navigation Options](assets/readme-files/sub-menu.png)

### Exit Program

A confirmation message is displayed before exiting the program, ensuring users intend to exit.

![Confirmation Prompt](assets/readme-files/exit-app.png)

Date | Distance (km) | Duration (h:mm)
---|---|---
5 January | 5 | 0:40
10 January | 10 | 1:30
15 February | 5 | 0:35
20 February | 10 | 1:20
25 March | 5 | 0:30
31 March | 10 | 1:10

Month | Total Distance (km) | Average Pace (mm:ss)
---|---|---
January  | 15 | 0:25
January  | 15 | 0:25
February  | 15 | 0:25
February  | 15 | 0:25
March  | 15 | 0:25
March  | 15 | 0:25

### Continuous Operation

Keep the tracker running seamlessly until I decide to exit, providing uninterrupted access to workout logging and progress tracking features.

### Google Sheets Integration

Sync workout logs and progress data with Google Sheets, leveraging the gspread library for seamless interaction and real-time updates, ensuring data accessibility and convenience for users.

### Future Features

Delete or update tables. 

[Back to top ⇧](#fitness-tracker)

## Technologies Used

### Language Used

* [Python3](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries and Programs Used

* [GitPod](https://gitpod.io/) was used for writing code, committing, and then pushing to GitHub.

* [GitHub](https://github.com/) was used to store the project after pushing.

* [Heroku](https://id.heroku.com/) was used to deploy the application.

* [PEP8 online check](http://pep8online.com/) was used to validate the Python code.

* [PrettyTable](https://pypi.org/project/prettytable/) library was used to present the data in table format.

* [Colorama](https://pypi.org/project/colorama/) library was used to apply color to the terminal text. 

* [Miro](https://miro.com/) was used to create the program flowchart.

[Back to top ⇧](#macro-calculator)

## Testing

### Testing User Stories

* As a user, I want to log my workouts.

* As a user, I want to view my workout log.

* As a user, I want to view my progress each month.

* As a user, I want the workouts and progress to be presented clearly.

* As a user, I want to understand the main objective of the program clearly to know its purpose.

* As a user, I want each step to be easy to comprehend, ensuring I provide the correct input without confusion.

* As a user, I expect clear feedback if I input incorrect data, helping me rectify mistakes efficiently.

### Code Validation

The [PEP8 online check](https://pep8ci.herokuapp.com/#) was used continuosly during the development proces to validate the Python code for PEP8 requirements.

![PEP8 Code Validation](assets/readme-files/pep8-code-validation.png)

### Manual Testing

#### Workout Date Format

<table>
    <tr>
        <th>Feature</th>
        <th>Outcome</th>
        <th>Example</th>
        <th>Pass/Fail</th>
    </tr> 
    <tr>
        <td rowspan=2>Menu Format</td>
        <td>Validates that input for the main menu choice is one of the valid options: 1, 2, 3, or 4.</td>
        <td><img src=assets/readme-files/main-menu-invalid.png alt="Age value is empty"></td>
        <td>Pass</td>
    </tr>
        <td>Validates that input for the submenu choice is one of the valid options: 1 or 2</td>
        <td><img src=assets/readme-files/sub-menu-invalid.png alt="Age value is too low"></td>
        <td>Pass</td>
    </tr>   
    <tr>
        <td>Data Entry</td>
        <td>Ensures that exactly 3 values are entered for each workout: day, month, distance, and duration.</td>
        <td><img src=assets/readme-files/values-invalid.png alt="Age value is empty"></td>
        <td>Pass</td>
    <tr>
        <td rowspan=2>Workout Date Format</td>
        <td>Validates the workout date format (Day Month).</td>
        <td><img src=assets/readme-files/age-empty.png alt="Age value is empty"></td>
        <td>Pass</td>
    </tr>
        <td>Validates the workout date format (Day Month).</td>
        <td><img src=assets/readme-files/age-low.png alt="Age value is too low"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan=2>Distance Validation</td>
        <td>Validates that the distance entered is a positive number.</td>
        <td><img src=assets/readme-files/age-empty.png alt="Age value is empty"></td>
        <td>Pass</td>
    </tr>
        <td>Validates the workout date format (Day Month).</td>
        <td><img src=assets/readme-files/age-low.png alt="Age value is too low"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan=4>Duration Format</td>
        <td>Validates that the duration follows the format "h:mm" (hours:minutes).</td>
        <td><img src=assets/readme-files/duration-format.png alt="Age value is empty"></td>
        <td>Pass</td>
    </tr>
        <td>Validates that the hours are between 0 and 9 (inclusive).</td>
        <td><img src=assets/readme-files/age-low.png alt="Age value is too low"></td>
        <td>Pass</td>
    </tr>
    </tr>
        <td>Validates that the minutes are between 0 and 59.</td>
        <td><img src=assets/readme-files/minutes-number-invalid.png alt="Age value is too low"></td>
        <td>Pass</td>
    </tr>
    </tr>
        <td>Ensures that the minutes are in a 2-digit format.</td>
        <td><img src=assets/readme-files/two-digit-invalid.png alt="Age value is too low"></td>
        <td>Pass</td>
    </tr>
</table>

[Back to top ⇧](#fitness-tracker)

## Deployment

The application has been deployed using [Heroku](https://id.heroku.com/) by following these steps:

[Heroku](https://id.heroku.com/) was used to deploy the application.

1. Create the requirements.txt file and run: `pip3 freeze > requirements.txt` in the console.
2. Commit changes and push them to GitHub.
3. Go to the Heroku's website.
4. From the Heroku dashboard, click on "Create new app".
5. Enter the "App name" and "Choose a region" before clicking on "Create app".
6. Go to "Config Vars" under the "Settings" tab.
7. Click on "Reveals Config Vars" and add the KEY: CREDS and the VALUE stored in creds.json file if needed.
8. Add the Config Var, KEY: PORT and VALUE: 8000.
9. Go to "Buildpacks" section and click "Add buildpack".
10. Select "python" and click "Save changes"
11. Add "nodejs" buildpack as well using the same process.
12. Go to "Deployment method", under the "Deploy" tab select "GitHub" and click on "Connect to GitHub".
13. Go to "Connect to GitHub" section and "Search" the repository to be deployed.
14. Click "Connect" next the repository name.
15. Choose "Automatic deploys" or "Manual deploys" to deploy your application.

[Back to top ⇧](#fitness-tracker)

## Credits

### Content

### Media

### Code
* [Stack Overflow](https://stackoverflow.com/) was consulted on a regular basis for inspiration and sometimes to be able to better understand the code being implement.

[Back to top ⇧](#fitness-tracker)

## Acknowledgements

* My tutor, Marcel, for his invaluable feedback and guidance.

* Code Institute and its amazing Slack community for their support and providing me with the necessary knowledge to complete this project.



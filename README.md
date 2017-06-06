# College Nicknames

This code was written as an Alexa skill that can be used with Amazon's voice activation products (Echo, Dot, etc).

This application will ask the user to provide the nickname for state colleges in a quiz like format. The application will keep track of the answers and provide a summary to the user at the end of the quiz with the number of correct answer. The application is configured as a lambda function and once the skill is associated with your Alexa device, the skill is activated with “Let’s play college nicknames”.

# Customization

All customizations are done to lib.py. 

Current customization:

GAME_LENGTH: 5

QUESTIONS: Pac 12 and Big 10 schools (All US schools are listed)

# Lambda Installation
1. Log into your AWS account
2. Click on Lambda service under Compute Services
3. Click on “Create Lambda function”
4. Click “Blank function”
5. For Configure Triggers select “Alexa Skills Kit” from the pull down, click Next
6. Select the following for “Configure function”
    * Name: choose a name for your function
    * Description: enter your description
    * Runtime: python 2.7
    * Code entry type: Upload a .zip file
        * zip up main.py and lib.py on your local compute
    * Function package: click upload and select the zip file you created above
    * Handler: main.lambda_handler
    * Role: Choose an existing role
    * Existing role: lambda_basic_execution
    * Click Next
7. Click Create function
8. Click Actions pulldown and click “configure test event”
9. Change sample event template to “Alexa Start Session”
10. Click Save and test
    * Successful test should list response JSON with text including “Let’s play College Nicknames…"

# Creators
Jerry Bearer and Darryl Wong

# Inspiration
The fun and challenge to create an Alexa app. It was also our final project for our University of Washington Python Programming Certificate Program.

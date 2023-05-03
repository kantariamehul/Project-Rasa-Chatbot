# Title: Virtual Assistant (Chatbot) for educational institute websites

Link of demonstration (16 min): https://youtu.be/0AW3Rc6Fa_M

Link of Slack App: https://app.slack.com/client/T035HH1EBRA/D03CF0Z51CK (Private)

# Requirements:
- Anaconda Navigator (2.1.2)
- Python (3.6 to 3.8)
- Rasa 3.1
- ngrok (to create path for slack integration)
- Visual Studio (as editter)
- pip (20.2)

# Installation Guide for widows 10 (64 bit)
- Install Anaconda Navigator (2.1.2)
- Create virtual environment "RasaEnv"
- Select python 3.6 or 3.7 or 3.8 versions only
- From "RasaEnv" start terminal from right side green button
- type "pip -V" to check the version if its not 20.2 then update the version by "pip install pip==20.2"
- check python version by "python -V". it should be 3.6 to 3.8
- install rasa by "pip install rasa", In the project Rasa 3.1 is used.
- "where.exe rasa" is used to check the location where rasa.exe is available in this "RasaEnv" environment.
- Then with "rasa init" create a basic project model and related files to be updated for further enhancements.
- by cd command change current directory to "RasaPro"
- create a folder named "RasaPro" at C:\Users\USERNAME\Anaconda3\envs\RasaEnv.
- provide the path to "C:\Users\USERNAME\Anaconda3\envs\RasaEnv\RasaPro" to create all project files
- By default it will be created in current directory which will create meash between exixting files and newlly created files
- So create a folder C:\Users\USERNAME\Anaconda3\envs\RasaEnv\RasaPro and specify the path.
- Select yes all the times to create project, train project and interact with project on command line arguments.
- Try with various inputs like Hi, Hello, Who are you?,bye to understand behavior of bot
- Now its time to updates all important files and once you are ready jump to Run updated files.

# Run exixting Rasa Project
- Open Anaconda / Open Anaconda prompt as administrator
- Open Environment "RasaEnv" and open command prompt from right side green button of the environment name. / Type "conda activate RasaEnv"
- change the directory to the folder "RasaPro" where all files are created
- use "cd C:\Users\USERNAME\Anaconda3\envs\RasaEnv\RasaPro" to change the directory
- Update files and run "rasa train" to train model with new inputs/files
- Run the updated project by "rasa shell"
- Enjoy the show :-).

# Additional functionalities
- Use "rasa interactive" command to visualise the ongoing process by RASA NLU instead of "rasa shell"
- Use "rasa visualize" command to verify the flow of the algorithm in flow chart format
- Use "rasa eveluate" command to verify test_stories and their sucess ratio
- Use "rasa test" command to evelauste all possible intents and get confucion metrix to identify possible changes in intents
- Use "rasa data validate" to evaluate performance of all test stories
- See all generated files in test folder for more detailed results.

# steps to create data base and required tables
- sqlite is used to store entity values from slots to database
- create a database files in actions folder
- use cd to make actions as surrent directory
- "sqlite mu_students.db" to create nu_students.db data base file to store email and enrollment information from slots.
- use "sqlite" command to enter in sqlite if db is already created.
- ".open mu_students.db" can be used to open already existing db file or use DB Browser (SQLite) to visualise the data base.
- Once database is created use ".databases" commad to know which data base is currenly selected and location of db.
- ".tables" can be used to check created table in data base. which will be empty as of now.
- Some times it os required to change the system path to actions folder. link:https://stackoverflow.com/questions/5920136/mysql-is-not-recognised-as-an-internal-or-external-command-operable-program-or-b
- Now create a table with Email and Enrollment titles of the columans with "CREATE TABLE mu_stu (Email NVARCHAR(50),Enrollment NVARCHAR(50));"
- Use "Select * from mu_stu" to see what data is stored in the db. which is empty as of now.
- refer email.py file to learn how to enter data in the db.
- Similarly create database adm_students with similar steps. refer Admission.py file for column titles and table name.

# Steps to verify slack integration
- install ngrok in base environment by "pip install ngrok" (not in RasaEnv)
- it will display https link with .io extension, copy it and paste at 3 different places in slack application
- We will require three separate terminals
- first one in base environemnt with "ngrok http 5005"
- secons one in rasa environment with "rasa run"
- third in rasa environent with "rasa run actions"
- Make sure test for ngrok https link in slack app is sucessfully linked
- now open chat bot application in slack application/environment on slack website or mobile app
- enjoy chat :)

WestJet Chatbot

Description:

This project shows a rule-based ChatBot for the airline company WestJet. I used various API keys from the AirLabs API website to pull all the information needed for the ChatBot. With the help of the API endpoints, I was able to incorporate real-time data into the ChatBot to provide maximum value for the user. 

I then used Pandas DataFrames to store this data in columns. Furthermore, I cleaned the data to remove any unnecessary columns and inconsistencies. This process made it easy for the ChatBot to access this information when called upon by the user.

Finally, through Loops, the ChatBot will ask the user many prompts to get the desired answer. 

The ChatBot has five functions:

* Booking a Flight
* Checking Daily Flight Schedules
* Baggage Assitance
* Online Check-IN
* File a claim

Getting Started: 

To use the WestJet chatbot, run the westjet_chatbot.py script in your Python environment. The script will begin running and prompt the user for input.

To access the SQLite database created by prompt 5, run the database_query.py script. The script will showcase all relevant data that the user has inputted.

Requirements:

The WestJet chatbot requires the following libraries to be installed:
* pandas
* sqlite3


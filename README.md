# CarSearchDatabase

#######install pip before hand if not working#######
#make sure to install pip

    python3 -m pip3 install --upgrade pip or pip3 install --upgrade pip

#to run our app create a virtual environment

    python3 -m venv venv

#activate the virtual environment

    source venv/bin/activate

#install the requirements to run the web app

    pip3 install -r requirements.txt

#change directory

    cd ./carsearchproject

#run the app
    
    python3 server.py or FLASK_APP=server.py flask run

#copy link and put it into any browser

#to navigate through our web app you need to use specific data that is found in our database

#There are many ways to navigate through a sqlite database, for our project we used an extension from visual studio code called SQLite by alexcvzz
#tha lets you visually see the data from our database. Right click on the database.sqlite file and "open database". open the sqlite explorer at the #bottom left of visual studio code. Click the database.sqlite. Press the play button on any of the buttons to see our data visually.

#Now using this data from the database you are able to navigate through our web app. this includes the logins data much more.

#once done deactivate the virtual environement
    
    deactivate

#######IF WINDOWS TRY THIS#######
#respectfully to the code that's giving you an error

#make virtual environment

        py -m venv venv
        
#activate virtual environment

        .\venv\Scripts\activate
        
#install requirments txt

        python3 -m pip3 install -r requirements.txt
        

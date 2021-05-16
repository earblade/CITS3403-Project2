# CITS3403-Project2

### Setup

Note: Python needs to be installed in system with correct path before going through these steps:

<b>Windows</b>

1. venv/Scripts/activate
2. cd flaskFiles
3. pip install -r requirements.txt
4. $env:FLASK_APP = "flaskFiles" - (provide the "FLASK_APP" environment variable)
5. flask run

6. To get out of running the website: (Keyboard) ctrl + c
7. To get out of virtual environment: deactivate

<b>Linux</b>

1. Activate the virtual environment

`source venv/bin/activate`

2. Go into the flask dir

`cd flaskFiles`

3. Install necessary libraries from

`pip3 install -r requirements.txt`

4. Check the current FLASK_APP environment variable with

`echo $FLASK_APP`

5. If it returns with `app`, skip this step, otherwise type in

`export FLASK_APP="app"`

6. Run the server with

`flask run`

---

### To handle databses

Currently there is only one table in the database.db file named user

To gain access to the database

1. sqlite3 databse.db

To Look at all the user data ( account information- Note passwords are hashed with sha256)

1. select \* from user;

To delete all user data in table

1. delete from user;

To list out all tables in database

1. .tables

---

### Timeline

[Demo for initial design concept using AdobeXD](https://xd.adobe.com/view/ef8babce-e4e8-4f4f-a5a0-3924df6be634-bad8/?fullscreen)

- Please refer to the _Projects_ tab to see what actions need to be done still

### Other

- Uses Bootstrap version 4.6

  Please refer to https://getbootstrap.com/docs/4.6/getting-started/introduction/

### Libraries

- https://animate.style/

### Theme

[Login Design](https://profile.w3schools.com/log-in?redirect_url=https%3A%2F%2Fmy-learning.w3schools.com)

### Resources

[Font](https://fonts.googleapis.com/css?family=Poppins)

[Homepage Image](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.savvymom.ca%2Fwp-content%2Fuploads%2F2020%2F01%2FOnline-Learning.jpg&f=1&nofb=1)

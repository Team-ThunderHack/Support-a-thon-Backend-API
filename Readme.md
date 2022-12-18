# Setup API at your localhost : 
  1 )Fork the repo <br/>
  2) Clone at local host <br/>
  3) Setup virtual env by `python3 -m venv env`<br/>
  4) Activate virtual env by `. env/bin/activate`<br/>
  5) Install all packages in requirements.txt by `pip install -r /path/to/requirements.txt` <br/>
  6) `cd interview`<br/>
  7) `python manage.py runserver`

# API Docs:

## End Points:

### 1) api/create (POST Method)
  Description : To create a user with the following details and save his/her details in the database.
  
  Parameters : <br />
  name => character Field<br />
  key => integer Field<br />
  email => character Field<br />
  password => character Field<br />
  
  Example : <br />
  `http://127.0.0.1:8000/create?name=ankur&email=ankur@gmail.com&password=1234567&key=73627`<br />
  
  Responses : <br />
  A ) If user is created and entered into DB : `User Created Successfully`<br />
  B) If key is invalid : `Invalid Key`<br />

### 2) api/authenticate (GET Method)
  Description : To check the password entered by the user.
  
  Parameters : <br />
  key => integer Field<br />
  email => character Field<br />
  password => character Field<br />
  
  Example : <br />
  `[http://127.0.0.1:8000/create?name=ashutosh&email=ashutosh@sample.com&password=123456&key=73627](http://127.0.0.1:8000/authenticate?email=ankur@gmail.com&password=1234567&key=73627)`<br />
  
  Responses : <br />
  A) If password is correct : `Correct Password`<br />
  B) If password is incorrect : `Incorrect Password`<br />
  C) If key is invalid : `Invalid Key`<br />
  
  ### 3) api/doAnalysis (GET Method)
  Description : To check the password entered by the user.
  
  Parameters : <br />
  key => integer Field<br />
  email => character Field<br />
  questionID => integer Field<br />
  path => character Field<br />
  
  Example : <br />
  `http://127.0.0.1:8000/doAnalysis?email=ashutosh@sample.com&key=73627&questionID=1&path=/Users/anilaswani/Desktop/interview/sample.wav`<br />
  
  Responses : <br />
  A) List with question ID , wpm, filled Words List and filler Phrases List<br />
  [
    "35",
    61.723602484472046,
    [
        "Like"
    ],
    []
]
<br/>
  B) If key is invalid : `Invalid Key`<br />
  
  ### 4) api/getDetails (GET Method)
  Description : To check the password entered by the user.
  
  Parameters : <br />
  key => integer Field<br />
  email => character Field<br />
  questionID => integer Field<br />
  
  Example : <br />
  `http://127.0.0.1:8000/getDetails?email=vijay@gmail.com&key=73627&questionID=1`
  
  Responses : <br/>
  A) List with question ID , wpm, filled Words List and filler Phrases List<br />
  [
    "vijay@gmail.com",
    35,
    61,
    "[\"Like\"]",
    "[]"
] <br/>
B) If key is invalid : `Invalid Key`<br />

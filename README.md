### Sample Application
<DESCRIPTION>
Application for checking useability of UUID in models. Postgres database is being used as database

  ### Installation
To setup, first create virtualenv and install dependencies via command:
```pip3 install -r requirements.txt```

## Running the Development Server

1. Apply migrations:
   ```bash
   python manage.py migrate
   ```

2. Run the server:
   ```bash
   python manage.py runserver
   ```
   
3. To create a user object, following json obj is being used for the endpoint ```http://localhost:8000/user/create/```
   ```
     {
      "email": "",
      "username":"",
      "first_name": "",
      "password": "",
      "last_name": ""
    }
    ```
4. To generate token, use the following json ``` {"username" :"jhonnny3", "password":"abc123"}``` for the endpoint ``` http://localhost:8000/token/```

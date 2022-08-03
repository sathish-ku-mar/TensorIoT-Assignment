# TensorIoT-Assignment

### System Requirements
- Python 3.7+
- Anaconda 3
------------
### 1. Create of virtual environment
Open the terminal and enter the following command:<br />`$ conda create -n <environment_name> python=3.7`<br />
Once the environment has been created, activate the environment:<br />`$ conda activate <environment_name>`

------------
### 2. Clone project to the local machine
In the terminal, navigate to the location where the project folder has to be created. Then enter the git command to clone the project:<br />`$ git clone https://github.com/sathish-ku-mar/TensorIoT-Assignment.git`<br />
Once cloned, change the directory to **TensorIoT-Assignment**<br />`$ cd TensorIoT-Assignment`

------------
### 3. Install the project requirements
Install the python packages listed in the **requirements.txt** file.
Enter the following command in the terminal:<br />`$ pip install -r requirements.txt`

------------

### 4. Run the development server
To start the development server, run the following command:<br />`$ flask run`<br />
By default the server runs on port`5000`<br />
Check whether the server is running by going to [http://127.0.0.1:5000/user/](http://127.0.0.1:5000/user/ "http://127.0.0.1:5000/user/")

------------
### 5. User login API
URL: http://127.0.0.1:5000/user/login/
Content-Type: application/json
Payload: {
    "email": "sathish@gmail.com",
    "password": "123456"
}

------------
### 6. User register API
URL: http://127.0.0.1:5000/user/register/
Content-Type: application/json
Payload: {
    "name": "sathish",
    "email": "sathish@gmail.com",
    "password": "123456"
}
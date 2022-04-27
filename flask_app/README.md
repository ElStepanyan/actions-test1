

## flask_info

  

Simple flask (python) application. Just show simple system information

  

Requrements:

 - python3 
 - pip3

  

ENV vars:

 - F_NAME (application name, will present in response)

 
For simple run: 

    pip install --no-cache-dir -r requirements.txt
    flask run

Build via docker: 

    docker build -t flask_info .

Run via docker: 

    docker run -p 5000:5000 flask_info (or you can use docker-compose)

Response example:

  

    {
    
    "application": "F_APP_DEFAULT",
    
    "architecture": "x86_64",
    
    "hostName": "27c883c75c74",
    
    "ipAddress": "172.17.0.2",
    
    "platform": "Linux",
    
    "processor": "",
    
    "ram": "63 GB"
    
    }





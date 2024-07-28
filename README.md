# Predictive Model

---

### Overview

- Web service that identifies digits captured within images
- Intended for use with the Classification UI and the Classification API



### API

- **URL:** https://localhost:5000/predict_value
- **Method:** GET
- **URL Request Parameters:**
  - file-path: text
    - Local file path of the image to be processed 
- **Response Status:** 200 OK
- **Example Response Value:**
  - "Digit value for image: [8]"



### Environment Configuration

- Download Python

- Create a virtual environment

  ```
  >> python -m venv env
  
  >> source env/Scripts/activate
  ```

- Import the libraries that are used

  ```
  >> python -m pip install -U jupyter numpy matplotlib pandas scipy scikit-learn
  ```

- Install Flask

  ```
  >> pip install Flask
  ```

- Create a self-signed certificate

  ```
  >> mkdir certs && cd certs
  
  >> openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 3650
  ```

- Register SSL cert with Java Keystore (run as an admin)

  ```
  >> keytool -importcert -file cert.pem -keystore "C:\Program Files\Java\jdk-17\lib\security\cacerts"
  ```

  

### Run the Application

- Start the web server from the project root directory, */predictive-model*

  ```
  >> export FLASK_APP=controller.py
  
  >> python controller.py
  ```



### Test the API from the Browser

- Write a number down on a piece of paper, take a picture of it and upload the picture to the project root directory, */predictive-model* with the file name *image-name.jpg*
- Enter URL *https://localhost:5000/predict_value?file-path=image-name.jpg*
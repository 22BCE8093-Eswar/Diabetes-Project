# Diabetes Flask App 

This project is a simple Flask web application deployed on **Render**.  

url: https://diabetes-web-xcmp.onrender.com/

---

### 1. Files Setup

#### `app.py`
Your main Flask app file.  
Make sure it defines the Flask instance as `app`:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Render Deployment!"
````

requirements.txt
List all dependencies here. For example:
````
Flask==3.0.3
gunicorn==23.0.0
````

You can generate this file with:
````
pip freeze > requirements.txt
````

Procfile

This tells Render how to run your app:
````
web: gunicorn app:app
````


gunicorn = WSGI server for production

app:app = <filename>:<Flask instance> → Here, app.py has app = Flask(__name__)

runtime.txt
Specify Python version:

````
python-3.11.8
(Render supports only certain versions, check Render Python docs)
````


### 2. Deployment on Render
Push your project to GitHub.

Go to Render Dashboard.

Click New + → Web Service.

Connect your GitHub repo.

Fill in:

Build Command:
````
pip install --upgrade pip setuptools wheel && pip install -r requirements.txt
````

Start Command:
````
gunicorn app:app
````


Deploy 


### 3. Verify
   
Once deployed, open the Render-provided URL.

Update requirements.txt whenever you install new libraries.

Restart deployment from Render after changes.

If using templates/static, keep proper folder structure:

````
/templates
/static
````

📌 Example Local Run
````
pip install -r requirements.txt
python app.py
````

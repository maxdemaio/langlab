# langlab - An open source language learning website
![Photo of the website](/static/images/website_picture.png)

#### Welcome to LangLab! It's an open-source foreign language learning website for language learners of all levels.

### What is this website for?
It's for practicing the conjugations of the 25 most common verbs of a target language and finding great resources you enjoy to supplement learning.

### Why did you create this website?
I wanted to make a website where language learners (mostly beginner-intermediate level) can practice their skills and have a home base for resources.

When I was learning French in middle school, I found it very easy to rank up my skills by quickly running through conjugations with instant feedback. Coupled with content you like watching/reading, the language learning process can become not only fun, but very efficient.

### What did you use to build this website?
I used Python (Django) for the backend, PostgreSQL for database management, Bootstrap for the frontend, and Heroku for deployment. I'm planning on adding either Vue.js or React on top of the current stack and using Namecheap for domain registration.

---

## How to run this web app locally

### 1. Install the requirements within `requirements.txt` using pip

After cloning the repository onto your machine, navigate to the project's directory. For this step, the ideal setup would be creating and activating a virtual environment (venv) then installing all the requirements.

#### A) Venv setup

Run the following commands:
1) Create a venv with the name "langlab_ENV"
2) Activate the venv

```console
python -m venv langlab_ENV
langlab_ENV\scripts\activate.bat
```

Now, from the project directory you can run:

```console
pip install -r requirements.txt
```

### 2. Migrate and run your server

1) Set yourself a `SECRET_KEY` in `settings.py`
2) Make the migrations to setup the tables in your SQLite database:

```console
python manage.py migrate 
```

3) Import all of the conjugate app data:

```console
python manage.py shell
from conjugate import conj_db_import
conj_db_import.lang_import_all()
exit()
```

4) Start up the app:

```console
python manage.py runserver
```

### 3. Want to contribute?

Thank you! That would be great. Please feel free to send any pull requests here.


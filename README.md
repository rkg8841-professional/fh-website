# fh-website
I am creating a website that displays results of my different projects in one spot. 

The projects are listed below :






For a basic Flask project, you typically need the following folder structure:

/venv: This folder contains the Python virtual environment. It's created when you set up the virtual environment and should not be manually created or included in your repository.

/app or /src: This directory will contain your Flask application package. It's where you'll store your Python modules, templates, and static files.

/templates: This folder is for your HTML templates. Flask automatically looks for templates in a folder named templates inside your application package.

/static: This folder is for static files like CSS, JavaScript, and images. Flask serves static files from a folder named static in your application package.

/tests: This directory will contain your unit tests. Organizing tests in their own directory helps keep your project clean.

/instance: Flask supports instance folders for configuration that shouldn't be version-controlled, such as secrets and database file paths. This folder is optional and depends on your application's needs.

Root files: In the root of your project, you'll typically have:

app.py or run.py: The entry point to your Flask application.
requirements.txt: A file listing your project's dependencies. You can generate this file using pip freeze > requirements.txt.
.gitignore: This file tells Git which files or folders to ignore in your project. You should at least include /venv and any .pyc files.
README.md: A Markdown file providing an overview of your project, setup instructions, and other essential information.


Viewing output of docker

docker build -t my-flask-app .

docker run -p 4000:5000 my-flask-app


to run pytest you need to run this in terminal :

export PYTHONPATH="${PYTHONPATH}:/path/to/your/project"

Project Structure
Code: Github
Docker Image: Docker Hub
Host: 
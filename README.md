
#  Django Todo List

The Django Todo List application is a simple yet functional web app that allows users to manage tasks. Built using **Python** and **Django**, it features task creation, completion, and deletion functionalities with a clean user interface powered by **Bootstrap**.

---
## Live Demo

View the Todo-list live https://todo-list-pitv.onrender.com

---
##Screenshot
![image](https://github.com/user-attachments/assets/b0ae011e-f681-4100-890c-7893e5018bd3)

---

##  Features

* Create new tasks with a title and description
* View a list of all tasks
* Mark tasks as completed
* Delete tasks
* Responsive design using Bootstrap 4

---

## Technologies Used

* **Backend**: Python, Django (MVC framework)
* **Frontend**: HTML, Bootstrap 4
* **Database**: SQLite (Django’s default)
* **Others**: Django Templating Language, CSRF protection

---

##  Project Structure

* **Project Root**: Contains Django project configuration and management script
* **App (`todoapp`)**: Contains models, views, URLs, and templates for the todo functionality
* **Templates Folder**: Stores HTML templates (primarily `index.html`)

---

## Setup Instructions

1. Clone or download the project
2. Set up a Python virtual environment
3. Install required packages using pip
4. Create and apply database migrations
5. Run the development server
6. Open the application in your browser at `http://127.0.0.1:8000/`

---

##  App Functionality

* **Homepage (`/`)**: Displays a form to create new tasks and a table listing all current tasks
* **Add Task**: Form submission creates a new task entry in the database
* **Complete Task**: Clicking the "Completed" button updates the task's status
* **Delete Task**: Removes the task from the database

---

##  URL Routing

* `/` – View all tasks
* `/create/` – Create a new task
* `/complete/<id>/` – Mark task as completed
* `/delete/<id>/` – Delete task

---

##  Logic & Flow

* Views handle both data processing and interaction with the model
* Templates dynamically display data using Django template tags
* Bootstrap provides styling and responsiveness
* User inputs are protected using Django’s built-in CSRF protection

---

## User Interface

* Simple and clean layout using Bootstrap
* Table format for listing tasks with actions for each
* Form at the top for adding new tasks
* Visual badge for completed tasks



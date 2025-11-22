# Task-Manager

Task-Manager is a simple and intuitive web application built with **Flask** and **Firebase** for managing your daily tasks. You can add, edit, and delete tasks, with real-time updates stored in Firebase Firestore. The project is deployed and accessible online.

---

## **Deployed Link**

[View Live App on PythonAnywhere](https://appinedisony.pythonanywhere.com/)

---

## **Features**

- Add new tasks with descriptions
- Edit or delete existing tasks
- Real-time data storage with Firebase Firestore
- Clean and user-friendly interface
- Fully deployed and accessible online

---

## **Technologies Used**

- **Frontend:** HTML, CSS
- **Backend:** Python, Flask
- **Database:** Firebase Firestore
- **Deployment:** PythonAnywhere
- **Other:** Firebase Admin SDK for backend integration

---

## **Setup Instructions (Local Development)**

**1. Clone the repository:**

--bash
git clone https://github.com/YourUsername/Task-Manager.git
cd Task-Manager

**2. Create and activate a virtual environment:**

python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

**3. Install required packages:**

pip install -r requirements.txt

**4. Add Firebase credentials:**
Upload your Firebase service account JSON file into the project folder.

Ensure app.py points to the JSON correctly:

import os
json_path = os.path.join(os.path.dirname(__file__), 'task-manager-5d189-firebase-adminsdk-fbsvc-faa872437a.json')

**Important**: The Firebase JSON file is not included in this repo for security reasons. To run locally or deploy, upload your own Firebase service account JSON to the project folder.

**5. Run the app locally:**

python app.py

Open http://127.0.0.1:5000 in your browser.

**FOLDER STRUCTURE**
Task-Manager/
│
├── app.py                     # Main Flask application
├── templates/                 # HTML templates
├── static/                    # CSS, JS
├── task-manager-5d189-firebase-adminsdk-fbsvc-faa872437a.json  # Add manually
├── requirements.txt
└── README.md

## **Usage**

- Open the app in your browser.
- Add a new task by typing in the input field and clicking "Add".
- Edit a task by clicking the "Edit" button next to it.
- Delete a task by clicking the "Delete" button.
- All tasks are saved in Firebase Firestore and update in real time.






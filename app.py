import os
import json
import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import uuid

# Firebase Setup
json_path = os.path.join(os.getcwd(),"task-manager-5d189-firebase-adminsdk-fbsvc-faa872437a.json")
cred=credentials.Certificate(json_path)
firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)
app.secret_key = "task-secret-key"

# ------------- HOME -------------
@app.route("/")
def index():
    tasks_ref = db.collection("tasks").order_by("created_at")
    tasks = [dict(id=t.id, **t.to_dict()) for t in tasks_ref.stream()]
    return render_template("index.html", tasks=tasks)


# ------------- ADD TASK -------------
@app.route("/task/add", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        data = {
            "title": request.form["title"],
            "description": request.form.get("description", ""),
            "due_date": request.form.get("due_date", ""),
            "completed": False,
            "created_at": datetime.utcnow(),
            "history": [
                {"action": "Created", "time": datetime.utcnow()}
            ]
        }
        db.collection("tasks").add(data)
        flash("Task added successfully!", "success")
        return redirect(url_for("index"))

    return render_template("add_edit.html", action="Add")


# ------------- EDIT TASK -------------
@app.route("/task/<task_id>/edit", methods=["GET", "POST"])
def edit_task(task_id):
    task_ref = db.collection("tasks").document(task_id)
    task = task_ref.get().to_dict()

    if request.method == "POST":
        updated = {
            "title": request.form["title"],
            "description": request.form.get("description", ""),
            "due_date": request.form.get("due_date", ""),
            "completed": request.form.get("completed") == "on",
        }

        # Add a history event
        task["history"].append({"action": "Updated", "time": datetime.utcnow()})

        task_ref.update({**updated, "history": task["history"]})
        flash("Task updated!", "success")
        return redirect(url_for("index"))

    return render_template("add_edit.html", action="Edit", task=task, id=task_id)


# ------------- DELETE -------------
@app.route("/task/<task_id>/delete", methods=["POST"])
def delete_task(task_id):
    db.collection("tasks").document(task_id).delete()
    flash("Task deleted.", "info")
    return redirect(url_for("index"))


# ------------- TOGGLE COMPLETE -------------
@app.route("/task/<task_id>/toggle", methods=["POST"])
def toggle(task_id):
    task_ref = db.collection("tasks").document(task_id)
    task = task_ref.get().to_dict()

    task["completed"] = not task["completed"]
    task["history"].append({
        "action": "Marked complete" if task["completed"] else "Marked incomplete",
        "time": datetime.utcnow()
    })

    task_ref.update(task)
    return redirect(url_for("index"))


# ------------- VIEW HISTORY -------------
@app.route("/task/<task_id>/history")
def history(task_id):
    task = db.collection("tasks").document(task_id).get().to_dict()
    return render_template("history.html", task=task)


if __name__ == "__main__":
    app.run(debug=True)

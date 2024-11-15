from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory database (for demonstration)
tasks = {}
task_id_counter = 1

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(list(tasks.values())), 200

@app.route("/tasks", methods=["POST"])
def add_task():
    global task_id_counter
    data = request.get_json()
    if "task_name" not in data:
        abort(400, description="Task name is required")
    
    task = {
        "id": task_id_counter,
        "task_name": data["task_name"],
        "completed": data.get("completed", False)
    }
    tasks[task_id_counter] = task
    task_id_counter += 1
    return jsonify(task), 201

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    if task_id not in tasks:
        abort(404, description="Task not found")
    
    data = request.get_json()
    task = tasks[task_id]
    task["task_name"] = data.get("task_name", task["task_name"])
    task["completed"] = data.get("completed", task["completed"])
    return jsonify(task), 200

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    if task_id not in tasks:
        abort(404, description="Task not found")
    
    del tasks[task_id]
    return jsonify({"message": "Task deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)

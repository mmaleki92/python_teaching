from fastapi import FastAPI, HTTPException
from typing import List

app = FastAPI()

# Store tasks and user answers in memory (replace with a database in a production scenario)
tasks = [
    {"id": 1, "question": "What is the capital of France?", "correct_answer": "Paris"},
    {"id": 2, "question": "What is 2 + 2?", "correct_answer": "4"},
]

user_answers = {}

# Endpoint to broadcast tasks
@app.get("/broadcast_tasks", response_model=List[dict])
def broadcast_tasks():
    return tasks

# Endpoint to submit answers
@app.post("/submit_answer/{task_id}")
def submit_answer(task_id: int, answer: str, user_name: str):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    correct_answer = task["correct_answer"]

    # Grade the answer (simple matching for demonstration purposes)
    is_correct = answer.lower() == correct_answer.lower()
    grade = 1 if is_correct else 0

    # Store user answer and grade
    user_answers[user_name] = {"task_id": task_id, "answer": answer, "grade": grade}

    return {"message": "Answer submitted successfully"}

# Endpoint to display grades
@app.get("/display_grades")
def display_grades():
    return user_answers

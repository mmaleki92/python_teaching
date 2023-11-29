import requests

base_url = "http://127.0.0.1:8000"  # Replace with the correct URL of your FastAPI server

def print_response(response):
    print("Status Code:", response.status_code)
    print("Response Content:", response.json())
    print("\n")

# GET: Broadcast tasks
response = requests.get(f"{base_url}/broadcast_tasks")
print("GET /broadcast_tasks:")
print_response(response)

# POST: Submit answers
task_id = 1
answer = "Paris"
user_name = "Alice"
response = requests.post(f"{base_url}/submit_answer/{task_id}", json={"answer": answer, "user_name": user_name})
print(f"POST /submit_answer/{task_id}:")
print_response(response)

# Display grades
response = requests.get(f"{base_url}/display_grades")
print("GET /display_grades:")
print_response(response)

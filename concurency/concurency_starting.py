import time

def simulate_task(task_name, duration):
    print(f"Starting {task_name}")
    time.sleep(duration)
    print(f"Completed {task_name}")

# Concurrent execution
simulate_task("Task A", 2)
simulate_task("Task B", 2)
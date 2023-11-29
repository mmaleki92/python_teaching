import threading
import redis

# Connect to Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

# Subscribe to a channel
pubsub = redis_client.pubsub()
pubsub.subscribe('my_channel')

# Function to handle incoming messages
def handle_messages():
    for message in pubsub.listen():
        if message['type'] == 'message':
            print(f"Received message: {message['data']}")

# Start a thread to handle incoming messages
handle_thread = threading.Thread(target=handle_messages)
handle_thread.start()

# Keep the main thread alive to continue receiving messages
handle_thread.join()

import redis
import time

# Connect to Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

# Function to publish messages to a channel
def publish_messages():
    i = 0
    while True:
        i += 1
        message = f"Message {i + 1}"
        print(f"Publishing: {message}")
        redis_client.publish('my_channel', message)
        time.sleep(1)  # Simulating some delay between messages

# Start publishing messages
publish_messages()

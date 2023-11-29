import redis

# Connect to a local Redis server (default configuration)
redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

# Test the connection
print("Connected to Redis")

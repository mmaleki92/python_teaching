import redis

# Connect to a local Redis server (default configuration)
redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

# Test the connection
print("Connected to Redis")
# Set a key-value pair
redis_client.set('my_key', 'Hello, Redis!')

# Get the value by key
value = redis_client.get('my_key')
print("Value retrieved:", value)
# Push values to the end of a list
redis_client.rpush('my_list', 'item1', 'item2', 'item3')

# Retrieve the list
my_list = redis_client.lrange('my_list', 0, -1)
print("List contents:", my_list)

# Push values to the end of a list
redis_client.rpush('my_list', 'item1', 'item2', 'item3')

# Retrieve the list
my_list = redis_client.lrange('my_list', 0, -1)
print("List contents:", my_list)
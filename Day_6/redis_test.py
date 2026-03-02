# r = redis.Redis(unix_socket_path='/tmp/redis.sock')

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)

r = redis.Redis(connection_pool=pool)


#1. Install redis: brew install redis

#2. run server: redis-server  (remember port)

#3. if show url: redis-cli

#4. pip install redis fastapi uvicorn httpx

------------------------------------------------
Redis Bacis
#1. set name soton (name is key & soton is value)

#2. get name

#3. del name

#4. check value: exists name

#5. check all key in database: keys *

#6. delete value after 10 sec: expire name 10

#7. set with expire time: setex name 10 soton

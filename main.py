from fastapi import FastAPI
from redis import Redis
from httpx import AsyncClient
import json

app = FastAPI()


@app.on_event('startup')
async def startup_event():
    app.state.redis = Redis(host='localhost', port=6379, db=0)
    app.state.http_client = AsyncClient()


@app.on_event('shutdown')
async def shutdown_event():
    app.state.redis.close()


@app.get('/entries')
async def read_item():
    value = app.state.redis.get('entries')

    if value is None:
        response = await app.state.http_client.get('https://api.publicapis.org/entries')
        value = response
        data_str = json.dumps(value)
        app.state.redis.set('entries', data_str)

    return json.loads(value)

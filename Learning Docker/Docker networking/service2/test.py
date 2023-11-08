import redis
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    r = redis.Redis(host="redis", port=6379)
    return {"result": str(r)}


if __name__ == "__main__":
    uvicorn.run("test:app", reload=True, host="0.0.0.0", port=8000)

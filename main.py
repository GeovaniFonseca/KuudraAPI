from fastapi import FastAPI
import random
import uvicorn

app = FastAPI()

@app.get("/")
def read_root();
    return {"Hello": "World"}

@app.get("/random")
def read_random():
    return random.randint(0, 6)

if __name__ = "__main__":
    uvicorn.run("main:app", port=8000, reload=True)


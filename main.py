from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/')
def index():
    # task = create_task.delay(20, 1, 3)
    return {"message": "hello"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=False)
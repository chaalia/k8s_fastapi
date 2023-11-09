from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def norma_root():
    return {"Rejeb": "Welcome to Fastapi with K8S"}

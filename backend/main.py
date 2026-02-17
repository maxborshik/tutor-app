from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"status": "Backend is Online", "framework": "FastAPI"}


@app.get("/health")
def health_check():
    return {"status": "ok"}

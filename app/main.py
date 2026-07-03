from fastapi import FastAPI

app = FastAPI(
    title="SearchX API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to SearchX 🚀"
    }
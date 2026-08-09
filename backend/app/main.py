from fastapi import FastAPI

app = FastAPI(
    title="BeeERP",
    version="0.1"
)


@app.get("/")
def root():
    return {
        "Hola Pepsicola"
    }
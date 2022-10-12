from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

from fastapi.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def redirect_to_chatbot():
    return RedirectResponse("static/index.html")

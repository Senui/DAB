from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")  # Create a templates directory and place your HTML templates there

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/process_doi")
async def process_doi(doilist: str = Form(...)):
    # Call your API with the list of DOIs here
    # Substitute this with your actual API call
    # result = call_api(doilist)
    result = "This is a placeholder result."
    return templates.TemplateResponse("result.html", {"result": result})

if __name__ == '__main__':
    uvicorn.run('app2:app', host="127.0.0.1", port=8081)

from fastapi import FastAPI
import uvicorn

from .services.data_access_request_handler import DataAccessRequestHandler
from .utils.setup_logging import setup_logging

app = FastAPI()

@app.post("/data-request/")
async def create_data_request():
    # Logic to handle data request
    pass

# Add more endpoints as needed

if __name__ == '__main__':
    setup_logging()
    uvicorn.run('app:app', host="127.0.0.1", port=8081)

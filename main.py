from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from pydantic import BaseModel
from fastapi import Request
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class User(BaseModel):
    user: str


@app.post('/')
def main(user: User):
    return user



@app.get("/")
async def index():
    return FileResponse("index.html")


users = []
@app.post("/login/")
async def login(request: Request):
    # users.append({"username": username, "password": password})
    # return {"username": username, "password": password}
    try:
        json = await request.json()
        print(json)
        return json
    except:
        return 'Invalid JSON data.'
    return await request.json()


@app.get("/users/")
async def get_users():
    return users                         

                                         
@app.get("/user/{user_id}")              
async def read_user(user_id: int):
    return users[user_id]

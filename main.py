from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# allow browser requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# create a Jinja2 template engine
templates = Jinja2Templates(directory="static")

# serve the html file to root path
@app.get("/", response_class=HTMLResponse)
def login_serve(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

class LoginData(BaseModel):
    username: str
    password: str

# handle login post request
@app.post("/login")
def handle_login(data: LoginData):
    print(f"receiverd login data:{data.username}, {data.password}")

    if data.username == "username" and data.password == "password":
        return {"message": "login successful"}
    else:
        return JSONResponse(status_code= 401, content={"message": "login failed"})
    
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
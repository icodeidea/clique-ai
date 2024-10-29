from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from chainlit.auth import create_jwt
from chainlit.user import User
from chainlit.utils import mount_chainlit
from starlette.responses import RedirectResponse
from starlette.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root(request: Request):
    print('hi')

@app.get("/custom-auth")
async def custom_auth():
    # Verify the user's identity with custom logic.
    token = create_jwt(User(identifier="Test User"))
    return JSONResponse({"token": token})

mount_chainlit(app=app, target="assistant.py", path="/chat")

from typing import Any, Dict, TYPE_CHECKING
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

if TYPE_CHECKING:
    # Give mypy a fake version of the route
    def read_root() -> Dict[str, str]: ...

else:

    @app.get("/", response_class=JSONResponse)
    def read_root() -> JSONResponse:
        return JSONResponse(
            content={"message": "Welcome to MyApp – your FastAPI project is running!"}
        )

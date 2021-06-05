from os import environ
from dotenv import dotenv_values
from dotenv import load_dotenv
from pathlib import Path
load_dotenv(Path("./env.dev"))
load_dotenv(Path("./env"))
ENVS = {
    **dotenv_values("env.dev"),  # load shared development variables
    **dotenv_values("env"),  # load sensitive variables
    **environ,  # override loaded values with environment variables
}


def is_in() -> bool:
    return "DETA_KEY" in ENVS
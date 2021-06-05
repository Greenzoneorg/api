from os import environ
from dotenv import dotenv_values
from dotenv import load_dotenv
from pathlib import Path
ENVS = {
    **dotenv_values("env.dev"),  # load shared development variables
    **dotenv_values("env"),  # load sensitive variables
    **environ,  # override loaded values with environment variables
}

load_dotenv(Path("./env.dev"))
load_dotenv(Path("./env"))
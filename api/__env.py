from os import environ
from dotenv import dotenv_values

ENVS = {
    **dotenv_values(".env.dev"),  # load shared development variables
    **dotenv_values(".env"),  # load sensitive variables
    **environ,  # override loaded values with environment variables
}

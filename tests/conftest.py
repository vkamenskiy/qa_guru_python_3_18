import os

import pytest
from dotenv import load_dotenv

from utils.base_session import BaseSession

load_dotenv()


@pytest.fixture(scope='session')
def reqres():
    api_url = os.getenv('REQRES_API_URL')
    return BaseSession(api_url)


@pytest.fixture(scope='session')
def demoshop():
    api_url = os.getenv('DEMOSHOP_API_URL')
    return BaseSession(api_url)


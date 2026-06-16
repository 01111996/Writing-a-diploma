import pytest
from utils.browser import create_driver


@pytest.fixture(scope='session')
def driver():
    a = create_driver()
    yield a
    a.quit()
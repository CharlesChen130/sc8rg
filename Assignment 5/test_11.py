#log in with a username that does not exist in users data but password is in data
import pytest
import System

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

def test_login_wrong_username(grading_system):
    name = 'Songxi Chen'
    password = '123454321'
    grading_system.login(name, password)



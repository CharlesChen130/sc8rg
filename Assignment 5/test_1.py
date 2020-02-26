import pytest
import System

def test_login(grading_system):
    name = 'cmhbf5'
    password = 'bestTA'
    grading_system.login(name, password)
    assert name == grading_system.usr.name

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

#pass    
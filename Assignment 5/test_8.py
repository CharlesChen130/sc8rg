import pytest
import System

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

def test_check_ontime(grading_system):
    name = 'akend3'
    password = '123454321'
    grading_system.login(name, password)
    assert grading_system.usr.check_ontime('02/24/20', '02/26/20')
    assert not grading_system.usr.check_ontime('02/26/20', '02/24/20')

#fail      
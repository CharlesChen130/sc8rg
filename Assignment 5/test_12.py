#Student checks grade of course that he is not in. 
import pytest
import System

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

def test_check_grades_wrong_course(grading_system):
    name = 'akend3'
    password = '123454321'
    grading_system.login(name, password)
    course='software_engineering'
    grades=grading_system.usr.check_grades(course)
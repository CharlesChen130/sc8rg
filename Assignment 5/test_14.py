#Professor drops a student from a course that he is not in charge of
import pytest
import System

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

def test_drop_wrong_professor(grading_system):
    name = 'goggins'
    password = 'augurrox'
    grading_system.login(name, password)
    course='comp_sci'
    studentname='akend3'
    courseset=grading_system.usr.courses
    assert course in courseset
    grading_system.usr.drop_student(studentname, course)

#Professor drops a student that is not in the class
import pytest
import System

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

def test_drop_wrong_student(grading_system):
    name = 'goggins'
    password = 'augurrox'
    grading_system.login(name, password)
    course='databases'
    studentname='yted91'
    student=grading_system.users[studentname]['courses']
    assert course in student
    grading_system.usr.drop_student(studentname, course)
import pytest
import System

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

def test_drop_student(grading_system):
    name = 'goggins'
    password = 'augurrox'
    grading_system.login(name, password)
    course='databases'
    studentname='hdjsr7'
    grading_system.usr.drop_student(studentname, course)
    student=grading_system.users[studentname]['courses']

    flag=0
    for key in student:
        if key == course:
            flag=1
    
    assert flag == 0

#pass      
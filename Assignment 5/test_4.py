import pytest
import System

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

def test_create_assignment(grading_system):
    name = 'cmhbf5'
    password = 'bestTA'
    grading_system.login(name, password)
    newassignment='assignment3'
    duedate='02/16/20'
    course='databases'
    grading_system.usr.create_assignment(newassignment, duedate, course)
    assignment=grading_system.courses[course]['assignments']

    for key in assignment:
        if key == newassignment:
            date=grading_system.courses[course]['assignments'][newassignment]['due_date']
    
    assert date == duedate

#pass  
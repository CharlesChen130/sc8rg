import pytest
import System

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

def test_view_assignments(grading_system):
    name = 'akend3'
    password = '123454321'
    grading_system.login(name, password)
    course='databases'
    assignments=grading_system.usr.view_assignments(course)

    for key in assignments:
        assert key[0] in grading_system.courses[course]['assignments']
        assert key[1] == grading_system.courses[course]['assignments'][key[0]]['due_date']

#fail
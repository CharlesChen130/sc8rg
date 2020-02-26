import pytest
import System

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

def test_check_grades(grading_system):
    name = 'akend3'
    password = '123454321'
    grading_system.login(name, password)
    course='databases'
    grades=grading_system.usr.check_grades(course)

    for key in grades:
        assert key[0] in grading_system.users[name]['courses'][course]
        assert key[1] == grading_system.users[name]['courses'][course][key[0]]['grade']

#pass      
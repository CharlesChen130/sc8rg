import pytest
import System

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

def test_submit_assignment(grading_system):
    name = 'akend3'
    password = '123454321'
    grading_system.login(name, password)
    course='databases'
    assignment='assignment1'
    date='02/26/20'
    submission='FFF'
    grading_system.usr.submit_assignment(course, assignment,submission, date)
    studentassignment=grading_system.users[name]['courses'][course][assignment]

    assert studentassignment['submission_date'] == date
    assert studentassignment['submission'] == submission
    assert not assignment['ontime']

#fail   
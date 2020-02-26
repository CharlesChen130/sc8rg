import pytest
import System

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

def test_change_grade(grading_system):
    name = 'cmhbf5'
    password = 'bestTA'
    grading_system.login(name, password)
    newgrade=67
    grading_system.usr.change_grade('akend3', 'databases', 'assignment1', newgrade)
    grades=grading_system.usr.check_grades('akend3','databases')

    for key in grades:
        if key[0] == "assignment1":
            grade=key[1]
    
    assert grade == newgrade

#fail

"""
gradingSystem = System.System()
gradingSystem.load_data()
name = 'cmhbf5'
password = 'bestTA'
gradingSystem.login(name, password)
newgrade=23
gradingSystem.usr.change_grade('akend3', 'databases', 'assignment1', newgrade)
grades=gradingSystem.usr.check_grades('akend3','databases')
print(grades)    
"""
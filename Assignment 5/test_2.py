import pytest
import System

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

def test_check_password(grading_system):
    assert grading_system.check_password('cmhbf5','bestTA')
    assert not grading_system.check_password('cmhbf5','bestta')
    assert not grading_system.check_password('cmhbf5','BESTTA')

#pass  
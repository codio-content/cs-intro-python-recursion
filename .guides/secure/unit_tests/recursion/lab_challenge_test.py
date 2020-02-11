# Import student function form the newly copied file
from lab_challenge import recursive_power

# Import system and os modules
import sys, os

# File path and name of student code
path = ".guides/secure/unit_tests/recursion"
file = "lab_challenge.py"
student_code = os.path.join(path, file)

def is_recursive(file):
  recursion_count = 0
  with open(file, "r") as code_to_check:
    for line in code_to_check.readlines():
      if "recursive_power" in line and "print" not in line:
        recursion_count += 1
    return recursion_count > 1

# Homemade unit test, call student function w/ instructor input & output
def test_student_code():
    """Homemade unit test for student work
    Return True if all of the tests pass
    Return False if at least one test fails"""
    
    # Boolean variables for each test
    test1 = False
    test2 = False
    test3 = False
    test4 = False
    
    # Print title for visual feedback
    print("<h2>Testing your code...</h2>")
    
    # First test case
    if recursive_power(5, 5) == 3125:
        test1 = True
        print("Test 1 <b>passed</b>.")
    else:
        print("Test 1 did <b>not pass</b>.")
        
    # Second test case
    if recursive_power(8, 4) == 4096:
        test2 = True
        print("Test 2 <b>passed</b>.")
    else:
        print("Test 2 did <b>not pass</b>.")
        
    # Third test case
    if recursive_power(6, 7) == 279936:
        test3 = True
        print("Test 3 <b>passed</b>.")
    else:
        print("Test 3 did <b>not pass</b>.")
    
    # Test to see if recursion is being used
    test4 = is_recursive(student_code)
    if test4:
      print("Test 4 <b>passed</b> - recursion used")
    else:
      print("Test 4 did <b>not pass</b> - recursion not used")
    
    # Return results of the unit tests
    print("<hr>")
    if test1 and test2 and test3 and test4:
        return True
    else:
        return False

# Print final results of the unit test
if test_student_code():
    print("<h3>All tests passed!</h3>")
    sys.exit(0)
else:
    print("<h3>Not all of the tests passed.</h3>")
    sys.exit(1)
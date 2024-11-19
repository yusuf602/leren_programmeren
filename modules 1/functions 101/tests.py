import test_lib
from test_lib import test, report
from function import biggest 

expected = "Beide getallen zijn even groot" 
result = biggest(23, 23)
test('TEST nr1=nr2', expected, result)

expected = 'Maximum: 44 en minimum: 20'
result = biggest(44,20)
test('TEST nr1>nr2', expected, result)

expected = "Maximum: 44 en minimum: 23" 
result = biggest(23, 44) 
test('TEST nr1<nr2', expected, result)

if __name__ == "__main__":
    report()
from test_lib import *
ROUND_TO = 5
bedrag = 10.99

def afronden_op_stuiver(bedrag):
    centen = round(bedrag)
    afgeronde_centen = round(bedrag * 100 / ROUND_TO) * 5 / 100
    return afgeronde_centen


expected = 10.55
result = afronden_op_stuiver(10.53)
test('test 1', expected, result)

expected = 33.55
result = afronden_op_stuiver(33.56)
test('test 1', expected, result)

expected = 14.55
result = afronden_op_stuiver(14.54)
test('test 1', expected, result)

expected = 1.60
result = afronden_op_stuiver(1.59)
test('test 1', expected, result)

expected = 12.20
result = afronden_op_stuiver(12.22)
test('test 1', expected, result)
report()
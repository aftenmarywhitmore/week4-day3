#1. MakeUpperCase -- Time Complexity: O(1)
def make_upper_case(s):
    return s.upper()


#2. BasicMathematicalOperations -- Time Complexity: O(1)
def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2;
    if operator == "-":
        return value1 - value2;
    if operator == "*":
        return value1 * value2;
    if operator == "/":
        return value1 / value2;

#3. InvertValues -- Time Complexity: O(1)
def invert(lst):
    return [x and -x for x in lst]

print(invert([1,2,3,4,5]), [-1,-2,-3,-4,-5])
print(invert([1,-2,3,-4,5]), [-1,2,-3,4,-5])
print(invert([]), [])
print(invert([0]), [0])


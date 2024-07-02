# 덧셈 함수
def add(num1, num2):
    return num1 + num2

# 뺄셈 함수
def subtract(num1, num2):
    return num1 - num2

# 곱셈 함수
def multiply(num1, num2):
    return num1 * num2

# 나눗셈 함수
def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return 0

# 기능 테스트
result_add = add(10,20)
print(result_add)

result_div = divide(2,0)
print(result_div)
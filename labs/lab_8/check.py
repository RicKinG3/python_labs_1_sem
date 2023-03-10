def checker(num):
    while True:
        if num.isdigit(): return num
        num = input("Введите целое положительное число заново: ")

def matrix_check(num):
    if num.isdigit() or (num[0] =='-' and num[1::].isdigit()) or (num[0] =='+' and num[1::].isdigit()):
        return True
    else:
        return False
# if all(map(matrix_check, new)):
        #     new = map(int, new)
# 演習3.11.1 コラッツ数列

def collatz(number):
    if number % 2 == 0:
        return int(number / 2)
    else:
        return 3 * number + 1

print('最初の数を入力してください : ',end='')
number = int(input())

print('----------')

while True:
    number = collatz(number)
    print(number)
    if number == 1:
        break

print('----------')
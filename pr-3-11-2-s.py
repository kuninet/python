# コラッツ数列(入力チェック版)

def collatz(number):
    if number % 2 == 0:
        return int(number / 2)
    else:
        return 3 * number + 1

def proc(number):
	n = collatz(number)
	print(n)
	if n == 1:
		return
	else:
		proc(n)
		
print('最初の数を入力してください : ',end='')

try:
	number = int(input())
except ValueError:
	print('usage : ☆入力値は数字で!')
	exit(1)

print('----------')

proc(number)

print('----------')
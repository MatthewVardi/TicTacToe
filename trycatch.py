# def div42by(divideBy):
# 	try:
# 		return 42 / divideBy
# 	except ZeroDivisionError:
# 		print('Error: you tried to divide by zero!')

# print(div42by(4))
# print(div42by(2))
# print(div42by(0))
# print(div42by(1))

print ('how many cats do you own?')

numCats = input()
try:
	if int(numCats) >= 4:
		print('that is a lot of cats')
	else:
		print('that is not many cats')
except ValueError:
	print('you did not enter a valid integer')


def eggs():
	global spam
	spam = 55 # this would normally be a local var, 
	# however the global statement above tells it t use the global var i declared under
	print(spam)


spam = 45 #global variable

print(spam)
eggs()
#after eggs() it will change spam to 55 instead of 45 
print(spam)



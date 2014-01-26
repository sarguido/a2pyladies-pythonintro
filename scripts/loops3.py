# You should usually declare functions at the beginning of your file
# Simple print function
def printing(item):
	print "The number is", item

x = 5 
y = 10
z = 15

# List of our variables
numbers = [x, y, z]

# For each item in the numbers list, print out
for num in numbers:
	printing(num)

	# If the item is less than 10, print the first condition
	# If the item is greater than 10, print the second condition
	if num < 10:
		print num, "is less than 10"
	elif num > 10:
		print num, "is greater than 10"

# While x is not equal to 0, print out the value of x
# Then subtract one from x and repeat, until x gets to be 0
while x != 0:
	printing(x)
	x = x - 1
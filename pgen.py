import string
import random

s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation

s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))

docu = "generated.txt"

while True:
	try:
		plen = int(input("Enter password length: "))
		if plen  <= 0:
			print("Must be > 0")
			continue
	except ValueError:
		print("Invalid input")
		continue

	
	password = "".join(random.sample(s, plen))
	print("Your password: ", password)

	with open(docu, "a") as file:
		file.write(password + "\n")

	choice = input("Generate another password? (y/n): ").strip().lower()
	if choice != 'y':
		print('Bye!')
		break

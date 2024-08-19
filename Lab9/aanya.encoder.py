def encoder(input):
	before = []
	for i in range (0,len(input)):
		num = int(input[i])
		if num <=6:
			before.append(num)
		else:
			if num == 7:
				new_num = -3
				before.append(new_num)
			elif num == 8:
				new_num = -2
				before.append(new_num)
			elif num == 9:
				new_num = -1
				before.append(new_num)
	updated = [str(x+3) for x in before]
	stored = "" 
	return stored.join(x for x in updated)

def menu():
	print("Menu")
	print("---------")
	print("1. Encode\n2. Decode\n3. Quit")

def main():
	menu()
	while True:
		option = input("Please enter an option: ")
		try:
			option = int(option)
			if option < 0:
				print("Please enter a valid number.")
			else:
				if option == 3:
					break
				elif option == 1:
					key = input("Please enter your password to encode: ")
					encoded_key = encoder(key)
					print("Your password has been encoded and stored!")
				elif option == 2:
					print(f"The encoded password is {encoded_key}, and the original password is {key}")
				else:
					print("Please enter a valid option.")
		
		except ValueError:
			print("Please enter a valid number.")
			continue

if __name__ == "__main__":
	main()


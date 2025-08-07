import random

def play_guessing_game(): 
	""" Plays a number guessing game..."""
	print("--- Number Guessing Game ---")
	print("This game has a number between 0 to 99.")
	print("Can you guess it? Challange..... ")
	print("You have 9 attempts.")

	secret_number = random.randint(0, 99)
	attempt = 0
	max_attempt = 9

	while attempt <max_attempt:
		attempt += 1
		try:
			guess_num = input(f"Attempt {attempt}: Enter your guess: ")
			guess = int(guess_num)

			# check user's guess
			if guess < secret_number:
				print ("Your guess is too low! Try again.")
			elif guess > secret_number:
				print ("Your guess is too high! Try again.")
			else:
				print(f"Congratulations! You guessed the right number. {secret_number}")
				print(f"You can guess {attempt} attempts.")
				break

		except ValueError:
			print("Invalid input. Please, enter only number between 0 to 99.")
		except Exception as e: 
			print(f"An unexpected error occurs: {e}")
			break

	else:
		print("🧨 Game over! You have used all of your 9 attempts.")
		print(f"The correct number was: {secret_number}")
	print("Thanks for playling!")

#main program
if __name__ == "__main__":
	play_guessing_game()

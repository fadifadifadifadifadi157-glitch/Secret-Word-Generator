import random

words = ["python", "coding", "coffee", "rocket", "tiger"]

word = random.choice(words)

print(" Secret Word Challenge")
print("I have chosen a secret word.")
print(" You have 3 attempts to guess it!")

for attempt in range(1, 4):
    guess = input(f"Attempt {attempt}: ").lower().strip()

    if guess == word:
        print(" Correct! You found the secret word!")
        break
    else:
        print(" Wrong guess!")
        print(" Hint: The word starts with", word[0])

else:
    print(" You ran out of attempts!")
    print("The secret word was:", word)


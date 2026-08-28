import random

words = ["python", "coding", "coffee", "rocket", "tiger"]

word = random.choice(words)

print("🔮 Secret Word Challenge")
print("I have chosen a secret word.")

guess = input("Guess the word: ").lower()

if guess == word:
    print("🎉 Correct! You found the secret word!")
else:
    print("❌ Wrong guess!")
    print("The secret word was:", word)

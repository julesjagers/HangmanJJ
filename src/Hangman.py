import random

possible_answers = ["Hond", "Kat", "Papegaai", "Olifant"]

chosen_word = possible_answers[random.randint(0,3)]

fault_count = 0

pending_word = "-" * len(chosen_word)

while True:
    print(pending_word)
    guessed_input = input("Guess a letter or a word: ")

    if len(guessed_input) > 1:
        if guessed_input == chosen_word:
            print("Word is correctly guessed")
            break
        else:
            fault_count += 1
            print("You guessed wrong")
        
    else:
        if guessed_input not in chosen_word:
            fault_count += 1
            print("You guessed wrong")
        else:
            for index in pending_word:
                if pending_word[index] == guessed_input:
                    pending_word[index] = guessed_input
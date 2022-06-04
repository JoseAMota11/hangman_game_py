from random import choice
import re
from os import system

clear = lambda: system("cls")

def user_input(question, answer, res):
  try:
    attempts = 10
    message = ""
    while attempts >= 0:
      if attempts == 0:
        message = f"The word was {answer.upper()}.\n"
        break
      if question == answer.upper():
        message = f"¡Congratulations, you won! The right word is {question}.\n"
        break
      if attempts != 10: print(f"You have {attempts} attempst left.\n")
      print(question)
      user_guess = input("\nType a letter and try to guess the word: ")
      if user_guess.isnumeric():
        raise TypeError
      elif len(user_guess) > 1:
        raise ValueError
      else:
        if user_guess in answer:
          for m in re.finditer(user_guess, answer):
            res[m.start()] = user_guess.upper()
          question = "".join(res)
          print(question)
          attempts -= 1
          clear()
        else:
          attempts -= 1
          clear()
    print(message)
  except TypeError:
    print("You cannot type numbers.")
  except ValueError:
    print("You only can type one letter.")

def game_logic(chosen_word):
  question = re.sub("[a-zá-ú]", "_", chosen_word)
  answer = chosen_word
  res = [i for i in question]
  user_input(question, answer, res)

def random_word(words):
  chosen_word = choice(words)
  game_logic(chosen_word)

def word_generator():
  try:
    words = []
    with open("./data.txt", "r", encoding="utf-8") as f:
      for word in f:
        word = word.replace("\n", "")
        words.append(word)
      random_word(words)
  except ValueError:
    print("There was an error with the 'data.txt' file.")

def start_game():
  print("¡Guess the word!")
  word_generator()

def main():
  start_game()

if __name__ == "__main__":
  main()
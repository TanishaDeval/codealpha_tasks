import random
def hangman(wrong_guess):

    match wrong_guess:
        case 1:
            return  """
    °"""
        case 2:
            return """
    °
    |"""
        case 3:
            return """
     °
    /|"""
        case 4:
            return """
     °
    /|\\"""
        case 5:
            return """
     °
    /|\\
    / """
        case 6:
            return """
    °
   /|\\
   / \\"""
        case _ :
            return " "
def game():
    fruits_list = ["apple", "mango", "banana", "orange", "grapes"]
    fruit = random.choice(fruits_list)
    dashes = ["_"] * len(fruit)

    print(""" HANGMAN GAME
      🍎
    🍌🍇🥭
      🍊
      🍇
    🍌  🥭""")
    print()
    print("Guess the fruit🧠")
    print()
    print("🍎 🥭 🍇  🍌 🍊 ")
    print()
    print("  ".join(dashes))
    print()
    num_wrong_guess = 0
    guessed_letters=[]
    while "_" in dashes and num_wrong_guess<6:
     guess = input("Enter your guess(a-z): ").lower()
     if len(guess)!=1 or not guess.isalpha():
      print("❌Invalid input")
      continue
     if guess in guessed_letters:
      print("Already guessed!🙅")
      continue
     guessed_letters.append(guess)
     if guess in fruit:
       for i in range(len(fruit)):
         if guess == fruit[i]:
          dashes[i]=guess
          print("Correct guess🎊")
          print(f"🧠Wrong guesses:{num_wrong_guess}/6 ")
          print()
          print("Updated word")
          print("  ".join(dashes))
          print()
     else:
          print("Wrong guess❌")
          num_wrong_guess+=1
          print(f"Wrong guesses:{num_wrong_guess}/6 ")
          print(hangman(num_wrong_guess))
          print("Be careful!💀")
          print()
          print(f"Wrong guesses:{num_wrong_guess} ")
    if "_" not in dashes and num_wrong_guess <= 6:
     print("YOU WIN🏆")
    else:
      print("YOU LOSE😞")
      print(f"The fruit  is {fruit}")
def main():
 while True:
    game()
    print()
    while True:
     play = input("Play again? (y/n): ").lower()
     if play  in ["y", "n"]:
        break
     print("Enter only y or n")
    if play == "n":
     print("----The game ended!----")
     break
    if play=="y":
     print("----The game started again!----")

main()















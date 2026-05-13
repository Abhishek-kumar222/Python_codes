import random

def game():
    print("You are paying a game : ")
    score = random.randint(1,100)

    # fetch the high score

    with open("highScore.txt") as f:
      highScore = f.read()
      if(highScore==""):
         highScore=0
      else:
         highScore = int(highScore)
        
    print(f"Your score : {score}")
    if(score>highScore):
       with open("highScore.txt","w") as f:
          f.write(str(score))
    return score
game()
import random
random.seed(0)

class Player():
    round = False

    def __init__(self, turn, name):
        self.name = name
        self.turn = turn
        self.score = 0
        self.round_score = 0

    def rolled(self):
        seed = random.randint(1, 6)
        return seed

    def hold_or_roll(self):
        while self.round != True:

            choose = input(self.name + "'s turn."+ " Your current score is "+str(self.score + self.round_score) +"\n" +"Enter 'r' to roll or 'h' to hold score: ")
            if choose == 'r':
                roll = self.rolled()
                print("You rolled a {}".format(roll))
                if roll == 1 :
                    print(self.name+" turn is over. \n")
                    self.round_score = 0
                    self.turn = False
                    self.round = True
                elif roll >= 2 and roll <= 6:
                    self.round_score += roll
                    print(self.name+" has {} points for this turn so far".format(self.round_score))
                if self.score + self.round_score >= 100:
                    self.score += self.round_score
                    print(self.name+" has won the Game!")
                    self.round = True
                    self.turn = False

            elif choose == 'h':
                self.score += self.round_score
                print(self.score)
                self.round_score = 0
                print(self.name + " has a TOTAL SCORE of {}.".format(self.score)+"\n")
                self.turn = False
                self.round = True


def main():
    player1 = Player(True, "Player 1")
    player2 = Player(False, "Player 2")
    gameOver = False
    while gameOver == False:
      if player1.turn == True:
        player1.hold_or_roll()
        # print("******")
        # print(player1.turn)
        if player1.score >= 100:
          gameOver = True
        player2.turn = True
        player1.round = False
      else:
        player2.hold_or_roll()
        if player2.score >= 100:
          gameOver = True
        player1.turn = True
        player2.round = False


if __name__ == "__main__":
    main()

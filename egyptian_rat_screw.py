import random, statistics

DEBUG = False
def printf(msg):
    if DEBUG: print(msg, end="")

CARDS = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

class Player:
    def __init__(self, name, slapChance):
        self.name = name
        self.chance = slapChance
        self.deck = []
    
    def slap(self, stack):
        slapped = random.random() < self.chance
        if slapped:
            printf(f"{self.name} slapped deck and took: {', '.join(stack)}\n")
            self.deck.extend(stack)
            stack.clear()
        return slapped
    
    def take(self, stack):
        self.deck.extend(stack)
        stack.clear()

    def play(self, stack):
        if self.deck:
            card = self.deck.pop(0)
            printf(f"{self.name} played {card}\n")
            stack.append(card)
            return True
        else:
            printf(f"{self.name} has no cards to play\n")
            return False

class Game:
    def __init__(self, players):
        self.stack = CARDS * 4
        self.players = players
        random.shuffle(self.stack)
        self.count = len(players)
        self.turn = 0
        self.won = False

        for i in range(len(self.stack)):
            self.players[i % self.count].take([self.stack.pop(0)])
        
        for i in self.players:
            printf(f"{i.name} starts with deck {str(i.deck)}\n")
    
    def checkWin(self, player):
        if len(player.deck) == 52:
            print(f"{player.name} won on turn {self.turn}")
            self.won = True
    
    def checkSlap(self):
        canSlap = False
        if len(self.stack) > 2 and self.stack[-1] == self.stack[-2]: canSlap = True 
        if len(self.stack) > 3 and self.stack[-1] == self.stack[-3]: canSlap = True
        if canSlap: 
            printf("Card can slap. ")
            for i in self.players:
                printf(f"Checking {i.name}; ")
                if i.slap(self.stack):
                    self.checkWin(i)
                    return True 
    
    def play(self):
        royals = {"J": 1, "Q": 2, "K": 3, "A": 4}
        while True:
            if self.won: return self.turn
            self.turn += 1
            printf(f"Turn {self.turn}: ")
            self.players[self.turn % self.count].play(self.stack)
            self.checkSlap()



def main():
    chances = (.10, .20, .30, .40, .50, .60)
    players = [Player("Player " + str(i), chances[i]) for i in range(len(chances))]

    plays = []
    for i in range(100):
        plays.append(Game(players).play())
    print(f"Total turns taken for each game: {str(plays)}\nAverage: {statistics.mean(plays)};",
        f"Max: {sorted(plays)[-1]}; Min: {sorted(plays)[0]}")

main()
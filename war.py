import random

def warGame():
    nums = [i for i in range(1, 14)]
    cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    arr = {}
    for j in range(len(cards)): arr[cards[j]] = nums[j]

    deck = cards * 4
    random.shuffle(deck)

    p1 = deck[:26]
    n1 = 26
    p2 = deck[26:]
    n2 = 26

    turn = 0
    #print("Player 1 deck:", p1, "\nPlayer 2 deck:", p2)

    while True:
        if len(p1) == 0 or len(p2) == 0: break
        turn += 1
     #   print("Turn", turn, end=": ")
        c1 = p1.pop(0)
      #  print("P1 played", c1, end="; ")
        c2 = p2.pop(0)
       # print("P2 played", c2, end="; ")
        v1 = arr[c1]
        v2 = arr[c2]
        if v1 > v2:
          #  print("P1 wins trade")        
            p1.extend([c1, c2])
        elif v1 < v2:
         #   print("P2 wins trade")
            p2.extend([c1, c2])
        else:
            try:
                a1 = [c1] + [p1.pop(0) for i in range(4)]
                a2 = [c2] + [p2.pop(0) for i in range(4)]
            except:
             #   print("Deck has run out of cards at tiebreaker.")
                break
            v1 = arr[a1[4]]
            v2 = arr[a2[4]]
            if v1 > v2:
            #    print("P1 wins trade")        
                p1.extend(a2)
            elif v1 < v2:
           #     print("P2 wins trade")
                p2.extend(a1)
        if n1 == 0:
            random.shuffle(p1)
           # print("P1 shuffled his deck to", p1)
            n1 = len(p1)
        if n2 == 0:
            random.shuffle(p2)
            #print("P2 shuffled his deck to", p2)
            n2 = len(p2)
        n1 -= 1
        n2 -= 1

#    if len(p1) == 0: print("\nPlayer 2 wins!")
 #   else: print("\nPlayer 1 wins!")
    return turn

turns = []
for i in range(100):
    turns.append(warGame())

print("All games played: ", turns)
turns.sort()
print("Sorted by highest: ", turns[::-1])

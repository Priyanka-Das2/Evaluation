import random


def Monty(choice, monty_stall=[1,0,0]):
    x = 1 - monty_stall[choice]
    return x
    

my_stall = [1,0,0]
NUM_SIMS = 100000000

wins = 0.00
for i in range(NUM_SIMS):
    choice = random.randint(0,2)
    success = Monty(choice)
    wins = wins + success

p = wins/NUM_SIMS
print('iterations',  NUM_SIMS, 'wins ', wins, ' prob of winning', p)


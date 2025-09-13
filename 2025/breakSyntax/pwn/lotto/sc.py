import random
S = 0x31313131
random.seed(S)
wins = [random.randint(1,49) for _ in range(6)]
print("Winning numbers are: ", wins)
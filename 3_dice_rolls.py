from random import randint

# This script simulated the results of rolling 3 dices that contains 00, 11, and 22
# simulation done due to some boardgame containing this mechanic

# {'Total 0': 73945, 'Total 1': 222370, 'Total 2': 443533, 'Total 3': 518986, 
#  'Total 4': 445166, 'Total 5': 222338, 'Total 6': 73662}

#  {'Total 0': '3.7%', 'Total 1': '11.1%', 'Total 2': '22.2%', 'Total 3': '25.9%', 
#  'Total 4': '22.3%', 'Total 5': '11.1%', 'Total 6': '3.7%'}  


dice_choice = [0, 0, 1, 1 , 2, 2]

simulation = 2000000
distribution = {
    f"Total {i}": 0 for i in range(7)
}

def roll_die() -> int:
    total = 0
    for _ in range(3):
        total += dice_choice[randint(0, 5)]
    return total

for _ in range(simulation):
    distribution[f"Total {roll_die()}"] += 1

print(distribution)

distribution_percentage = {k: f"{v/simulation*100:.1f}%" for k, v in distribution.items()}
print("\n", distribution_percentage)
"""
CP1404/CP5632 Practical
Code for quick pick program
"""
import random
MIN=1
MAX=45

def main():
    """Generate quick pick numbers"""
    num_of_quick_pick = int(input("How many quick pick? "))
    for i in range(0, num_of_quick_pick):
        quick_pick_numbers = []
        for j in range(0, 6):
            random_pick = random.randint(MIN, MAX)
            while random_pick in quick_pick_numbers:
                random_pick = random.randint(MIN, MAX)
            quick_pick_numbers.append(random_pick)
        quick_pick_numbers.sort()

        for j in quick_pick_numbers:
            print("{:<5d}".format(j), end="")
        print()

main()
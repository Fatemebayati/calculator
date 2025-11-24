import random
import os

def num_dice():
    while True:
        try:
            num_dice=input("number of dise:")
            valid_responses=['1','one','2','two']
            if num_dice not in valid_responses:
                raise ValueError('1 or 2 only')
            else:
                return num_dice
        except ValueError as err:
            print("erorr")

def roll_dice():
    min_val=1
    max_val=6
    roll_again='y'
    while roll_again.lower=="yes" or roll_again.lower=="y":
        os.system('cls' if os.name=='nt' else 'clear')
        amount=num_dice()
        if amount=='2' or amount=="two":
            print("rolling the dise...")
            dice_1=random.randint(min_val,max_val)
            dice_2=random.randint(min_val,max_val)
            print("dice one:",dice_1)
            print("dice two:",dice_2)
            roll_again=input("roll again[y or yes]?")
        else:
            print("rolling the dise...")
            dice_1=random.randint(min_val,max_val)
            print(f"the value is:{dice_1}")
            roll_again=input("roll again[y or yes]?")
    
if __name__ == '__main__':
    roll_dice()
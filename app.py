from random import randint

    
#Set Variables
def main_game():
    repeat = "y"
    points = 0
    one_count = 0
    two_count = 0
    three_count = 0
    four_count = 0
    five_count = 0
    six_count = 0
    

    while repeat.lower() == "y":
        # Creates Dice
        dice = [randint(1,6),randint(1,6),randint(1,6),randint(1,6),randint(1,6)]
        
        for die in dice:
            # Normal Points
            if die == 1:
                points += 100
            if die == 5:
                points += 50
                
            # Bonus Points
            if die == 1:
                one_count += 1
                if one_count == 3:
                    points += 1100 - 300 # Subtracts 300 from Normal Points
            if die == 2:
                two_count += 1
                if two_count == 3:
                    points += 200
            if die == 3:
                three_count += 1
                if three_count == 3:
                    points += 300
            if die == 4:
                four_count += 1
                if four_count == 3:
                    points += 400
            if die == 5:
                five_count += 1
                if five_count == 3:
                    points += 500 - 150 # Subtracts 150 from Normal Points
            if die == 6:
                six_count += 1
                if six_count == 3:
                    points += 600
                
        print(dice)          
        print(points)
        
        # Resets Counts
        one_count = 0
        two_count = 0
        three_count = 0
        four_count = 0
        five_count = 0
        six_count = 0
        
        # End or Continue Game
        if points >= 5000:
            print("Congrats you got to 5000!!")
            break
        else:
            repeat = input("Press Y To Roll Again or Q to Quit: ")

main_game()

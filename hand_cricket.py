import time
import random

score = 0
total = 0


class Hand_Cricket_Game:
    def __init__(self):
        pass

    @staticmethod
    def welcome():
        print("************ Welcome to hand cricket game ************")

    def user_bat(self):
        global score, total
        print("You are batting now .......and computer is bowling")
        user_batting_number_for_game = int(input("Enter Your batting shot number ( 1 to 10 ) "))
        computer_bowling_number_for_game = random.randint(0, 11)
        print("You choose : ", user_batting_number_for_game, "\n", "Computer bowl : ", computer_bowling_number_for_game)
        if user_batting_number_for_game != computer_bowling_number_for_game:
            score += user_batting_number_for_game
            print("Score : ", score)
            self.user_bat()
        else:
            total += score
            print("Both number are matching .....")
            print("You lose the wicket")
            print("Score = ", score)
        time.sleep(4)
        score = 0
        print("The Total score is ", total)
        print("Now Its Time to Computer to bat")
        while score <= total:
            computer_batting_number = random.randint(0, 10)
            user_bowling_number = int(input("Enter the bowling number "))
            print("Computer choose : ", computer_batting_number, "\n", "You bowl : ", user_bowling_number)
            if user_bowling_number != computer_batting_number:
                score += computer_batting_number
                print("Score = ", score)
                print("Target = ", total)
            else:
                print("Both are matching")
                print("You win")
                self.again()
        if score > total:
            print("You loose ... computer achieve your target")
            self.again()

    def computer_bat(self):
        global score, total
        print("computer is batting now .......and you are bowling")
        user_bowl_number_for_game = int(input("Enter Your bowling  number ( 1 to 10 ) "))
        computer_batting_number_for_game = random.randint(0, 10)
        print("computer  choose : ", computer_batting_number_for_game, "\n", "you bowl : ", user_bowl_number_for_game)
        if user_bowl_number_for_game != computer_batting_number_for_game:
            score += computer_batting_number_for_game
            print("Score : ", score)
            self.computer_bat()
        else:
            total += score
            print("Both number are matching .....")
            print("Computer loss the wicket")
            print("Score = ", score)
        time.sleep(4)
        score = 0
        print("The Total score is ", total)
        print("Now Its Time to you to bat")
        if score == total:
            print("draw")
            self.again()
        while score < total:
            computer_bowling_number = random.randint(0, 10)
            user_batting_number = int(input("Enter the batting shot number"))
            print("You choose: ", user_batting_number, "\n", "Computer bowl : ", computer_bowling_number)
            if user_batting_number != computer_bowling_number:
                score += user_batting_number
                print("Score :-", score)
                print("Target = ", total)
            else:
                print("Both are matching")
                print("You loss the wicket")
                print("Your score = ", score)
                self.again()
                break
        if score > total:
            print("You win ... you achieve the target")
            self.again()

    def toss(self):
        print(
            "First we play the Toss . If You win ,You can choose bat or bowling . "
            "If computer win ,computer can choose bat or Bowling")
        print("Select ODD or EVEN (type odd or even)")
        user_choice_toss = str(input().lower())
        print("Put Your Number (1 to 10 only)")
        computer_choice_toss_number = random.randint(0, 10)
        user_choice_toss_number = int(input())
        toss_result = user_choice_toss_number + computer_choice_toss_number
        print("Toss result : ", toss_result)
        print("*" * 10)
        if user_choice_toss == 'even':
            if toss_result % 2 == 0:
                print("You have won the toss")
                user_bat_or_bowl = input("What do u want?(bat/bowl)").lower()
                if user_bat_or_bowl == 'bat':
                    self.user_bat()
                elif user_bat_or_bowl == 'bowl':
                    self.computer_bat()
                else:
                    print("Invalid Input.The game will restart")
                    self.toss()
            else:
                computer_choice_toss = random.choice(['bat', 'bowl'])
                if computer_choice_toss == 'bat':
                    print('The computer choose to bat')
                    self.computer_bat()
                elif computer_choice_toss == 'bowl':
                    print('Computer choose to bowl')
                    self.user_bat()
        if user_choice_toss == 'odd':
            if toss_result % 2 != 0:
                print("You have won the toss")
                user_bat_or_bowl = input("What do u want?(bat/bowl) ").lower()
                if user_bat_or_bowl == 'bat':
                    self.user_bat()
                elif user_bat_or_bowl == 'bowl':
                    self.computer_bat()
                else:
                    print("Invalid Input.The game will restart")
                    self.toss()
            else:
                computer_choice_toss = random.choice(['bat', 'bowl'])
                if computer_choice_toss == 'bat':
                    print('The computer choose to bat ')
                    self.computer_bat()
                elif computer_choice_toss == 'bowl':
                    print('Computer choose to bowl')
                    self.user_bat()

    def again(self):
        print("Still you want to play the game (yes or no)")
        again_playing = input()
        if again_playing == 'yes':
            self.toss()
        elif again_playing == 'no':
            print("Thank you for playing the game")
            exit()


game = Hand_Cricket_Game()
game.welcome()
game.toss()
game.again()
import time
import random

score = 0
total = 0


class Hand_Cricket_Game:
    def __init__(self):
        pass

    @staticmethod
    def welcome():
        print("************ Welcome to hand cricket game ************")

    def user_bat(self):
        global score, total
        print("You are batting now .......and computer is bowling")
        user_batting_number_for_game = int(input("Enter Your batting shot number ( 1 to 10 ) "))
        computer_bowling_number_for_game = random.randint(0, 11)
        print("You choose : ", user_batting_number_for_game, "\n", "Computer bowl : ", computer_bowling_number_for_game)
        if user_batting_number_for_game != computer_bowling_number_for_game:
            score += user_batting_number_for_game
            print("Score : ", score)
            self.user_bat()
        else:
            total += score
            print("Both number are matching .....")
            print("You lose the wicket")
            print("Score = ", score)
        time.sleep(4)
        score = 0
        print("The Total score is ", total)
        print("Now Its Time to Computer to bat")
        while score <= total:
            computer_batting_number = random.randint(0, 10)
            user_bowling_number = int(input("Enter the bowling number "))
            print("Computer choose : ", computer_batting_number, "\n", "You bowl : ", user_bowling_number)
            if user_bowling_number != computer_batting_number:
                score += computer_batting_number
                print("Score = ", score)
                print("Target = ", total)
            else:
                print("Both are matching")
                print("You win")
                self.again()
        if score > total:
            print("You loose ... computer achieve your target")
            self.again()

    def computer_bat(self):
        global score, total
        print("computer is batting now .......and you are bowling")
        user_bowl_number_for_game = int(input("Enter Your bowling  number ( 1 to 10 ) "))
        computer_batting_number_for_game = random.randint(0, 10)
        print("computer  choose : ", computer_batting_number_for_game, "\n", "you bowl : ", user_bowl_number_for_game)
        if user_bowl_number_for_game != computer_batting_number_for_game:
            score += computer_batting_number_for_game
            print("Score : ", score)
            self.computer_bat()
        else:
            total += score
            print("Both number are matching .....")
            print("Computer loss the wicket")
            print("Score = ", score)
        time.sleep(4)
        score = 0
        print("The Total score is ", total)
        print("Now Its Time to you to bat")
        if score == total:
            print("draw")
            self.again()
        while score < total:
            computer_bowling_number = random.randint(0, 10)
            user_batting_number = int(input("Enter the batting shot number"))
            print("You choose: ", user_batting_number, "\n", "Computer bowl : ", computer_bowling_number)
            if user_batting_number != computer_bowling_number:
                score += user_batting_number
                print("Score :-", score)
                print("Target = ", total)
            else:
                print("Both are matching")
                print("You loss the wicket")
                print("Your score = ", score)
                self.again()
                break
        if score > total:
            print("You win ... you achieve the target")
            self.again()

    def toss(self):
        print(
            "First we play the Toss . If You win ,You can choose bat or bowling . "
            "If computer win ,computer can choose bat or Bowling")
        print("Select ODD or EVEN (type odd or even)")
        user_choice_toss = str(input().lower())
        print("Put Your Number (1 to 10 only)")
        computer_choice_toss_number = random.randint(0, 10)
        user_choice_toss_number = int(input())
        toss_result = user_choice_toss_number + computer_choice_toss_number
        print("Toss result : ", toss_result)
        print("*" * 10)
        if user_choice_toss == 'even':
            if toss_result % 2 == 0:
                print("You have won the toss")
                user_bat_or_bowl = input("What do u want?(bat/bowl)").lower()
                if user_bat_or_bowl == 'bat':
                    self.user_bat()
                elif user_bat_or_bowl == 'bowl':
                    self.computer_bat()
                else:
                    print("Invalid Input.The game will restart")
                    self.toss()
            else:
                computer_choice_toss = random.choice(['bat', 'bowl'])
                if computer_choice_toss == 'bat':
                    print('The computer choose to bat')
                    self.computer_bat()
                elif computer_choice_toss == 'bowl':
                    print('Computer choose to bowl')
                    self.user_bat()
        if user_choice_toss == 'odd':
            if toss_result % 2 != 0:
                print("You have won the toss")
                user_bat_or_bowl = input("What do u want?(bat/bowl) ").lower()
                if user_bat_or_bowl == 'bat':
                    self.user_bat()
                elif user_bat_or_bowl == 'bowl':
                    self.computer_bat()
                else:
                    print("Invalid Input.The game will restart")
                    self.toss()
            else:
                computer_choice_toss = random.choice(['bat', 'bowl'])
                if computer_choice_toss == 'bat':
                    print('The computer choose to bat ')
                    self.computer_bat()
                elif computer_choice_toss == 'bowl':
                    print('Computer choose to bowl')
                    self.user_bat()

    def again(self):
        print("Still you want to play the game (yes or no)")
        again_playing = input()
        if again_playing == 'yes':
            self.toss()
        elif again_playing == 'no':
            print("Thank you for playing the game")
            exit()


game = Hand_Cricket_Game()
game.welcome()
game.toss()
game.again()

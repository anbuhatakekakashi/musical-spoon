'''
SCOREBOARD DESIGN IDEA

    TEAM 1 - 90 pts

SGT Andrews:    20 pts
SPC Bradley:    30 pts
SGT Christian:  40 pts

    TEAM 2 - 110 pts

SGT Davis:      50 pts
SSG Eckland:    50 pts
SSG Forehand:   10 pts

    -- or --


TEAM 1 - 90 pts
TEAM 2 - 110 pts
TEAM 3 - 150 pts
'''

#  This is a dictionary consisting of question numbers as keys, and their associated hashes as values

known_hashes = {1: "AAAAAAAAAAAAAAAAAAAA",
                2: "BBBBBBBBBBBBBBBBBBBB",
                3: "CCCCCCCCCCCCCCCCCCCC"}

class Scoreboard:
    '''
    scoreboard = {1: "Team 1",
                  2: "Team 2",
                  3: "Team 3",
                  4: "Team 4",
                  5: "Team 5",
                  6: "Team 6",
                  7: "Team 7",
                  8: "Team 8"}
    '''
    scoreboard = {"Team 1": 0,
                  "Team 2": 0,
                  "Team 3": 0,
                  "Team 4": 0,
                  "Team 5": 0,
                  "Team 6": 0,
                  "Team 7": 0,
                  "Team 8": 0}

class Team:
    team_number = ""
    points = ""

    def numberOfTeams(number):
        team_num = input("Enter number of teams in competition: ")
        # for each number in team_num, create scoreboard with that team
        # for iter in team_num:

        Scoreboard.scoreboard["Team 1"] += 5

def hash_checker(question, hash):

    # Check if hash is between 20 and 30 characters
    if (len(hash) < 20):
        raise Exception("String is too small")
    elif (len(hash) > 30):
        raise Exception("String is too large")

    if (known_hashes[question] == hash):
        print("CORRECT!")
        # send success message back to user
        # update scoreboard
        # write to disk
    else:
        print("WRONG!")
        # notify user they got the message wrong



def display_menu():
    print("\n")
    print("1.  Display scoreboard")
    print("99. Exit")

def display_scoreboard():
    pass

def main():
    valid = True
    while (valid):
        # display_scoreboard()
        display_menu()
        choice = input("Enter option: ")
        if(choice == "1"):
            pass
        elif(choice == "2"):
            pass
        elif(choice == "3"):
            pass
        elif(choice == "99"):
            valid = False
        else:
            print("ERROR:  Please choose a valid option\n")

if __name__ == '__main__':
    main()
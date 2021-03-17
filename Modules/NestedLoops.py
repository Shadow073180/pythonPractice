

#Given a tic-tac-toe board of 3x3, print every position
def output_ever_position_of_a_3_by_3_tic_tac_toe_board():
    rows = [1,2,3]
    columns = [1,2,3]

    for row in rows:
        for column in columns:
            print(row,column)

#Create a program where every person meets the other persons
def player_matchup(players):
    for player in players:
        for person in players:
            if person != player:
                print(player + ":" + person)


#If a normal for loop finishes in n steps O(n), how many steps has a nested loop?
def answer_steps_taken():
    print("O(n)^2")
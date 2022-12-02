#These static variables represent the static scores you get from selecting Rock, Paper, or Scissors
#or from getting a win, loss or draw
ROCK_SCORE = 1
PAPER_SCORE = 2
SCISSORS_SCORE = 3
WIN_SCORE = 6
DRAW_SCORE = 3
LOSS_SCORE = 0
#These dictionaries are static and are simply referenced to translate input to proper outputs
ENCRYPTION = {'A': 'Rock', 'B': 'Paper', 'C':'Scissors', 'X' : 'Rock', 'Y': 'Paper', 'Z':'Scissors'}
PICK_SCORE = { 'Rock' : ROCK_SCORE, 'Paper':PAPER_SCORE,'Scissors':SCISSORS_SCORE}
MATCH_RESULT = { 'X': LOSS_SCORE, 'Y':DRAW_SCORE,'Z':WIN_SCORE}
WIN_DICT = {'A':PAPER_SCORE, 'B':SCISSORS_SCORE,'C':ROCK_SCORE}
LOSS_DICT = {'A': SCISSORS_SCORE, 'B': ROCK_SCORE, 'C': PAPER_SCORE}

#function imports data from the input.txt file and stores it in the strategyGuide variable
def import_data(strategyGuide):
    with open('input.txt', 'r') as f:
        content = f.readlines()
        for matchup in content:
            strategyGuide.append(matchup)
        return strategyGuide

#helper function to determine the winner of a game of RPS; never never directly called, referenced by later functions
def calculate_winner(villain, hero):
    if (villain == 'Paper' and hero == 'Rock') or (villain == 'Scissors' and hero == 'Paper') or (villain == 'Rock' and hero == 'Scissors'):
        return LOSS_SCORE
    elif (villain == 'Paper' and hero == 'Scissors') or (villain == 'Scissors' and hero == 'Rock') or (villain == 'Rock' and hero == 'Paper'):
        return WIN_SCORE
    else:
        return DRAW_SCORE

#function used in part 1 to determine the score; iterates over the strategyGuide list, calls the calculate_winner function,
#then adds the outcome to total_score
def calculate_total(strategyGuide):
    total_score = 0
    for matchup in strategyGuide:
        total_score += calculate_winner(ENCRYPTION[matchup[0]], ENCRYPTION[matchup[2]])
        total_score += PICK_SCORE[ENCRYPTION[matchup[2]]]
    return total_score

#function used to calculate the second solution; again iterates over the strategyGuide list and calls the calculate_winner function,
#but evaluates whether the outcome should be a win, loss or draw, and acting accordingly
def calculate_total_second(strategyGuide):
    total_score = 0
    for matchup in strategyGuide:
        if matchup[2] == 'X':
            total_score+= LOSS_SCORE
            total_score+= LOSS_DICT[matchup[0]]
        elif matchup[2] == 'Y':
            total_score += DRAW_SCORE
            total_score += PICK_SCORE[ENCRYPTION[matchup[0]]]
        elif matchup[2] == 'Z':
            total_score += WIN_SCORE
            total_score += WIN_DICT[matchup[0]]
    return total_score

if __name__ == '__main__':

    strategyGuide = []
    import_data(strategyGuide)
    #print(f'Your expected total score is {calculate_total(strategyGuide)}')
    print(f'If you follow the elves instructions EXACTLY, your score should be {calculate_total_second(strategyGuide)}')

ROCK_SCORE = 1
PAPER_SCORE = 2
SCISSORS_SCORE = 3
WIN_SCORE = 6
DRAW_SCORE = 3
LOSS_SCORE = 0
ENCRYPTION = {'A': 'Rock', 'B': 'Paper', 'C':'Scissors', 'X' : 'Rock', 'Y': 'Paper', 'Z':'Scissors'}
PICK_SCORE = { 'Rock' : ROCK_SCORE, 'Paper':PAPER_SCORE,'Scissors':SCISSORS_SCORE}

def import_data(strategyGuide):
    with open('input.txt', 'r') as f:
        content = f.readlines()
        for matchup in content:
            strategyGuide.append(matchup)
        return strategyGuide

def calculate_winner(villain, hero):
    if (villain == 'Paper' and hero == 'Rock') or (villain == 'Scissors' and hero == 'Paper') or (villain == 'Rock' and hero == 'Scissors'):
        return LOSS_SCORE
    elif (villain == 'Paper' and hero == 'Scissors') or (villain == 'Scissors' and hero == 'Rock') or (villain == 'Rock' and hero == 'Paper'):
        return WIN_SCORE
    else:
        return DRAW_SCORE

def calculate_total(strategyGuide):
    total_score = 0
    for matchup in strategyGuide:
        total_score += calculate_winner(ENCRYPTION[matchup[0]], ENCRYPTION[matchup[2]])
        total_score += PICK_SCORE[ENCRYPTION[matchup[2]]]
    return total_score

def test_run(strategyGuide):
    for matchup in strategyGuide:
        print(f'Opponent is picking {ENCRYPTION[matchup[0]]}, you are picking {ENCRYPTION[matchup[2]]}')


if __name__ == '__main__':
    strategyGuide = []
    import_data(strategyGuide)
    #test_run(strategyGuide)
    print(f'Your expected total score is {calculate_total(strategyGuide)}')

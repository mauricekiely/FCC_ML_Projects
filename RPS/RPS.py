from collections import Counter 
# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
  if prev_play:
    opponent_history.append(prev_play)
  else:
    opponent_history.clear()

  winning_play = {'R': 'P', 'P': 'S', 'S': 'R'}
  
  guess = "R"

  if len(opponent_history) > 3:
    potential_moves = [
      ''.join(opponent_history[-3:] + [move]) for move in ['S', 'R', 'P']
    ]

    past_moves = Counter([
      ''.join(opponent_history[i:i + 4]) for i in range(len(opponent_history) - 3)
    ])
      
    opponent_guess = max(potential_moves, key=lambda seq: past_moves.get(seq, 0))[-1]
    guess= winning_play[opponent_guess]

  return guess

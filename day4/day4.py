in_file = open('input.txt', 'r')

draw_list = list(map(int,in_file.readline().strip().split(',')))
in_file.readline()


bingo_cards = []
new_card = []
new_row = []

for line in in_file.readlines():
  if line == '\n':
    bingo_cards.append(new_card)
    new_card = []
  else:
    for num in line.strip().split():
      new_row.append({'value': int(num), 'marked': False})
    new_card.append(new_row)
    new_row = []

bingo_cards.append(new_card)

in_file.close()




def mark_number(board, num):
  marked_spot = []
  for row_ind, row in enumerate(board):
    for col_ind, spot in enumerate(row):
      if spot['value'] == num:
        spot['marked'] = True
        marked_spot = [row_ind, col_ind]

  return marked_spot

  

def check_winner(board, added_row, added_col):
  good_row = True

  for spot in board[added_row]:
    if spot['marked'] == False:
      good_row = False
  
  if good_row:
    return True

  good_col = True
  for spot in [board[i][added_col] for i in range(5)]:
    if spot['marked'] == False:
      good_col = False
  if good_col: 
    return True

  return False


def score_board(board):
  total = 0
  for row in board:
    for spot in row:
      if spot['marked'] == False:
        total += spot['value']
  return total



def play_game(board_list):
  num_winners = 0
  winners = []
  num_boards = len(board_list)
  for draw in draw_list:
    for board_ind, board in enumerate(board_list):
      marked_spot = mark_number(board, draw)
      if len(marked_spot) > 0 and check_winner(board, marked_spot[0], marked_spot[1]) and board_ind not in winners:
        num_winners += 1
        winners.append(board_ind)
        if num_winners == num_boards:
          return draw * score_board(board)

print(play_game(bingo_cards))
      

import sys, csv

def startup(file):
  with open(file, newline='') as input:
    board = []
    wires = csv.reader(input)
    for wire in wires:
      board.append(read_wire(wire))
    print(nearest_intersect(board))

def read_wire(wire):
  curr = [0,0]
  board = []
  for path in wire:
    dir = path[0]
    dist = int(path[1:])
    if dir == "U":
      for i in range(1, dist + 1):
        curr[0] += 1
        board.append(tuple(curr))
    elif dir == "D":
      for i in range(1, dist + 1):
        curr[0] -= 1
        board.append(tuple(curr))
    elif dir == "L":
      for i in range(1, dist + 1):
        curr[1] -= 1
        board.append(tuple(curr))
    elif dir == "R":
      for i in range(1, dist + 1):
        curr[1] += 1
        board.append(tuple(curr))
  return board

def nearest_intersect(board):
  intersect = set(board[0]) & set(board[1])
  steps = []
  for pt in intersect:
    wireAStep = 0
    wireBStep = 0
    for (i, step) in enumerate(board[0]):
      if step == pt:
        wireAStep = i + 1
    for (i, step) in enumerate(board[1]):
      if step == pt:
        wireBStep = i + 1
    steps.append(wireAStep + wireBStep)
  return min(steps)

if __name__ == '__main__':
  startup(sys.argv[1])
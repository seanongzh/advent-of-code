import sys, csv

def startup(file):
  with open(file, newline='') as program:
    original = next(csv.reader(program))
    for noun in range(0, 99):
      for verb in range(0, 99):
        progList = original.copy()
        progList[1] = noun
        progList[2] = verb
        # For each noun-verb combination in adds 1 and 2... run the program
        for i, op in enumerate(progList):
          # Instructions are four integers long
          if i % 4 == 0:
            if int(op) == 1:
              # Some clunky typecasting here...
              # Can I default CSV values to integers?
              progList[int(progList[i+3])] = int(progList[int(progList[i+1])]) + int(progList[int(progList[i+2])])
            elif int(op) == 2:
              progList[int(progList[i+3])] = int(progList[int(progList[i+1])]) * int(progList[int(progList[i+2])])
            elif int(op) == 99:
              break
        if int(progList[0]) == 19690720:
          with open("output", mode='w') as output:
            final = csv.writer(output)
            final.writerow(progList)

if __name__ == '__main__':
  startup(sys.argv[1])
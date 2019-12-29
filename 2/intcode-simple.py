import sys, csv

def startup(file):
  with open(file, newline='') as program:
    progList = next(csv.reader(program))
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
  with open("output", mode='w') as output:
    final = csv.writer(output)
    final.writerow(progList)

if __name__ == '__main__':
  startup(sys.argv[1])
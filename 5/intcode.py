import sys, csv

def startup(ifile):
  with open(ifile) as input:
    progInitStr = next(csv.reader(input))
    progInit = [ (int(x)) for x in progInitStr ]
    progHalt = read(progInit)
    
  with open("output", mode = "w") as ofile:
    output = csv.writer(ofile)
    output.writerow(progHalt)

def read(program):
  i = 0
  while i > -1:
      inst = program[i]
      # instruction ABCDE: DE is two-digit opcode
      opcode = inst % 100

      # Parse parameter modes (ABC in instruction ABCDE)
      # 0 is position (variable), 1 is immediate (literal)
      fstMode = (inst // 100) % 10
      sndMode = (inst // 1000) % 10
      trdMode = inst // 10000

      # Math instructions, 3 parameters
      if opcode == 1 or opcode == 2 or opcode == 7 or opcode == 8:
        if fstMode == 0:
          fst = program[program[i+1]]
        elif fstMode == 1:
          fst = program[i+1]
        if sndMode == 0:
          snd = program[program[i+2]]
        elif sndMode == 1:
          snd = program[i+2]
        if trdMode == 0:            # Can never be in immediate mode
          trd = program[i+3]
        if opcode == 1:             # Opcode 1 (addition)
          program[trd] = fst + snd
        elif opcode == 2:           # Opcode 2 (multiplication)
          program[trd] = fst * snd
        elif opcode == 7:           # Opcode 7 (less than)
          if fst < snd:
            program[trd] = 1
          else:
            program[trd] = 0
        elif opcode == 8:           # Opcode 8 (equals)
          if fst == snd:
            program[trd] = 1
          else:
            program[trd] = 0
        i += 4
      
      # I/O instructions, 1 parameter
      elif opcode == 3 or opcode == 4: 
        param = program[i+1]
        if opcode == 3:                             # Opcode 3 (Input)
          program[param] = int(input("Input: "))
        else:                                       # Opcode 4 (Output)
          if fstMode == 0:
            print(program[param])
          elif fstMode == 1:
            print(param)
        i += 2
      
      # Conditionals, 2 parameters
      elif opcode == 5 or opcode == 6:
        if fstMode == 0:
          fst = program[program[i+1]]
        elif fstMode == 1:
          fst = program[i+1]
        if sndMode == 0:
          snd = program[program[i+2]]
        elif sndMode == 1:
          snd = program[i+2]
        # Opcode 5 (jump if true) and Opcode 6 (jump if false)
        if (opcode == 5 and fst != 0) or (opcode == 6 and fst == 0):
          i = snd
        else:
          i += 3

      # Halt instruction, no parameters
      elif opcode == 99:
        break
      
  return program


if __name__ == '__main__':
  startup(sys.argv[1])
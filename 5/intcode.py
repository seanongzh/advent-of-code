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
      # Arithmetic instructions, 3 parameters
      if opcode == 1 or opcode == 2:
        
        # Parse parameter modes (ABC in instruction ABCDE)
        fstMode = (inst // 100) % 10
        sndMode = (inst // 1000) % 10
        trdMode = inst // 10000

        # 0 is position mode, 1 is immediate mode
        if fstMode == 0:
          fst = program[program[i+1]]
        elif fstMode == 1:
          fst = program[i+1]
        if sndMode == 0:
          snd = program[program[i+2]]
        elif sndMode == 1:
          snd = program[i+2]
        if trdMode == 0:        # Can never be in immediate mode
          trd = program[i+3]

        if opcode == 1:             # Opcode 1 (addition)
          program[trd] = fst + snd
        else:                       # Opcode 2 (multiplication)
          program[trd] = fst * snd

        i += 4
      
      # Opcode 3
      # Input instruction, 1 parameter, no modes
      elif opcode == 3: 
        param = program[i+1]
        program[param] = int(input("Input: "))
        i += 2
      
      # Opcode 4
      # Output instruction, 1 parameter
      elif opcode == 4:
        paramMode = (inst // 100) % 10
        param = program[i+1]
        if paramMode == 0:
          print(program[param])
        elif paramMode == 1:
          print(param)
        i += 2

      # Halt instruction, no parameters
      elif opcode == 99:
        break
      
  return program


if __name__ == '__main__':
  startup(sys.argv[1])
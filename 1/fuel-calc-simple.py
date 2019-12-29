import sys

def startup(file):
  masses = open(file)
  totalFuel = 0
  for module in masses:
    totalFuel = totalFuel + fuel_calc(int(module)) # Cast input to integer
  print(totalFuel)
  masses.close()

def fuel_calc(mass):
  mass = mass // 3 # floor division
  mass = mass - 2
  return mass

if __name__ == '__main__':
  startup(sys.argv[1])
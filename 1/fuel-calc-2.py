import sys

def startup(file):
  masses = open(file)
  totalFuel = 0
  for module in masses:
    totalFuel += fuel_calc(int(module)) # Cast input to integer
  print(totalFuel)
  masses.close()

def fuel_calc(module):
  totalFuel = 0
  moduleFuel = module // 3 # floor division
  moduleFuel = moduleFuel - 2
  totalFuel += moduleFuel 
  currentFuel = moduleFuel
  # Fuel for module is calculated... now that fuel also needs fuel!
  fuelForCurrFuel = 0
  while currentFuel > 0:
    totalFuel += fuelForCurrFuel
    fuelForCurrFuel = (currentFuel // 3) - 2
    currentFuel = fuelForCurrFuel
  return totalFuel
    

if __name__ == '__main__':
  startup(sys.argv[1])
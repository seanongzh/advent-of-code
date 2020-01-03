import sys

def startup(start, end):
  count = 0
  for i in range(start, end+1):
    if is_pwd(i):
      count += 1
  print(count)

def is_pwd(num):
  return no_decreasing_digits(num) and has_only_two_same_digits(num)

def no_decreasing_digits(num):
  num = str(num)
  for i in range(0, len(num) - 1):
    if int(num[i]) > int(num[i+1]):
      return False
  return True

def has_two_same_digits(num):
  num = str(num)
  for i in range(0, len(num) - 1):
    if num[i] == num[i+1]:
      return True
  return False

def has_only_two_same_digits(num):
  if has_two_same_digits(num):
    num = str(num)
    prevEql = False
    chk = False
    count = 0
    for i in range(0, len(num) - 1):
      if num[i] == num[i+1]:
        if prevEql:
          if chk:
            count -= 1
            chk = False
        else:
          prevEql = True
          chk = True
          count += 1
      else:
        prevEql = False
    if count > 0:
      return True
    else:
      return False
  else:
    return False

if __name__ == '__main__':
  startup(int(sys.argv[1]), int(sys.argv[2]))
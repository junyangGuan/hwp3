def digit_sum(n):
  if n//10 > 0 :
    return   digit_sum(n//10) + n%10
  else :
    return  n%10
  
def run():
  cj = input("Enter an int: ")
  cj = int(cj)
  print(f"sum of digits of {cj} is {digit_sum(cj)}.")
if __name__  == "__main__":
  run()
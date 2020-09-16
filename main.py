def digit_sum(n):
  a = n%10
  b = n//10%10
  c = n//100%100
  d = n//1000%1000
  e = n//10000%10000
  f = n//100000%100000
  g = n//1000000%1000000
  h = n//10000000%10000000
  i = n//100000000%100000000
  j = n//1000000000
  sum = a+b+c+d+e+f+g+h+i+j
  a=int(a)
  b=int(b)
  c=int(c)
  d=int(d)
  e=int(e)
  f=int(f)
  g=int(g)
  h=int(h)
  i=int(i)
  j=int(j)
  sum=int(sum)
  return sum
def run():
  cj = input("Enter an int: ")
  cj = int(cj)
  print(f"sum of digits of {cj} is {digit_sum(cj)}.")
if __name__ =="__main__":
  run()
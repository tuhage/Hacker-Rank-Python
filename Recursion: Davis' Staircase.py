import math

def stepPerms(n):
  sum=0
  for i in range(0, n):
     for j in range(0, n):
         if(i*2+j*3<=n):
             sum += (math.factorial((n - (2*i + 3*j)) + i+j) / (math.factorial(n - (2*i + 3*j)) * math.factorial(i)*math.factorial(j)))



  return sum

print(stepPerms(1000))


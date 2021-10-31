while True:
  b=input().split()
  X,M=b
  X=int(X)
  M=int(M)
  if(X==0 and M==0):
      break
  else:
      E=X*M
      print(E)
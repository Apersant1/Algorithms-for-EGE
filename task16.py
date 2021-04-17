def F(n):
  if n > 0:
    F(n − 1)
    print(n)
    F(n − 2)
F(4) # 1231412

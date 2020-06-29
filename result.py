def foo(a,b,c):
  return b**2-4*a*c

def kor(a,b,c):
  x1=(-b+foo(a,b,c)**0.5)/2*a
  x2=(-b-foo(a,b,c)**0.5)/2*a
  return x1,x2

try:
  assert kor(1,18,32) == (-2.0,-16.0)
except AssertionError:
  print("Корни неверны, правильно:",kor(1,18,32))
try:
  assert kor(1,18,32) == (-2.0,-10.0)
except AssertionError:
  print("Корни неверны, правильно:",kor(1,18,32))
try:
  assert kor(1,2,1) == (-2.0,-16.0)
except AssertionError:
  print("Корни неверны, правильно:",kor(1,2,1))
try:
  assert kor(1,2,1) == (-2.0,-16.0)
except AssertionError:
  print("Корни неверны, правильно:",kor(1,2,1))
  
##print(kor(1,18,32))

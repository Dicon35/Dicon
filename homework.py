import kem as kem


try:
 result = []
 def drivider(a, b):
  if a < b:
   raise ValueError
  if b > 100:
   raise IndexError
  return a/b

 data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}

 for key in data:
  res = drivider(key, data[kem])
  result.append(res)

 print(result)

except (ZeroDivisionError, NameError) as error:
 print(error)

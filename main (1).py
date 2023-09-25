def leepyear(year):
  if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    return True
  else:
    return False
year=int(input("Enter the year:"))
if leepyear(year):
  print("{}is a leep year".format(year))
else:
  print("{}is not a leep year". format(year))
try:
    print(x)
except NameError:
    print('x is not defined idiot')

try:
  f = open("emails/excptn/etc/hosts", "w+")
  f.write("Success!")
except FileNotFoundError:
  print("Data file not found")
except Exception as ex:
  print("Error appending to file: " + str(ex))
else:
  f.close()
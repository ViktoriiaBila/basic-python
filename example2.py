def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)
x = raw_input('input x : ')
y = raw_input('input y : ')
summ = x + y
print (summ)

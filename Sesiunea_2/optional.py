# 3.1. Put "monty" at the right with a space of 70 in front of
def right_justify(s):
  word = len(s)
  column = 70
  space = column - word
  return s.rjust(space)


# print(right_justify('monty'))

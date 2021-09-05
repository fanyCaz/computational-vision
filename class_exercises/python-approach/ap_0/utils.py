import json

def save_matrix(name: str, dictionary):
  with open(name,'w') as json_file:
    json.dump(dictionary,json_file, indent=2)

"""
Optional: extra_constraint can receive an array of two elements,
the minimum value and the maximum value like: [0,2]
"""
def input_normalized(question: str, extra_constraint=None):
  res = input(question)
  try:
    if int(res) < 1:
      print('Ingresa un número positivo')
      return input_normalized(question)
    else:
      if extra_constraint:
        if int(res) < extra_constraint[0] or int(res) > extra_constraint[1]:
          print(f"Ingresa un número entre {extra_constraint[0]} y {extra_constraint[1]}")
          return input_normalized(question, extra_constraint)
      return int(res)
  except:
    print('Ingresa un número entero, porfavor')
    return input_normalized(question)
  return res

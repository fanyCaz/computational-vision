import json

def save_matrix(name: str, dictionary):
  with open(name,'w') as json_file:
    json.dump(dictionary,json_file, indent=2)

def print_matrix(name: str, matrix):
  f = open(name, 'w')
  for i,row in enumerate(matrix):
    f.write(str(i) + '\n')
    for pixel in row:
      f.write(str(pixel) + ' - ')
    f.write("\n")
  f.close()

"""
Optional: extra_constraint can receive an array of two elements,
the minimum value and the maximum value like: [0,2]
"""
def input_normalized(question: str, extra_constraint=None):
  res = input(question)
  try:
    if float(res) < 0:
      print('Ingresa un número positivo')
      return input_normalized(question)
    else:
      if extra_constraint:
        if float(res) < extra_constraint[0] or float(res) > extra_constraint[1]:
          print(f"Ingresa un número entre {extra_constraint[0]} y {extra_constraint[1]}")
          return input_normalized(question, extra_constraint)
      return float(res)
  except:
    print('Ingresa un número , porfavor')
    return input_normalized(question)
  return res

import json

def save_matrix(name: str, dictionary):
  with open(name,'w') as json_file:
    json.dump(dictionary,json_file, indent=2)

def input_normalized(question: str):
  res = input(question)
  try:
    if int(res) < 1:
      print('Ingresa un número positivo')
      return input_normalized()
    else:
      return int(res)
  except:
    print('Ingresa un número entero, porfavor')
    return input_normalized()
  return res

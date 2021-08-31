import json

def save_matrix(name: str, dictionary):
  with open(name,'w') as json_file:
    json.dump(dictionary,json_file, indent=2)

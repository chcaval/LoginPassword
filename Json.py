import json

data = {'Nome':'Carlos', 'idade':45, 'RG':456, 'CPF':123456789}
data_string = json.dumps(data)
print(data_string)

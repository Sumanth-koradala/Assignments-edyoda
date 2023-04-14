# ASSIGNMENT 1



import json

with open("C:\AMD\Sublime Text\employee_det.json") as f:

	data = json.load(f)

for i in data["emp_details"]:
	print([i])
f.close()





import json

dict_obj = {
	"Andhra pradesh" : "Vishakapatnam" ,
	"Telangana" : "Hyderabad" ,
	"Karnataka"  : "Bangalore" ,
	"Tamil nadu" : "Chennai" ,
	"Maharashtra" : "Mumbai"
}


with open("tellme.json", "w") as outfile:
    json.dump(dict_obj, outfile)

f = open("tellme.json")
data = json.load(f)
print(data)






























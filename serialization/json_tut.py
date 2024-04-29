import json

people = [
  {
    "name": "Sabrina Green",
    "username": "sgreen",
    "phone": {
      "office": "802-867-5309",
      "cell": "802-867-5310"
    },
    "department": "IT Infrastructure",
    "role": "Systems Administrator"
  },
  {
    "name": "Eli Jones",
    "username": "ejones",
    "phone": {
      "office": "684-348-1127"
    },
    "department": "IT Infrastructure",
    "role": "IT Specialist"
  }
]

#store data in a json file
with open('serialization/people.json', 'w') as people_json:
    json.dump(people, people_json, indent=2)

#to print data into a string
pipol_json = json.dumps(people)
# print(pipol_json)

print('-----------------------------------------------------------------------------------')

#load() method does the opposite of dump() method
with open('serialization/people.json', 'r') as people_reader:
    reading = json.load(people_reader)
# print(reading)


"""
Use of the Faker library
https://pypi.org/project/Faker/
"""
import json
from faker import Faker

fake = Faker()
people = []
for i in range(100):
    dic = {
           'suffix': fake.suffix(),
           'name': fake.name(),
           'address': fake.address(),
           'country': fake.country(),
           'job': fake.job(),
           'company': fake.company(),
           'email': fake.email(),
          }
    people.append(dic)

with open('people.json', 'w', encoding='utf8') as file:
    json.dump(people, file, indent=4)

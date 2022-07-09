"""
Use of the Faker library
https://pypi.org/project/Faker/
"""
import json
from faker import Faker

fake = Faker()
dic = {}
for _ in range(10):
    name = fake.prefix() + fake.name()
    address = fake.address()
    position = fake.job()
    company = fake.company()
    phone = fake.phone_number()

    dic.update({f'Person {_+1}':
                {'name': name,
                 'address': address,
                 'phone': phone,
                 'position': position,
                 'company': company,
                 }
                })

with open('profiles.json', 'w', encoding='utf-8') as f:
    json.dump(dic, f, indent=4)

for k, v in dic.items():
    print(f'{k}: {v}')
    print('\n')

for i in fake.profile().keys():
    print(i)

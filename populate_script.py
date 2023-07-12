import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

import random

from faker import Faker
from validate_docbr import CPF

from clients.models import Client


def creating_people(quantity_of_people):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantity_of_people):
        cpf = CPF()
        name = fake.name()
        email = '{}@{}'.format(name.lower(),fake.free_email_domain())
        email = email.replace(' ', '')
        cpf = cpf.generate()
        rg = "{}{}{}{}".format(random.randrange(10, 99),random.randrange(100, 999),random.randrange(100, 999),random.randrange(0, 9) ) 
        cellphone = "{} 9{}-{}".format(random.randrange(10, 21), random.randrange(4000, 9999), random.randrange(4000, 9999))
        active = random.choice([True, False])
        p = Client(name = name, email = email, cpf = cpf, rg = rg, cellphone = cellphone, active = active)
        p.save()

creating_people(50)
print("success!")
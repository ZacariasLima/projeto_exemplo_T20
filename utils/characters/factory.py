# from inspect import signature
from random import randint

from faker import Faker

def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt_BR')
# print(signature(fake.random_number))


def make_character():
    return {
        'id' : fake.random_number(digits=2, fix_len=True),
        'name': fake.sentence(nb_words=1),
        'race': fake.sentence(nb_words=1),
        'class': fake.sentence(nb_words=1),
        'spells': fake.random_number(digits=2, fix_len=True),
        'spells_unit': 'Magias Divinas',
        'skills': fake.random_number(digits=2, fix_len=True),
        'skills_unit': 'Perícias',
        'introduction': fake.sentence(nb_words=12),
        'background': fake.text(3000),
        'created_at': fake.date_time(),
        'function' : fake.sentence(nb_words=1),
        'player': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'cover': {
            'url': 'https://picsum.photos/%s/%s ' % rand_ratio(),
        }
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(make_character())
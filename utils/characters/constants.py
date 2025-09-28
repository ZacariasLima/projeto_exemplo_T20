#Constants File

#Character Attributes
def str():
    return 0

def dex():
    return 1

def con():
    return 2

def int():
    return 3

def wis():
    return 4

def char():
    return 5

#Fixed Choices
SIZES_CHOICES = [
        ("TN", "Minúsculo"),
        ("SM", "Pequeno"),
        ("MD", "Médio"),
        ("LG", "Grande"),
        ("HG", "Enorme"),
        ("GG", "Colossal"),
    ]

ROLES_CHOICES = [
        ("TNK", "Defensor"),
        ("HLR", "Curador"),
        ("MDG", "Dano Corpo a Corpo"),
        ("RDG", "Dano Longo Alcance"),
        ("SPT", "Suporte"),
        ("CST", "Conjurador"),
        ("SPC", "Especialista"),
    ]
import re
from django.core import exceptions


def validate_personal_names(value):
    pattern = r'[A-Z][a-z]+'
    if not re.match(pattern, value):
        raise exceptions.ValidationError('Name must start with upper letter and finish with lower one!')


def validate_location(value):
    pattern = r'[A-Za-z0-9,\. ]+'
    if not re.match(pattern, value):
        raise exceptions.ValidationError('Wrong location! Don`t include symbols like !@#$')


def validate_phone(value):
    pattern = '0[0-9]{9}'
    if not re.match(pattern, value):
        raise exceptions.ValidationError('Wrong phone number! Start with 0')

# def validate_username(value):
#     if value[0].isnumeric():
#         raise exceptions.ValidationError('Username cannot start with number!')
#     for ch in value:
#         if not ch.isalnum() or ch.isupper():
#             raise exceptions.ValidationError('Username must contain lower letters and numbers only!')

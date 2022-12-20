from enum import Enum
from project_1.core.my_mixins import ChoicesEnumMixin


class Genders(ChoicesEnumMixin, Enum):
    male = 'Male'
    female = 'Female'


# class Conditions(ChoicesEnumMixin, Enum):
#     used = 'used'
#     new = 'new'
#
#
# class Categories(ChoicesEnumMixin, Enum):
#     animals = 'Animals'
#     real_estate = 'Real Estate'
#     babies = 'Babies'
#     house_garden = 'House and garden'
#     vehicles = 'Vehicles'
#     electronics = 'Electronics'
#     appearance = 'Appearance'
#     others = 'Others'
#
#         # subcategory to appearance
#         #     clothes
#         #
#         #     shoes

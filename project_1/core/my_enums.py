from enum import Enum
from project_1.core.my_mixins import ChoicesEnumMixin


class Genders(ChoicesEnumMixin, Enum):
    male = 'Male'
    female = 'Female'

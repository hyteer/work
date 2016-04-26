# -*- coding: utf-8 -*-
import string
import random

g = lambda a, b : "".join(random.sample(string.letters, a)) + "".join(random.sample(string.digits, b))

print(g(5,9))
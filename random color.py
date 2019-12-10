import random

r = lambda: random.randint(0,255)

color = ('#%02X%02X%02X' % (r(),r(),r()))

print(color)
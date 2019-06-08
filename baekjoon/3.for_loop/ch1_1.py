import math
from collections import defaultdict
from collections import namedtuple

print(type(2))
print(type('hello'))
print(type(False))
print(type('a'))
print(type([1]))

a7tr = "hi"
print(a7tr * 3)
print(int('32'))
print(float('32'))

# module: file tht contains a collection of related functions

print(math.sin(2))


def print_lyrics():
    print("hello")
    print("lyrics")


print_lyrics()

print(isinstance('a', bool))

g = (x**2 for x in range(5))
for val in g:
    print(val)

print(sum(x**2 for x in range(5)))
print(any([True, False, False]))
print(all([True, False, False]))

myword = 'triangulation'
myforbidden = 'ta'


def avoid(word, forbidden):
    return not any(letter in forbidden for letter in word)

print(avoid(myword, myforbidden))


d = defaultdict(list)
t = d['new key']
print(t)

Point = namedtuple('Point', ['x', 'y', 'z'])
p = Point(1, 2, 3)
print(p.x)


class Pointier(Point):
    def hey(self):
        print('hey')
        print(self.x)


p2 = Pointier(2, 4, 6)
p2.hey()

animals = ['cat', 'dog', 'rabbit', 'cow', 'tiger']
fruits = ['apple', 'banana', 'orange']

for animal in animals:
    print(animal)

for fruit in fruits:
    print(fruit)
# O(A + F)

for animal in animals:
    for fruit in fruits:
        print(f'{animal} loves {fruit}')
# O(A * F)

num = 0
while num < len(animals):
    for fruit in fruits:
        print(fruit)
    for animal in animals:
        print(animal)
    num += 1

# O((F + A) * A) = > O(FA + A**2)

def counter(n):
    print(n)
    if n > 0:
        counter(n - 1)

counter(3)
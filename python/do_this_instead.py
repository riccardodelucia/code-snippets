####################################################
# =============#
# DON'T
for i in [0, 1, 2, 3, 3, 5]:
    print(i**2)

# =============#
# INSTEAD DO
# already lazy evaluation in python 3
for i in range(6):
    print(i**2)

####################################################
colors = ["red", "green", "blue", "yellow"]
# =============#
# DON'T
for i in range(len(colors)):
    print(colors[i])

# =============#
# INSTEAD DO
for color in colors:
    print(color)

####################################################
# =============#
# DON'T
for i in range(len(colors) - 1, -1, -1):
    print(colors[i])

# =============#
# INSTEAD DO
for color in reversed(colors):
    print(color)

####################################################
# =============#
# DON'T
for i in range(len(colors)):
    print(i, "-->", colors[i])

# =============#
# INSTEAD DO
for i, color in enumerate(colors):
    print(i, "-->", color)

####################################################
names = ["raymond", "rachel", "matthew"]
colors = ["red", "green", "blue", "yellow"]

# =============#
# DON'T
n = min(len(names), len(colors))
for i in range(n):
    print(names[i], "-->", colors[i])

# =============#
# INSTEAD DO
# implemented as old python 2 izip
for name, color in zip(names, colors):
    print(name, "-->", color)


####################################################
# never use compare functions over key functions.
# key functions are created to give a numerical size for each element within an array
# =============#
# DON'T
def compare_length(c1, c2):
    if len(c1) < len(c2):
        return -1
    if len(c1) > len(c2):
        return 1
    return 0


print(sorted(colors, cmp=compare_length))

# =============#
# INSTEAD DO
# key is a function, can be a lambda function
print(sorted(colors, key=len))

####################################################
# =============#
# DON'T
blocks = []
while True:
    block = f.read(32)
    if block == "":
        break
    blocks.append(block)

# =============#
# INSTEAD DO
# iter returns an iterator over the given object
# the second element is a sentinel to escape the iteration
# partial is like bind in JS. It fixes the second argument and
# provides a new function with one less parameter (i.e. a f.read that reads)
# exactly 32 B per block. The function now does need any parameter
for block in iter(partial(f.read, 32), ""):
    blocks.append(block)

####################################################


####################################################
# =============#
# DON'T
def find(seq, target):
    found = False
    for i, value in enumerate(seq):
        if value == target:
            found = True
            break
    if not found:
        return -1
    return i


# =============#
# INSTEAD DO
def find(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        return -1
    return i


####################################################
d = {"mathew": "blue", "rachel": "green", "raymond": "red"}
# =============#
# DON'T

for k in d:
    print(k)

# =============#
# INSTEAD DO
for k in d.keys():
    print(k)

for k in d.items():
    # Python 2 used to have iteritems,
    # that doesn't exist anymore in Python 3
    print(k)

####################################################
# DO THIS
keys = ["a", "b", "c"]
values = [1, 2, 3]
dictionary = dict(zip(keys, values))
print(dictionary)  # {'a': 1, 'b': 2, 'c': 3}


####################################################
colors = ["red", "green", "red", "blue", "green", "red"]
d = {}

# =============#
# DON'T
for color in colors:
    if color not in d:
        d[color] = 0
    d[color] += 1

d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1

# =============#
# INSTEAD DO
from collections import defaultdict

d = defaultdict(int)
for color in colors:
    d[color] += 1

####################################################
names = [
    "raymond",
    "rachel",
    "matthew",
    "roger",
    "betty",
    "melissa",
    "judith",
    "charlie",
]

# Goal: group all names with same length in one dict key, where
# the key is an int expressing the word length:
# {5: ['roger', 'betty'], 6: ['rachel', 'judith'], 7: ['raymond', 'matthew', 'melissa', 'charlie']}
d = {}

# =============#
# DON'T
for name in names:
    key = len(name)
    if key not in d:
        d[key] = []
    d[key].append(name)

# =============#
# INSTEAD DO
d = defaultdict(list)
for name in names:
    key = len(name)
    d[key].append(name)

####################################################
# Unpacking sequences: similar as JS

p = "Raymond", "Hettinger", 0x30, "python@example.com"

# =============#
# DON'T
fname = p[0]
lname = p[1]
age = p[2]
email = p[3]

# =============#
# INSTEAD DO
fname, lname, age, email = p

####################################################


# =============#
# DON'T
def fibonacci(n):
    x = 0
    y = 1
    for i in range(n):
        print(x)
        t = y
        y = x + y
        x = t


# =============#
# INSTEAD DO
def fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        print(x)
        x, y = y, x + y


####################################################
# =============#
# DON'T
tmp_x = x + dx * t
tmp_y = y + dy * t
tmp_dx = influence(m, x, y, dx, dy, partial="x")
tmp_dy = influence(m, x, y, dx, dy, partial="y")
x = tmp_x
y = tmp_y
dx = tmp_dx
dy = tmp_dy

# =============#
# INSTEAD DO
x, y, dx, dy = (
    x + dx * t,
    y + dy * t,
    influence(m, x, y, dx, dy, partial="x"),
    influence(m, x, y, dx, dy, partial="y"),
)

####################################################
names = [
    "raymond",
    "rachel",
    "matthew",
    "roger",
    "betty",
    "melissa",
    "judith",
    "charlie",
]
# =============#
# DON'T
# quadratic cost
s = names[0]
for name in names[1:]:
    s += ", " + name
print(s)

# =============#
# INSTEAD DO
print(", ".join(names))

####################################################
# Efficient list operations
names = [
    "raymond",
    "rachel",
    "matthew",
    "roger",
    "betty",
    "melissa",
    "judith",
    "charlie",
]

# =============#
# DON'T
del names[0]
names.pop(0)
names.insert(0, "mark")

# =============#
# INSTEAD DO
from collections import deque

# this collection is much faster in append and pop ops on top and end of the queue
names = deque(
    ["raymond", "rachel", "matthew", "roger", "betty", "melissa", "judith", "charlie"]
)

del names[0]
names.popleft()
names.appendleft("mark")

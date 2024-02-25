import math

def find_roots(a, b, c):
    disc = b**2 - 4*a*c

    if a == 0:
      if b == 0:
        if c == 0:
          return []
        root = c
        return [root]
      root = -c/b
      return [root]
    elif disc > 0:
        root1 = (-b + math.sqrt(disc)) / (2*a)
        root2 = (-b - math.sqrt(disc)) / (2*a)
        return sorted([root1, root2])
    elif disc == 0:
        root = -b / (2*a)
        return [root]
    else:
        return []
# Random module in Python, which is used to generate pseudo-random numbers for various probabilistic distructions

# 1. seed() -> This initializes a random number generator.
# 2. getstate() -> This returns an object containing the current state of the generator.
# 3. setstate(state_obj) -> This restores the state of the generator at the point when "getstate()" was called, by passing the state object.
# 4. getrandbits(k) -> Return a python integer with "k" random bits.

import random
 
number_genrator = random.uniform(0, 1)
if number_genrator > 0.5:
    print("Head")
else:
    print("Tail")
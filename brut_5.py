import random
from brut_4 import action


for actions in action:
    actions["indicateur de risque"] = random.randint(1, 3)

print(action)

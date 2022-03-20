# NO TOUCHING ======================================

from random import choice, randint

# randomly assigns values to these four variables
actually_sick = choice([True, False])
kinda_sick = choice([True, False])
hate_your_job = choice([True, False])
sick_days = randint(0, 10)

if (actually_sick and sick_days) or (kinda_sick and sick_days):
	calling_in_sick = True
else:
	calling_in_sick = False

print(calling_in_sick)
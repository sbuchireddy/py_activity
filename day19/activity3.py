import random

def secret_santa(participants):
    valid = False
    while not valid:
        receivers = participants[:]
        random.shuffle(receivers)
        valid = all(giver != receiver for giver, receiver in zip(participants, receivers))
    return dict(zip(participants, receivers))

participants = ["Michael", "Jim", "Pam", "Dwight", "Angela"]
pairings = secret_santa(participants)

for giver, receiver in pairings.items():
    print(f"{giver} : {receiver}")

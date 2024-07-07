class Child:
    def __init__(self):
        self.next_child = None


round_dance = []

for i in range(6):
    child = Child()
    round_dance.append(child)

for i in round_dance:
    if not i == round_dance[len(round_dance) - 1]:
        i.next_child = round_dance[round_dance.index(i) + 1]
    else:
        i.next_child = round_dance[0]

#
print(round_dance)
print(round_dance[5].next_child)

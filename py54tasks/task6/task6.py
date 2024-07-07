class Child:
    def __init__(self):
        self.next_child = None
        self.prev_child = None

    def take_my_hand(self, child):
        self.next_child = child
        child.prev_child = self


child1 = Child()
child2 = Child()
child3 = Child()
child4 = Child()
child5 = Child()
child6 = Child()

round_dance = [child1, child2, child3, child4, child5, child6]

for i in round_dance:
    if not i == round_dance[-1]:
        i.take_my_hand(round_dance[round_dance.index(i) + 1])
    else:
        i.take_my_hand(round_dance[0])

for i in round_dance:
    print(i.prev_child, i.next_child)

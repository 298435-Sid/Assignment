list_a = list(map(int, input("Enter elements of Set A : ").split()))
list_b = list(map(int, input("Enter elements of Set B : ").split()))

set_a = set(list_a)
set_b = set(list_b)

if set_a.issubset(set_b):
    print("Set A is a subset of Set B.")
elif set_a.issuperset(set_b):
    print("Set A is a superset of Set B.")
elif set_a.isdisjoint(set_b):
    print("Set A and Set B are disjoint.")
else:
    print("Set A and Set B partially overlap.")
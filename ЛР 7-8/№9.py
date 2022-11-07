a_1 = input()
a_2 = input()
razn = len(a_1) - len(a_2)
if len(a_1) > len(a_2):
    print(a_1 * razn)
else:
    print(a_2 * razn)
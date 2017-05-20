def tower_builder(n_floors):
    tower = []
    basefloor = '*' * (((n_floors - 1) * 2) + 1)
    tower.append(basefloor)
    floor = 0
    while floor <= n_floors:
        print(floor, n_floors)
        floor += 1
        built_floor = floor * ' ' + basefloor[floor:-floor] + floor * ' '
        tower.append(built_floor)
    print(tower)
    return tower


def tower_builder(n_floors):
    return [floor * ' ' + (str('*' * (((n_floors-1) * 2) + 1))[floor:-floor] or str('*' * (((n_floors-1) * 2) + 1)))+ floor * ' ' for floor in range(n_floors)]

print(tower_builder(6), tower_builder(1))
from collections import namedtuple

Query = namedtuple('Query', ('y', 'x'))
ALIVE = '*'
EMPTY = '-'


def count_neighbors(y, x):
    n_ = yield Query(y + 1, x + 0)  # North
    ne = yield Query(y + 1, x + 1)  # Northeast
    # Define e_, se, s_, sw, w_, nw ...
    # ...
    neighbor_states = [n_, ne, e_, se, s_, sw, w_, nw]
    count = 0
    for state in neighbor_states:
        if state == ALIVE:
            count += 1
    return count


it = count_neighbors(10, 5)
q1 = next(it)  # Get the first query
print('First yield: ', q1)
q2 = it.send(ALIVE)  # Send q1 state, get q2
print('Second yield:', q2)
q3 = it.send(ALIVE)  # Send q2 state, get q3
# ...
try:
    count = it.send(EMPTY)  # Send q8 state, retrieve count
except StopIteration as e:
    print('Count: ', e.value)  # Value from return statement

# First yield:  Query(y=11, x=5)
# Second yield: Query(y=11, x=6)
# ...
# Count:  2

Transition = namedtuple('Transition', ('y', 'x', 'state'))


def game_logic(state, neighbors):
    # ...
    pass


def step_cell(y, x):
    state = yield Query(y, x)
    neighbors = yield from count_neighbors(y, x)
    next_state = game_logic(state, neighbors)
    yield Transition(y, x, next_state)


def game_logic(state, neighbors):
    if state == ALIVE:
        if neighbors < 2:
            return EMPTY  # Die: Too few
        elif neighbors > 3:
            return EMPTY  # Die: Too many
    else:
        if neighbors == 3:
            return ALIVE  # Regenerate
    return state


it = step_cell(10, 5)
q0 = next(it)  # Initial location query
print('Me:      ', q0)
q1 = it.send(ALIVE)  # Send my status, get neighbor query
print('Q1:      ', q1)
# ...
t1 = it.send(EMPTY)  # Send for q8, get game decision
print('Outcome: ', t1)

'''
Me:       Query(y=10, x=5)
Q1:       Query(y=11, x=5)
...
Outcome:  Transition(y=10, x=5, state='-')
'''

TICK = object()


def simulate(height, width):
    while True:
        for y in range(height):
            for x in range(width):
                yield from step_cell(y, x)
        yield TICK


class Grid(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.rows = []
        for _ in range(self.height):
            self.rows.append([EMPTY] * self.width)

    def __str__(self):
        pass
        # ...


def query(self, y, x):
    return self.rows[y % self.height][x % self.width]


def assign(self, y, x, state):
    self.rows[y % self.height][x % self.width] = state


def live_a_generation(grid, sim):
    progeny = Grid(grid.height, grid.width)
    item = next(sim)
    while item is not TICK:
        if isinstance(item, Query):
            state = grid.query(item.y, item.x)
            item = sim.send(state)
        else:  # Must be a Transition
            progeny.assign(item.y, item.x, item.state)
            item = next(sim)
    return progeny


grid = Grid(5, 9)
grid.assign(0, 3, ALIVE)
# ...
print(grid)


# ---*-----
# ----*----
# --***----
# ---------
# ---------
#
class ColumnPrinter(object):
    # ...
    pass


columns = ColumnPrinter()
sim = simulate(grid.height, grid.width)
for i in range(5):
    columns.append(str(grid))
    grid = live_a_generation(grid, sim)

print(columns)

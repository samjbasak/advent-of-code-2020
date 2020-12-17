class GameOf4DLife:
    def __init__(self, file_name):
        with open(file_name) as f:
            input_data = f.read().split('\n')
            self.active = set()
            for countx, x in enumerate(input_data):
                for county, y in enumerate(x):
                    if y == '#':
                        self.active.add((countx,county,0,0))

    def possible_neighbours(self, cell):
        poss_neighbours = [(cell[0]+x-1, cell[1]+y-1, cell[2]+z-1, cell[3]+w-1)
                              for x in range(3)
                              for y in range(3)
                              for z in range(3)
                              for w in range(3)
                              ]
        poss_neighbours.remove(cell)
        return poss_neighbours
    
    def count_neighbours(self, cell): 
        return sum([1
                   for i in self.possible_neighbours(cell)
                   if i in self.active
                   ])

    def cells_in_world_to_check(self):
        cells_to_check = []
        for cell in self.active:
            cells_to_check.extend(self.possible_neighbours(cell))
        return cells_to_check

    def cell_iteration(self, cell):
        neighbour_count = self.count_neighbours(cell)
        if cell in self.active:
            return 2 <= neighbour_count <= 3
        else:
            return neighbour_count == 3

    def iterate_world(self):
        new_active = set()
        cells_to_check = self.cells_in_world_to_check()
        for cell in cells_to_check:
            #print(cell)
            #print(self.cell_iteration(cell))
            if self.cell_iteration(cell):
                new_active.add(cell)
        self.active = new_active

gol = GameOf4DLife('day17.txt')

print(gol.active)
for i in range(6):
    gol.iterate_world()
    print(len(gol.active))



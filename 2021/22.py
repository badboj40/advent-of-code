from copy import deepcopy

class Cuboid:
    def __init__(self, is_on, x0, x1, y0, y1, z0, z1):
        self.is_on = is_on
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1
        self.z0 = z0
        self.z1 = z1
        self.inside = not(self.x1 < -50 or self.x0 > 50 or \
                          self.y1 < -50 or self.y0 > 50 or \
                          self.z1 < -50 or self.z0 > 50)
        size = (1 + self.x1 - self.x0) * (1 + self.y1 - self.y0) * (1 + self.z1 - self.z0)
        self.size = size if self.is_on else -size

    def get_overlap(self, cuboid):
        x0 = max(self.x0, cuboid.x0)
        x1 = min(self.x1, cuboid.x1)
        y0 = max(self.y0, cuboid.y0)
        y1 = min(self.y1, cuboid.y1)
        z0 = max(self.z0, cuboid.z0)
        z1 = min(self.z1, cuboid.z1)
        if x0 > x1 or y0 > y1 or z0 > z1:
            return None
        else:
            is_on = not self.is_on # Because of inclusion/exclusion
            return Cuboid(is_on, x0, x1, y0, y1, z0, z1)

    def __eq__(self, other):
        return self.x0 == other.x0 and self.x1 == other.x1 and \
               self.y0 == other.y0 and self.y1 == other.y1 and \
               self.z0 == other.z0 and self.z1 == other.z1

    def __str__(self):
        return f"state: {self.is_on}, size: {self.size} x: ({self.x0}, {self.x1}), y: ({self.y0}, {self.y1}), z: ({self.z0}, {self.z1}), inside: {self.inside}"


def parse_indata(indata):
    cuboids = []
    for line in indata:
        state, coords = line.split()
        is_on = True if state == 'on' else False
        x_str, y_str, z_str = coords.split(',')
        x0, x1 = [int(x) for x in x_str[2:].split('..')]
        y0, y1 = [int(y) for y in y_str[2:].split('..')]
        z0, z1 = [int(z) for z in z_str[2:].split('..')]
        cuboid = Cuboid(is_on, x0, x1, y0, y1, z0, z1)
        cuboids.append(cuboid)
    return cuboids


def part1(cuboids):
    init_cuboids = [cuboid for cuboid in cuboids if cuboid.inside]
    lit_cubes = set()
    for cuboid in init_cuboids:
        for x in range(cuboid.x0, cuboid.x1+1):
            for y in range(cuboid.y0, cuboid.y1+1):
                for z in range(cuboid.z0, cuboid.z1+1):
                    cube = (x, y, z)
                    if cuboid.is_on:
                        lit_cubes.add(cube)
                    else:
                        lit_cubes.discard(cube)
    return len(lit_cubes)


def part2(cuboids):
    previous_cuboids = []
    for cuboid in cuboids:
        new = []
        if cuboid.is_on:
            new.append(cuboid)
        for prev in previous_cuboids:
            overlap = prev.get_overlap(cuboid)
            if overlap is not None:
                new.append(overlap)
        previous_cuboids.extend(new)
    lit_cubes = 0
    for cuboid in previous_cuboids:
        lit_cubes += cuboid.size
    return lit_cubes


if __name__ == "__main__":
    with open("input/22", "r") as f:
        indata = f.read().split('\n')[:-1]
    cuboids = parse_indata(indata)

    print("part1:", part1(cuboids))
    print("part2:", part2(cuboids))

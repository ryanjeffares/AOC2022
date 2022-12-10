class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name: str):
        self.name = name
        self.dirs = []
        self.files = []

    def size(self) -> int:
        size = 0
        for f in self.files:
            size += f.size

        for d in self.dirs:
            size += d.size()

        return size


def problem_one(input_lines):
    dirs = {}
    nav_stack = []

    for line in input_lines:
        split = line.split(' ')

        if split[0] == '$':
            if split[1] == 'cd':
                current_dir = split[2]
                if current_dir == '..':
                    nav_stack.pop()
                else:
                    nav_stack.append(current_dir)
                    if current_dir not in dirs:
                        dirs[current_dir] = Directory(current_dir)
        elif split[0] == 'dir':
            dir_name = split[1]
            new_dir = Directory(dir_name)
            if new_dir not in dirs:
                dirs[new_dir] = new_dir
            dirs[nav_stack[len(nav_stack) - 1]].dirs.append(new_dir)
        else:
            size = int(split[0])
            name = split[1]
            file = File(name, size)
            dirs[nav_stack[len(nav_stack) - 1]].files.append(file)

    total = 0
    for dir_name, directory in dirs.items():
        size = directory.size()
        if size <= 100000:
            total += size

    return total


with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

print(problem_one(lines))

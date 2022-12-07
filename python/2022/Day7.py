import sys
from common import DataAnalyzer, Solver

input = DataAnalyzer.text("2022/day7.txt")


class Filesystem:
    def __init__(self):
        self._root = Node('/')
        self._cwd = self._root
        self._partition_size = 70000000
        self._update_partition_size = 30000000
    
    def mkdir(self, name):
        self._cwd._dirs.append(Node(name, self._cwd))
    
    def touch(self, name, size):
        file = Node(name, self._cwd, size=size)
        self._cwd._files.append(file)
    
    def cd(self, name):
        if name == '/':
            self._cwd = self._root
        elif name == '..':
            self._cwd = self._cwd.parent
        else:
            for dir in self._cwd._dirs:
                if dir.name == name:
                    self._cwd = dir
                    break
    
    def tree(self):
        self._root.stat(0)

    def du(self):
        return [dir.du() for dir in self._root._dirs]
    
    def syscheck(self, limit=100000):
        dirs = [item for subs in self.du() for item in subs]
        return sum([x[1] for x in dirs if x[1] <= limit])
    
    def update(self):
        if self._partition_size - len(self._root) < self._update_partition_size:
            diff = self._update_partition_size - (self._partition_size - len(self._root))
            dirs = [item for subs in self.du() for item in subs]
            from operator import itemgetter
            dirs.sort(key=itemgetter(1))

            for dir in dirs:
                if dir[1] >= diff:
                    return dir
        
        return ('', -1)
    
    def __len__(self):
        return len(self._root)


class Node:
    def __init__(self, name='', parent=None, size=0):
        self.name = name
        self.parent = parent

        self._dirs = []
        self._files = []
        self.__size__ = size
    
    def __len__(self):
        return self.__size__ if self.file() else sum([len(i) for i in self.nodes()])
    
    def nodes(self):
        return self._dirs + self._files
    
    def file(self):
        return not len(self._dirs) > 0 and not len(self._files) > 0
    
    def du(self):
        x = [(self.name, len(self))]
        [x.extend(dir.du()) for dir in self._dirs]
        return x

    def stat(self, depth):
        typeinfo = ' (dir)' if not self.file() else f' (file, size={len(self)})'
        print('  '*depth + ' - ' + self.name + typeinfo)
        [node.stat(depth+1) for node in self.nodes()]

filesystem = None


def filesystem_check():
    return filesystem.syscheck(limit=100000)

def update():
    return filesystem.update()

def run(input, cmd):
    global filesystem
    filesystem = Filesystem()

    for i in input:
        if i.startswith('$ '):
            if 'cd ' in i:
                filesystem.cd(i.split(' ')[2])
        else:  # ls output
            if i.startswith('dir '):
                filesystem.mkdir(i.split(' ')[1])
            else:
                split = i.split(' ')
                filesystem.touch(split[1], int(split[0]))

    return cmd()

def second():
    print(f"(2022 7.2) dir to delete for update => {run(input, update)}")

def first():
    print(f"(2022 7.1) total dir size => {run(input, filesystem_check)}")

if __name__ == '__main__':
    Solver.solve(sys.argv[1], first, second)

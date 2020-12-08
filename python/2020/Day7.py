import sys
from common import DataAnalyzer


def nesting(luggage, target):
    bags = 0

    del luggage[target]
    for key, value in luggage.items():
        bags += value

    return bags


def pack(data, target, suitcase={}, depth=1):
    # print("TARGET: {:s} => {:}".format(target, suitcase))
    for value in data[target]:
        print('CHECKING BAG: {:}'.format(value))
        count = 1 if value[0].isalpha() else int(value.split(' ')[0])
        style = target if value[0].isalpha() else value[2:]

        if 'no other' not in value:
            suitcase[style] = suitcase.get(style, 0) + (count * suitcase[target])
            pack(data, value[2:], suitcase, depth+1)
    
    return suitcase


def packer(file, target='shiny gold'):
    data = DataAnalyzer.text("2020/" + file)
    luggage = pack(patterns(data), target, {target : 1})
    print(suitcase)

    return nesting(luggage, target)


def options(data, target, current):
    check = []

    for key, values in data.items():
        for value in values:
            if target in value:
                current.add(key)
                options(data, key, current)

    return current


def patterns(data):
    patterns = {}

    for x in data:
        temp = x.replace('bags', '').split('contain')
        patterns[temp[0][:-1]] = temp[1][1:-1].split(', ')
    
    return patterns


def second():
    # print("(7.2.0) {:d} bags inside shiny gold bag".format(packer('day0.txt')))
    # print("(7.2.99) {:d} bags inside shiny gold bag".format(packer('day99.txt')))
    print("(7.2) {:d} bags inside shiny gold bag".format(packer('day7.txt')))


def first():
    data = DataAnalyzer.text("2020/day7.txt")
    result = options(patterns(data), 'shiny gold', set())
    print("(7.1) {:d} patterns for {:s}".format(len(result), 'shiny gold bag'))


def third():
    with open("../../resources/2020/day7.txt", "r") as fp:
        lines = fp.readlines()
        lines=[line.rstrip() for line in lines]

    # to make a dictionary of bags
    bag_types = []
    all_bags = {}
    for line in lines:
        mbag = " ".join(line.split(" ")[:2])
        contains = line[line.index("contain ")+8:-1]
        each_contain = contains.split(",")
        each_contain = [cnt.lstrip() for cnt in each_contain]
        each_contain = [" ".join(cont.split(" ")[:-1]) for cont in each_contain]
        #print(each_contain)
        each_contain = {" ".join(cont.split(" ")[1:]):cont.split(" ")[0] for cont in each_contain}
        #print(each_contain)
        if mbag not in bag_types:
            bag_types.append(mbag)
        if all_bags.get(mbag):
            each_contain.update(all_bags[mbag]) 
        all_bags[mbag] = each_contain

    def check_bag(bags, my_bag, current_bag):
        if current_bag==my_bag:
            return 1
        if bags.get(current_bag) is None:
            return 0
        else:
            counts = []
            for k, v in bags[current_bag].items():
                counts.append(check_bag(bags, my_bag, k))
            return max(counts)

    found_bags = 0
    my_bag = "shiny gold"
    for k, v in all_bags.items():
        if k != my_bag:
            found_bags+=check_bag(all_bags, my_bag, k)
    print(f"{found_bags} bags can contain {my_bag} bag.")


    my_bag = "shiny gold"
    bags_contains = {}
    test_bags=all_bags
    print(all_bags)
    for k, v in test_bags.items():
        bags_contains[k] = []
        try:
            for kk, vv in v.items():

                bags_contains[k]+=[kk]*int(vv)
        except:
            pass
    c=0

    def count_bags(current_bag):
        if current_bag==" " or bags_contains.get(current_bag) is None:
            return 0

        #print("key:", current_bag)
        cnt = len(bags_contains[current_bag])
        cnts = []
        for k in bags_contains[current_bag]:
            cnts.append(count_bags(k))    
        return sum(cnts)+cnt

    print(f"{my_bag} bag can hold {count_bags('shiny gold')} bags")

def solve(puzzle):

    if puzzle == '0':
        third()
    if puzzle == '1':
        first()
    elif puzzle == '2':
        second()
    else:
        first()
        second()


if __name__ == '__main__':
    solve(sys.argv[1])

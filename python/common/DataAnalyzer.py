import csv

PATH = "../../resources/"


def load(file):
    with open(PATH + file) as f:
        content = f.readlines()

    return content


def text(file):
    with open(PATH + file) as f:
        content = [line[:-1] for line in f.readlines()]

    return content


def str_csv(file):
    with open(PATH + file) as csvfile:
        content = [[str(x) for x in rec] for rec in csv.reader(csvfile, delimiter=',')]

    return content


def int_csv(file):
    with open(PATH + file) as csvfile:
        content = [[int(x) for x in rec] for rec in csv.reader(csvfile, delimiter=',')]

    return content


def ints(file):
    with open(PATH + file) as file:
        content = [int(x) for x in file.read().splitlines()]

    data = [int(x) for x in content]
    return data

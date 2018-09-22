def parser(filename):
    result=[]
    file = open(filename, "r")
    for line in file:
        result.append(line.splitlines()[0].split(" "))
    return result

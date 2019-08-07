MAX_INDEX = 3
line_changed = False


def get_line_changed():
    return line_changed


def set_line_changed(changed):
    global line_changed
    line_changed = changed


def next_not_zero(line, index):
    index += 1
    while index <= MAX_INDEX:
        if 0 != line[index]:
            return index
        index += 1
    return -1


def plus(line):
    i = 0
    while i <= MAX_INDEX:
        j = next_not_zero(line, i)
        if -1 != j and line[i] == line[j]:
            line[i] += line[j]
            line[j] = 0
            set_line_changed(True)
        i += 1
    return line

def move(line):
    i = 0
    while i <= MAX_INDEX:
        if 0 == line[i]:
            j = next_not_zero(line, i)
            if -1 != j:
                line[i] = line[j]
                line[j] = 0
                set_line_changed(True)
        i += 1
    return line
import os
import random
import logging
import line as row

WIDTH = 5
GOAL = 256
MAX_INDEX = 3
table_changed = False
table = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

logging.basicConfig(level=logging.DEBUG,
                    filename='256.log',
                    filemode='w',
                    format='%(message)s')


def get_table_changed():
    return table_changed


def set_table_changed(changed):
    global table_changed
    table_changed = changed


def show_table():
    os.system('cls')
    for line in table:
        show_line(line)


def show_line(line):
    shown_line = ''
    for num in line:
        if num == 0:
            shown_line += '·' + ' ' * (WIDTH - 1)
        else:
            shown_line += str(num) + ' ' * (WIDTH - len(str(num)))
    logging.debug('\n' + shown_line)
    print(shown_line)
    print('\n')


def get_new_table():
    new_table = [
        [table[0][0], table[1][0], table[2][0], table[3][0]],
        [table[0][1], table[1][1], table[2][1], table[3][1]],
        [table[0][2], table[1][2], table[2][2], table[3][2]],
        [table[0][3], table[1][3], table[2][3], table[3][3]],
    ]

    return new_table


def update_table(new_table):
    global table
    table = [
        [new_table[0][0], new_table[1][0], new_table[2][0], new_table[3][0]],
        [new_table[0][1], new_table[1][1], new_table[2][1], new_table[3][1]],
        [new_table[0][2], new_table[1][2], new_table[2][2], new_table[3][2]],
        [new_table[0][3], new_table[1][3], new_table[2][3], new_table[3][3]],
    ]


def left():
    for line in table:
        row.set_line_changed(False)
        line = row.plus(line)
        line = row.move(line)
        changed = row.get_line_changed()
        if changed:
            set_table_changed(changed)


def right():
    for line in table:
        row.set_line_changed(False)
        line.reverse()
        line = row.plus(line)
        line = row.move(line)
        line.reverse()
        changed = row.get_line_changed()
        if changed:
            set_table_changed(changed)


def up():
    new_table = get_new_table()
    for line in new_table:
        row.set_line_changed(False)
        line = row.plus(line)
        line = row.move(line)
        changed = row.get_line_changed()
        if changed:
            set_table_changed(changed)
    update_table(new_table)


def down():
    new_table = get_new_table()
    for line in new_table:
        row.set_line_changed(False)
        line.reverse()
        line = row.plus(line)
        line = row.move(line)
        line.reverse()
        changed = row.get_line_changed()
        if changed:
            set_table_changed(changed)
    update_table(new_table)


def full():
    for line in table:
        if 0 in line:
            return False

    return True


def new_num():
    if full():
        return

    line_index = random.randint(0, MAX_INDEX)
    column_index = random.randint(0, MAX_INDEX)
    if 0 == table[line_index][column_index]:
        table[line_index][column_index] = int(random.choice('24'))
    else:
        new_num()


def game_over(success):
    if success:
        print('GAME PASS😄 😄 😄 😄 😄')
    else:
        print('GAME OVER😭 😭 😭 😭 😭')
    exit()


def find_equal(table):
    for line in table:
        i = 0
        while i < MAX_INDEX:
            if line[i] == line[i + 1]:
                return True
            i += 1
    return False


def could_move():
    new_table = get_new_table()
    return find_equal(table) or find_equal(new_table)


def full():
    for line in table:
        if 0 in line:
            return False
    return True


def check():
    if full():
        if not could_move():
            game_over(False)
    else:
        for line in table:
            if GOAL in line:
                game_over(True)

import logging
import table
from pynput.keyboard import Key, Listener


logging.basicConfig(level=logging.DEBUG,
                    filename='256.log',
                    filemode='w',
                    format='%(message)s')


def on_press(key):
    if Key.up == key:
        logging.debug('\nup')
        table.up()
    elif Key.down == key:
        logging.debug('\ndown')
        table.down()
    elif Key.left == key:
        logging.debug('\nleft')
        table.left()
    elif Key.right == key:
        logging.debug('\nright')
        table.right()
    else:
        logging.debug('game_over:' + str(key))
        table.game_over(False)
        exit()

    if table.get_table_changed():
        table.new_num()
        table.set_table_changed(False)

    table.show_table()
    table.check()


table.new_num()
table.new_num()

table.show_table()
with Listener(on_press=on_press) as listener:
    listener.join()

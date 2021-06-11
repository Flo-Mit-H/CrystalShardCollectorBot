from pathlib import Path
import time
import pynput

keyboard = pynput.keyboard.Controller()
time_between_collect = 6
collected_shards_total = 0
collected_shards = 0
datapath = "shards.txt"


def press_and_release(char):
    keyboard.press(pynput.keyboard.KeyCode.from_char(char))
    keyboard.release(pynput.keyboard.KeyCode.from_char(char))


def press_array(press):
    chars = press.split()
    for char in chars:
        press_and_release(char)


def collect_shards():
    while True:
        increase_collected_shards()
        if(collected_shards_total % 2) == 0:
            # s!mine (every 10 seconds)
            press_array("s ! m i n e")
            enter()
            # s!search (every 5 seconds)
            press_array("s ! s e a r c h")
            enter()
        else:
            press_array("s ! s e a r c h")
        enter_print_save()
        time.sleep(time_between_collect)


def increase_collected_shards():
    global collected_shards_total
    global collected_shards
    collected_shards_total += 1
    collected_shards += 1


def enter():
    keyboard.press(pynput.keyboard.Key.enter)
    keyboard.release(pynput.keyboard.Key.enter)


def enter_print_save():
    enter()
    print("Collected {0} shards in this run and {1} shards in total".format(collected_shards, collected_shards_total))
    save_collected_shards()


def init_collected_shards():
    file = Path(datapath)
    if file.exists():
        with open(datapath, "r") as file:
            data = file.read()
            global collected_shards_total
            collected_shards_total = int(data)
    else:
        with open(datapath, "w") as file:
            file.write(str(collected_shards_total))
            file.close()


def save_collected_shards():
    with open(datapath, "w") as file:
        file.write(str(collected_shards_total))
        file.close()


if __name__ == "__main__":
    init_collected_shards()
    print("Starting to collect in 5 seconds")
    time.sleep(5)
    print("Starting to collect")
    collect_shards()

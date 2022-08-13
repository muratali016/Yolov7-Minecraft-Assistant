import keyboard
import uuid
import time
from PIL import Image
from mss import mss

mon = {
    "top": 19,
    "left": 19,
    "width": 2000,
    "height": 1200
}
sct = mss()

i = 0


def record_screen(record_id, key):
    global i
    i += 1
    print("{} {}".format(key, i))
    img = sct.grab(mon)
    a="sheep"
    im = Image.frombytes("RGB", img.size, img.rgb)
    im.save("./img_test/{}{}.png".format(a, i))


is_exit = False


def exit():
    global is_exit
    is_exit = True


keyboard.add_hotkey("9", exit)
record_id = uuid.uuid4()

while True:
    if is_exit: break
    try:

        if keyboard.is_pressed("1"):
            record_screen(record_id, "1")
            time.sleep(0.1)
        elif keyboard.is_pressed("2"):
            record_screen(record_id, "2")
            time.sleep(0.1)

        elif keyboard.is_pressed("3"):
            record_screen(record_id, "3")
            time.sleep(0.1)
        elif keyboard.is_pressed("4"):
            record_screen(record_id, "4")
            time.sleep(0.1)

        elif keyboard.is_pressed("5"):
            record_screen(record_id, "5")
            time.sleep(0.1)

        elif keyboard.is_pressed("6"):
            record_screen(record_id, "6")
            time.sleep(0.1)

        elif keyboard.is_pressed("7"):
            record_screen(record_id, "7")
            time.sleep(0.1)

        elif keyboard.is_pressed("8"):
            record_screen(record_id, "8")
            time.sleep(0.1)
        elif keyboard.is_pressed("9"):
            record_screen(record_id, "9")
            time.sleep(0.1)
    except RuntimeError:
        continue
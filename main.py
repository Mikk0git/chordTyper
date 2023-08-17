from pynput import keyboard


key_pressed = False
chord = ""
keyboard_controller = keyboard.Controller()


def keyPressed(key):
    global key_pressed
    try:
        key_pressed = True
        char = key.char
        print("Key pressed:", char)
        global chord
        chord = chord + char
    except:
        pass


def keyReleased(key):
    global key_pressed
    try:
        key_pressed = False
        # char = key.char
        # print("Key released:", char)
    except:
        pass


def delKey():
    keyboard_controller.press(keyboard.Key.backspace)
    keyboard_controller.release(keyboard.Key.backspace)


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed, on_release=keyReleased)
    listener.start()

    while True:
        if key_pressed:
            print("Waiting for key release...")
            while key_pressed:
                pass
            print("Key released. Waiting for key press... chord:", chord)

            chord = ""

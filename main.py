from pynput import keyboard

# Flaga wskazująca, czy klawisz jest wciśnięty
key_pressed = False
chord = ""


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

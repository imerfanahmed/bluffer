import pyautogui as pg
import time
import random

def random_mouse_movement():
    screen_width, screen_height = pg.size()
    x = random.randint(0, screen_width - 1)
    y = random.randint(0, screen_height - 1)
    pg.moveTo(x, y, duration=random.uniform(0.1, 0.5))

def switch_windows():
    # Simulate Alt+Tab to switch windows
    pg.keyDown("alt")
    pg.press("tab")
    pg.keyUp("alt")

def scroll_randomly():
    pg.scroll(random.randint(-10, 10))

def switch_tabs():
    # Simulate Ctrl+Tab to switch tabs in a browser or IDE
    pg.keyDown("ctrl")
    pg.press("tab")
    pg.keyUp("ctrl")

def type_random_characters():
    chars = 'abcdefghijklmnopqrstuvwxyz'
    char = random.choice(chars)
    pg.typewrite(char, interval=random.uniform(0.1, 0.3))

def do_stuff(wait):
    time.sleep(wait)
    for i in range(2000):
        action = random.choice([random_mouse_movement, switch_windows, scroll_randomly, switch_tabs, type_random_characters])
        action()
        time.sleep(random.uniform(0.5, 5))  # Random delay between actyions

do_stuff(5)
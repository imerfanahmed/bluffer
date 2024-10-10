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
    pg.keyDown("cmd")
    pg.press("tab")
    pg.keyUp("cmd")

def scroll_randomly():
    pg.scroll(random.randint(-10, 10))

def switch_tabs():
    # Simulate Ctrl+Tab to switch tabs in a browser or IDE
    pg.keyDown("ctrl")
    pg.press("tab")
    pg.keyUp("ctrl")

def type_random_characters():
    words = ['kodezen', 'wordpress', 'alms', 'github', 'how to do this', 'what is the issue', 'The code is fine']
    word = random.choice(words)
    pg.typewrite(word, interval=random.uniform(0.1, 1.5))

def do_stuff(wait):
    time.sleep(wait)
    for i in range(2000):
        action = random.choice([random_mouse_movement, switch_windows, scroll_randomly, switch_tabs, type_random_characters])
        action()
        time.sleep(random.uniform(0.5, 5))  # Random delay between actyions

do_stuff(5)

from datetime import date, datetime
from new_menu import start_the_game
import time

start = datetime.now()
running = True

while running:
    diff = (datetime.now() - start)
    sec = diff.seconds
    start_the_game
    if (sec > 60):
        running = False
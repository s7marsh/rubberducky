# ===============================================================================
# rubberducky.
#
# Copyright (c) 2022, Shintaro Marzo
# All rights reserved.
#
# BSD-3 License
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# ===============================================================================


from pynput import mouse, keyboard
import pyautogui as pg
import threading
import time
import random
from datetime import datetime

"""
Variables
"""
# some script flags
is_active = False
# So program won't exit when mouse is on (0,0) - upper left of screen
pg.FAILSAFE = False
# Controls the output messages displayed, higher means more messages
verbosity = 1
# Delay before checking the flag
polling_time = 10
min_poll_time = 3
max_poll_time = 17
# Counters
count_to_ctrl_tab = ((5*60) /  # 5 minutes
                     ((min_poll_time+max_poll_time)/2)  # average poll time
                     )
idle_count = 0  # initialize idle counter to 0


"""
Helper functions
"""


def vprint(v, message):
    """
    Controlled print behavior
    """
    if v <= verbosity:
        print(f'[{datetime.now().strftime("%H:%M:%S:%f")}] {message}')


def rand_float(start=0, end=1):
    randomized_float = random.random()
    return start + (end-start)*randomized_float


"""
Duck Things
"""


def square_move(length, duration):
    pg.moveRel(length, 0, duration)
    pg.moveRel(0, -1*length, duration)
    pg.moveRel(-1*length, 0, duration)
    pg.moveRel(0, length, duration)


def do_stuff():
    # Begin by pressing a safe key (QUACK!)
    pg.press("shift")
    # Move that mouse (SHAKE SHAKE SHAKE!)
    repeat = random.randint(3, 7)
    vprint(1, f'Move the mouse {repeat} times')
    for _ in range(repeat):
        square_move(100, 0.1)
    # End by pressing a safe key again (QUACK!)
    pg.press("shift")


def press_control_tab():
    pg.keyDown('ctrl')
    pg.press('tab')
    pg.keyUp('ctrl')


def duck_main():
    global is_active
    global polling_time
    global idle_count
    while True:
        polling_time = rand_float(min_poll_time, max_poll_time)
        vprint(1, f'Monitoring activity for {polling_time} secs')
        time.sleep(polling_time)

        # If you are doing something
        if is_active:
            idle_count = 0  # reset counter
        else:
            # Duck stufffff
            do_stuff()
            # Change scene once in a while
            if idle_count < count_to_ctrl_tab:
                idle_count += 1
            else:
                vprint(1, f'Control+Tab')
                press_control_tab()
                idle_count = 0  # reset counter

        # Clear is_active
        is_active = False


"""
Input Monitors: Set flag to active upon detection of activity
"""


def on_press(key):
    global is_active
    vprint(2, f'pressed "{key}"')
    is_active = True


def on_move(x, y):
    global is_active
    vprint(2, f'mouse moved to "({x},{y})"')
    is_active = True


def on_scroll(x, y, dx, dy):
    global is_active
    vprint(2, f'scrolled by "({dx},{dy})"')
    is_active = True


def on_click(x, y, button, pressed):
    global is_active
    vprint(2, f'{"clicked" if pressed else "released"} with {button}')
    is_active = True


if __name__ == '__main__':
    kb_listener = keyboard.Listener(on_press=on_press)
    mouse_listener = mouse.Listener(on_move=on_move,
                                    on_click=on_click,
                                    on_scroll=on_scroll)
    duck_thread = threading.Thread(target=duck_main)
    # Start Input listening and Duck threads in parallel...
    kb_listener.start()
    mouse_listener.start()
    duck_thread.start()
    # ... before joining them
    kb_listener.join()
    mouse_listener.join()
    duck_thread.join()

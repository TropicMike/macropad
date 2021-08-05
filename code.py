"""
A fairly straightforward macro/hotkey program for Adafruit MACROPAD.
Macro key setups are stored in the /macros folder (configurable below),
load up just the ones you're likely to use. Plug into computer's USB port,
use dial to select an application macro set, press MACROPAD keys to send
key sequences.
"""

# pylint: disaaaable=import-error, unused-import, too-few-public-methods

import os
import displayio
import terminalio
import usb_hid
from adafruit_display_shapes.rect import Rect
from adafruit_display_text import label
from adafruit_macropad import MacroPad
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

# CONFIGURABLES ------------------------

MACRO_DEFINITIONS = "/macros/work"


# CLASSES AND FUNCTIONS ----------------


class App:
    """Class representing a host-side application, for which we have a set
    of macro sequences. Project code was originally more complex and
    this was helpful, but maybe it's excessive now?"""

    def __init__(self, appdata):
        self.name = appdata["name"]
        self.macros = appdata["macros"]

    def switch(self):
        """Activate application settings; update OLED labels and LED
        colors."""
        GROUP[13].text = self.name  # Application name
        for i in range(12):
            if i < len(self.macros):  # Key in use, set label + LED color
                MACROPAD.pixels[i] = self.macros[i][0]
                GROUP[i].text = self.macros[i][1]
            else:  # Key not in use, no label or LED
                MACROPAD.pixels[i] = 0
                GROUP[i].text = ""
        MACROPAD.keyboard.release_all()
        MACROPAD.pixels.show()
        MACROPAD.display.refresh()


# INITIALIZATION -----------------------

MACROPAD = MacroPad()
MACROPAD.display.auto_refresh = False
MACROPAD.pixels.auto_write = False

# Set up displayio group with all the labels
GROUP = displayio.Group()
for KEY_INDEX in range(12):
    x = KEY_INDEX % 3
    y = KEY_INDEX // 3
    GROUP.append(
        label.Label(
            terminalio.FONT,
            text="",
            color=0xFFFFFF,
            anchored_position=(
                (MACROPAD.display.width - 1) * x / 2,
                MACROPAD.display.height - 1 - (3 - y) * 12,
            ),
            anchor_point=(x / 2, 1.0),
        )
    )
GROUP.append(Rect(0, 0, MACROPAD.display.width, 12, fill=0xFFFFFF))
GROUP.append(
    label.Label(
        terminalio.FONT,
        text="",
        color=0x000000,
        anchored_position=(MACROPAD.display.width // 2, -2),
        anchor_point=(0.5, 0.0),
    )
)
MACROPAD.display.show(GROUP)

# Load all the macro key setups from .py files in MACRO_FOLDER
APPS = []

# ======================
# Load macro definitions
# ======================
module = __import__(MACRO_DEFINITIONS)
APPS.append(App(module.app))

# LAST_POSITION = None
# LAST_ENCODER_SWITCH = MACROPAD.encoder_switch_debounced.pressed
APP_INDEX = 0
APPS[APP_INDEX].switch()

# the keyboard object!
cc = ConsumerControl(usb_hid.devices)

# MAIN LOOP ----------------------------
last_position = 0
while True:

    # ====================
    # Handle encoder wheel
    # ====================
    MACROPAD.encoder_switch_debounced.update()

    if MACROPAD.encoder_switch_debounced.pressed:
        cc.send(ConsumerControlCode.MUTE)
        # MACROPAD.mouse.click(MACROPAD.Mouse.RIGHT_BUTTON)

    current_position = MACROPAD.encoder

    if MACROPAD.encoder > last_position:
        cc.send(ConsumerControlCode.VOLUME_INCREMENT)
        last_position = current_position

    if MACROPAD.encoder < last_position:
        cc.send(ConsumerControlCode.VOLUME_DECREMENT)
        last_position = current_position
    # ====================

    EVENT = MACROPAD.keys.events.get()
    if not EVENT or EVENT.key_number >= len(APPS[APP_INDEX].macros):
        continue  # No key events, or no corresponding macro, resume loop
    KEY_NUMBER = EVENT.key_number
    PRESSED = EVENT.pressed

    # If code reaches here, a key or the encoder button WAS pressed/released
    # and there IS a corresponding macro available for it...other situations
    # are avoided by 'continue' statements above which resume the loop.

    SEQUENCE = APPS[APP_INDEX].macros[KEY_NUMBER][2]
    if PRESSED:
        if KEY_NUMBER < 12:  # No pixel for encoder button
            MACROPAD.pixels[KEY_NUMBER] = 0xFFFFFF
            MACROPAD.pixels.show()
        for item in SEQUENCE:
            if isinstance(item, int):
                if item >= 0:
                    MACROPAD.keyboard.press(item)
                else:
                    MACROPAD.keyboard.release(item)
            else:
                MACROPAD.keyboard_layout.write(item)
    else:
        # Release any still-pressed modifier keys
        for item in SEQUENCE:
            if isinstance(item, int) and item >= 0:
                MACROPAD.keyboard.release(item)
        if KEY_NUMBER < 12:  # No pixel for encoder button
            MACROPAD.pixels[KEY_NUMBER] = APPS[APP_INDEX].macros[KEY_NUMBER][0]
            MACROPAD.pixels.show()

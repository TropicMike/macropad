# https://learn.adafruit.com/macropad-hotkeys/custom-configurations
# MJS - Macros for Zoom, etc.

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Work', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'Mute', [Keycode.LEFT_ALT, 'a']),        # Alt-a - mute/unmute self
        (0x400000, 'Video', [Keycode.LEFT_ALT, 'v']),       # Alt-v - start/stop video camera
        (0x553700, 'Share', [Keycode.LEFT_ALT, 's']),       # Alt-s - start/stop screen sharing
        # 2nd row ----------
        (0x004000, 'FullScreen', [Keycode.LEFT_ALT, 'f']),
        (0x000000, ' ', ['']),
        (0x400000, 'End', [Keycode.LEFT_ALT, 'q']),                     # Alt-q - end meeting
        # 3rd row ----------
        (0x000000, ' ', ['']),
        (0x000000, ' ', ['']),
        (0x000000, ' ', ['']),
        # 4th row ----------
        # MJS - note the - unpresses the key
        (0x000040, 'Ada', [Keycode.COMMAND, 'n', -Keycode.COMMAND,
                           'www.adafruit.com\n']),   # Adafruit in new window
        (0x800000, 'Digi', [Keycode.COMMAND, 'n', -Keycode.COMMAND,
                            'www.digikey.com\n']),   # Digi-Key in new window
        (0x101010, 'Hacks', [Keycode.COMMAND, 'n', -Keycode.COMMAND,
                             'www.hackaday.com\n']), # Hack-a-Day in new win
        # Encoder button ---
        (0x000000, '', [Keycode.COMMAND, 'w']) # Close window/tab
    ]
}

#>>> from adafruit_hid.keycode import Keycode
#>>> print(dir(Keycode))
# ['__class__', '__module__', '__name__', '__qualname__', '__bases__', '__dict__', 'C', 'M', 'A', 'B',
# 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
# 'Y', 'Z', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'ZERO', 'ENTER',
# 'RETURN', 'ESCAPE', 'BACKSPACE', 'TAB', 'SPACEBAR', 'SPACE', 'MINUS', 'EQUALS', 'LEFT_BRACKET',
# 'RIGHT_BRACKET', 'BACKSLASH', 'POUND', 'SEMICOLON', 'QUOTE', 'GRAVE_ACCENT', 'COMMA', 'PERIOD',
# 'FORWARD_SLASH', 'CAPS_LOCK', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11',
# 'F12', 'PRINT_SCREEN', 'SCROLL_LOCK', 'PAUSE', 'INSERT', 'HOME', 'PAGE_UP', 'DELETE', 'END',
# 'PAGE_DOWN', 'RIGHT_ARROW', 'LEFT_ARROW', 'DOWN_ARROW', 'UP_ARROW', 'KEYPAD_NUMLOCK',
# 'KEYPAD_FORWARD_SLASH', 'KEYPAD_ASTERISK', 'KEYPAD_MINUS', 'KEYPAD_PLUS', 'KEYPAD_ENTER', 'KEYPAD_ONE',
# 'KEYPAD_TWO', 'KEYPAD_THREE', 'KEYPAD_FOUR', 'KEYPAD_FIVE', 'KEYPAD_SIX', 'KEYPAD_SEVEN', 'KEYPAD_EIGHT',
# 'KEYPAD_NINE', 'KEYPAD_ZERO', 'KEYPAD_PERIOD', 'KEYPAD_BACKSLASH', 'APPLICATION', 'POWER', 'KEYPAD_EQUALS',
# 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19', 'LEFT_CONTROL', 'CONTROL', 'LEFT_SHIFT', 'SHIFT',
# 'LEFT_ALT', 'ALT', 'OPTION', 'LEFT_GUI', 'GUI', 'WINDOWS', 'COMMAND', 'RIGHT_CONTROL', 'RIGHT_SHIFT',
# 'RIGHT_ALT', 'RIGHT_GUI', 'modifier_bit']

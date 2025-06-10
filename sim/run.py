import importlib.util, pathlib, board

# Dynamically load the generated C replacement written in Python for demo
# (In real life you'd compile & link the C; here we mimic behaviour.)
def led_toggle(button_pressed):
    if button_pressed:
        board.LED_STATE ^= 1
        board.write_led(board.LED_STATE)

# Fake button presses
for press in [1, 0, 1, 1]:
    led_toggle(press)

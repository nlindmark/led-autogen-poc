# sim/run.py

import sys
import os
# Insert project root into sys.path so imports like `specs.led` resolve.
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from specs.led import LEDModule

if __name__ == "__main__":
    m = LEDModule()
    print("Initial LED state:", m.LED_STATE)
    for press in [1, 0, 1, 1]:
        print(f"\nButton pressed: {press}")
        m.toggle(press)
        state = m.LED_STATE
        print("LED state now:", state)

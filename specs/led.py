# specs/led.py

from autogen.decorators import c_module, c_function
from sim.board import write_led

@c_module(name="led", category="service", header="led.h")
class LEDModule:
    """Module to control a single LED."""
    LED_STATE: int = 0

    @c_function(
        name="led_toggle",
        inputs=[("button_pressed", "int")],
        outputs=[],
        description="Toggle LED when button is pressed"
    )
    def toggle(self, button_pressed: int):
        if button_pressed:
            self.LED_STATE ^= 1
            write_led(self.LED_STATE)

    @c_function(
            name="led_status",
            inputs=[], 
            outputs=[("state", "int")],
            description="Return current LED state"
        )
    def status(self) -> int:
        # This both drives the generated stub and powers your Python sim
        return self.LED_STATE
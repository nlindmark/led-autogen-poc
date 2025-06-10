LED_STATE = 0

def write_led(value):     # hardware stub
    global LED_STATE
    LED_STATE = value
    print("LED:", "ON" if value else "OFF")

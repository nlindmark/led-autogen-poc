// AUTOGEN_SHA256:31c01079171c8690dba7c87521d6273473742f737ddf32e6f1c2b8c57a46122f
#include "led.h"
static int LED_STATE = 0;          /* 0 = off */

void led_toggle(int button_pressed)
{
    if (button_pressed) {
        LED_STATE ^= 1;            /* toggle */
    }
}
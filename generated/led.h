// AUTOGEN_SHA256:3ae2e5ff43db9776b7bd7622fab0689a471877677666d2388c196a6b70474eea
#ifndef LED_H_
#define LED_H_

/* Module: led  
   Category: service  
   MISRA: C:2012 */

/**
 * Return current LED state
 */
int
led_status();
/**
 * Toggle LED when button is pressed
 */
void
led_toggle(int button_pressed);

#endif /* LED_H_ */
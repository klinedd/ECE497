Homework 2 Readme file

ButtonsAndLEDs:
	When you run this file you can toggle the LEDS on whenever you are
	pressing the button down. When you lift off the button the lights
	will turn off again.
	*note* This logic is opposite for two of the LEDs. This is caused
	because of the way some of the GPIO pins are set to pull up, while
	others are set to pull down.

Etch-a-sketch:
	When you run the program, if you are looking at the board while the 
	beaglebone is above the breadboard, the far left button will move the
	etch-a-sketch to the right, the button directly right of that button
	moves the etch-a-sketch to the left. The third button from the left
	moves the etch-a-sketch down, while the far right button move the 
	etch-a-sketch up. 
	*note* I seem to be having a debouncing issue with the buttons to
	where the pressing the button once will move the etch-a-sketch two
	blocks instead of one, causing a break in the etcha-a-sketch line.

# Comments from Prof. Yoder
# Nice documentation  
# Grade:  10/10
List below instructs what I have done for each portion of hw01:

	1. I installed latest image on BeagleBone. However, as mentioned in 
	Tuesday's class, there is a new image that the professor will have us
	update to in the near future.

	2. Host computer has a functioning native version of ubuntu
	
	3. Attained kit from the parts room, bought two 8gig SD cards,
	and purchased a powered 4 x USB3.0 dongle.

	4. Git is working on computer and beaglebone. Finished the exercises
	getLearn and gitLearnFork

	5. I believe I successfully signed up for both groups. Awaiting a 
	digest in the form of an email to confirm

	6. etch-a-sketch program works and just needs to be documented at the 
	time of this writting	

// Comment from Prof. Yoder
// I'm having trouble running your code.  Demo in class
// Thanks for the demo
// Grade:  10/10

sudo ./etch.py 
sudo: unable to resolve host bone-0834
ALSA lib confmisc.c:767:(parse_card) cannot find card '0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_card_driver returned error: No such file or directory
ALSA lib confmisc.c:392:(snd_func_concat) error evaluating strings
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_concat returned error: No such file or directory
ALSA lib confmisc.c:1246:(snd_func_refer) error evaluating name
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM default
What X by X size grid do you want?5
Traceback (most recent call last):
  File "./etch.py", line 9, in <module>
    screen = pygame.display.set_mode((100*size,100*size))
pygame.error: No video mode large enough for 500x500
debian@bone-0834:~/studentWork/kline/hw01$ ./etch.py 
ALSA lib pcm_hw.c:1713:(_snd_pcm_hw_open) Invalid value for card
What X by X size grid do you want?5
Traceback (most recent call last):
  File "./etch.py", line 9, in <module>
    screen = pygame.display.set_mode((100*size,100*size))
pygame.error: Unable to open a console terminal

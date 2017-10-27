#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h> 
#include <signal.h>    // Defines signal-handling functions (i.e. trap Ctrl-C)
#include "beaglebone_gpio.h"

/****************************************************************
 * Global variables
 ****************************************************************/
int keepgoing = 1;    // Set to 0 when ctrl-c is pressed

/****************************************************************
 * signal_handler
 ****************************************************************/
void signal_handler(int sig);
// Callback called when SIGINT is sent to the process (Ctrl-C)
void signal_handler(int sig)
{
    printf( "\nCtrl-C pressed, cleaning up and exiting...\n" );
	keepgoing = 0;
}

int main(int argc, char *argv[]) {
    volatile void *gpioB_addr;
    volatile unsigned int *gpioB_oe_addr;
    volatile unsigned int *gpioB_datain;
    volatile unsigned int *gpioB_setdataout_addr;
    volatile unsigned int *gpioB_cleardataout_addr;

    // Set the signal callback for Ctrl-C
    signal(SIGINT, signal_handler);

    int fd = open("/dev/mem", O_RDWR);

    printf("Mapping %X - %X (size: %X)\n", GPIO3_START_ADDR, GPIO3_END_ADDR, 
                                          GPIO3_SIZE);
    //CREATE MMAP For Button
    gpioB_addr = mmap(0, GPIO3_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 
                        GPIO3_START_ADDR);

    gpioB_oe_addr           = gpioB_addr + GPIO_OE;
    gpioB_datain            = gpioB_addr + GPIO_DATAIN;
    gpioB_setdataout_addr   = gpioB_addr + GPIO_SETDATAOUT;
    gpioB_cleardataout_addr = gpioB_addr + GPIO_CLEARDATAOUT;
    
    if(gpioB_addr == MAP_FAILED) {
        printf("Unable to map GPIO\n");
        exit(1);
    }
    printf("GPIO mapped to %p\n", gpioB_addr);
    printf("GPIO OE mapped to %p\n", gpioB_oe_addr);
    printf("GPIO SETDATAOUTADDR mapped to %p\n", gpioB_setdataout_addr);
    printf("GPIO CLEARDATAOUT mapped to %p\n", gpioB_cleardataout_addr);
    
    printf("Start copying GPIO_07 to GPIO_03\n");
    while(keepgoing) {
    	if(*gpioB_datain & GPIO3_2) {
            *gpioB_setdataout_addr=GPIO3_1;
            //printf("ButtonL being Pressed\n");
    	} else {
            *gpioB_cleardataout_addr = GPIO3_1;
    	}
    	  
        //usleep(100000);
    }

    close(fd);
    return 0;
}


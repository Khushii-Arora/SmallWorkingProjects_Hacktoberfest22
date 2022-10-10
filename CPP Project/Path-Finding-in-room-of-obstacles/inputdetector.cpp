#include <iostream>
#include <sys/select.h>
#include<time.h>
#include <unistd.h>

int kbhit(void)
{
    struct timeval tv;
    fd_set read_fd;
    
    tv.tv_sec=0;
    tv.tv_usec=0;

    FD_ZERO(&read_fd);

    FD_SET(0,&read_fd);

    if(select(1, &read_fd,NULL, NULL, &tv) == -1)
        return 0;  /* An error occured */
  
    if(FD_ISSET(0,&read_fd))
        return 1;
      
    return 0;
}
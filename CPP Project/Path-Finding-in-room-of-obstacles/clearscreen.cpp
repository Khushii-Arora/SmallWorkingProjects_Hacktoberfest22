#include <iostream>

void clear(){
#if defined(__unix__) || defined(__unix) || defined(__linux__)
#define OS_LINUX
#elif defined(WIN32) || defined(_WIN32) || defined(_WIN64)
#define OS_WIN
#elif defined(__APPLE__) || defined(__MACH__)
#define OS_MAC
#else
#error Unknown Platform
#endif
#if defined(OS_LINUX) || defined(OS_MAC)
system("clear");

#elif defined(OS_WIN)
system("CLS");
#endif
}
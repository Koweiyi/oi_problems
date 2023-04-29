#include<stdio.h>

extern void Log(const char* message);

int main(){
    auto s = "hello koweiyi";
    Log(s);
    return 0;
}
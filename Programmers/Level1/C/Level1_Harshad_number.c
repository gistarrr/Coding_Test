#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool solution(int x) {
    int n,m,k,l;
    bool answer = true;
    if(1<=x && x<10)
    {
        answer=true;
    }
    else if(10<=x && x<100)
    {
        n=x/10;
        m=x%10;
        if(x%(n+m)==0)
            answer=true;
        else
            answer = false;
    }
    else if(100<=x && x<1000)
    {
        n=x/100;
        m=(x-n*100)/10;
        k=(x-n*100)%10;
        if(x%(n+m+k)==0)
            answer=true;
        else answer = false;
    }
    else if(1000<=x && x<10000)
    {
        n=x/1000;
        m=(x-n*1000)/100;
        k=(x-n*1000-m*100)/10;
        l=(x-n*1000-m*100)%10;
        if(x%(n+m+k+l)==0)
            answer=true;
        else answer = false;
    }
    else if(x==10000)
        answer=true;

    return answer;
}
#include <stdio.h>
#include <math.h>
//this algorithm will reverse any number you give it 
int reverse(int N)
{
    int temp,counter,i,j;
    int t[100];
    j=0;
    while(N>0)
    {
        counter=0;
        while(N>=10)
        {
            N=N-10;
            counter++;
        }
        t[j]=N;
        N=counter;
        j++;
    }
    temp=j-1;
    i=temp;
    j=0;N=0;
    while(i>=0&&j<=temp)
    {
        int x=pow(10,i);
        N=N+t[j]*x;
        i--;j++;
    }
    return N;
}

int main()
{
    printf("give me a number you like it to be reversed\n");
    int N;
    int n=N;
    scanf("%d",&N);
    int temporary=reverse(N);
    N=temporary;
    printf("the reverse of %d is %d\n",n,N);
    return 0;
}
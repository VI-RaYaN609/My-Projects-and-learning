#include <stdio.h>

int main(){
    int i,j,n,temp,t[100];
    printf("Give me a number n ");
    scanf("%d",&n);
    for (i=0;i<=n-1;i++)
    {
        printf("Give me T[%d]",i);
        scanf("%d",&t[i]);
    }
    for (i=0;i<=n-2;i++)
    {
        for(j=i+1;j<=n-1;j++)
        {
            if (t[i]>t[j])
            {
               temp=t[i];
               t[i]=t[j];
               t[j]=temp;
            }
        }
    }
    for (i=0;i<=n-1;i++){
        printf("T[%d]=%d\t",i,t[i]);
    }
    return 0;
}
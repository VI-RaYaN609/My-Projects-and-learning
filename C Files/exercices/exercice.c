#include <stdio.h>

int main()
{
    int i,N,j,min,Imin;
    int t[100];

      printf("This algorithm will request a table and will sort it out and give you max,min,somme\n");
    do
    {
        printf("Give me the number of coloumns N(0<N<100)\n");
        scanf("%d",&N);
    } while (N>100 || N<0);
    
//scan table
    for(i=1;i<=N;i++)
    {
        printf("Give me a value for T[%d]\n",i);
        scanf("%d",&t[i]);
    }
    i=1;
     while (i<=N-1)
     {
        min=t[i];
        Imin=i;
        printf("Min= %d Imin= %d\n",min,Imin);
        for(j=i+1;j<=N;j++)
        {
            if(min>t[j])
            {
                min=t[j];
                Imin=j;
            }
        }
        t[Imin]=t[i];
        t[i]=min;
        i++;
     }
     int somme=0;
     for(i=1;i<=N;i++){
       somme = somme +t[i];
     }  
      i=N;    
      printf("min=%d\t max=%d\t Somme=%d\n",t[1],t[i],somme);
//print table
    for(i=1;i<=N;i++)
    {
        printf("T[%d]=%d\t",i,t[i]);
    }

    return 0;
}
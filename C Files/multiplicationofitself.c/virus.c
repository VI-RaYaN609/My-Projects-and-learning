#include <stdio.h>
#include <string.h>



int main()
{
    int i,j;
    int k=0;
    int z=0;
    char buffer[255];
    for( i=1;i<=100;i++)
    {  
       sprintf(buffer,"C:\\Users\\VI RaYaN\\Desktop\\VS Code\\C Files\\multiplicationofitself.c\\VirusFiles\\file%d.txt",i);
       fopen;
        FILE *pF= fopen(buffer,"a");
        
        for(j=1;j<=100;j++)
        
        {fprintf(pF,"VIRUSVIRUSVIRUSVIRUSVIRUSVIRUSVIRUSVIRUSVIRUSVIRUSVIRUSVIRUS\n");
        k++;
        }
        fclose(pF);
        z++;
    }
    printf("Line got wroten %d times\n",k);
    printf("File Opened %d times",z);
    return 0;
}

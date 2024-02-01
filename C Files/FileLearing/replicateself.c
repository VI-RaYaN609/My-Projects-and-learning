#include<stdio.h>



int main()
{
    char buffer[255];

    FILE *file=fopen("test.c","r");
    if(file==NULL)
    {
        printf("Unable to open FILE");
        return 1;
    }
    FILE *replica=fopen("replica.c","w");
    if(replica==NULL)
    {
        printf("Unable to open replica");
        return 1;
    }
    int ch;
    while ((ch = fgetc(file))!=EOF)
    {
        fputc(ch,replica);
    }
    fclose(file);
    fclose(replica);
    return 0;
}
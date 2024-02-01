#include <stdio.h>
#include <math.h>

int main(){
int i,j,age;
char Name[25];
printf("hi what's you're name?\n");
scanf("%s",&Name);
printf("how old are you %s.\n",Name);
scanf("%d",&age);
while (age<=2)
{
    printf("haha,are you messing with me ?\ngive me your real age\n");
    scanf("%d",&age);
}

if(age>18)
        {
        printf("oh, your older then me,\n im 18");
        }
        else if(age==18)       
        {
        printf("oh, we are both 18 !!");
        }
        // else if(age<0)
        // {
        //     printf("haha,are you messing with me ?");
        // }
        else if (age<5)
        {
        printf("how are you reading and typing ...,you are %d",age);
        }
            else
        {
                printf("oh, your yonger then me,\nIm 18 ");
        }

    return 0;
     }
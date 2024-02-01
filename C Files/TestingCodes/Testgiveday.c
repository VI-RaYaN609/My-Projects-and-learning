#include <stdio.h>

int main(){
int i;
 printf("give me a day number (sunday is day 1)\n");
 scanf("%d",&i);
while (i==0||i>7)         //! ||= OR | && = AND | ! = NOT                    
{
 printf("no give me a number between 1 and 7\n");
 scanf("%d",&i);
}
switch(i)
{
 case 1:
  printf("Today is Sunday !!");
   break;    
 case 2:
  printf("Today is Monday !!");
   break;
 case 3:
  printf("Today is Tuesday !!");
   break;
 case 4:
  printf("Today is Wednesday !!");
   break;
 case 5:
  printf("Today is Thursday !!");
   break;
 case 6:
  printf("Today is Friday !!");
   break;
 case 7:
  printf("Today is Saturday !!");
   break;
}
    return 0;
}
#include <stdio.h>
#include <math.h> //!adds math functions :( sqrt ),( pow ),( round ),(   ceil   ),( floor  ), (  fabs  ),(log),(sin),(cos),(tan)
#include <string.h>                   // square root x**y    tadwir    round up   round down  make number
                                                                                             // positive

  // !   Variables: Blue ones are the most used
  // ? int= nombre entier 'N'  the number can be from (-2Bill to 2bill)     %d     
  //   unsinged int = a positive only number  (entier)                      %u     (unsigned remove the negative
  // ? float=nombre reel 'R'  Display 6-7 digits Max                        %f     side and add more positive ) Example :
  // ? double= nombre reel 'R' Display 15-16 digits Max                     %lf    unsigneed short is a number that can 
  // ? char= character like a,b,c        (for only one character)  =        %c     be from (0 to 65,535)   
  //                                     (for one or more characters)=      %s     65,535=32,768+32,767
  //  short=int but the number can be from (-32,768 to 32,767)             %d
  // ? bool= can store 1 byte mostly used for true or false                 %d       #include <bool.h>
    
  //   to make a variable a constant type "const" before the number type (int,float...)


  //TODO Arrays: int Tab[10]={    };

int main(){ 
    
int i=1,N;
float j;
char name[25];

 printf("What's your name?\n");
 fgets(name, 25, stdin);
 name[strlen(name)-1]='\0';
printf("Give me a number:\n");
scanf("%d",&i);
j=i*10;
printf("\"the number is \t j=%-2.3f\"\n",j);/* %.1 means 1 numbers in decimels (vergule)
                                            /* %1 alocate more space for number in right side (you have more room for number)
                                             %- left align
                                           */
 
 printf("Hello %s , how are you doing ?",name);
return 0;
}
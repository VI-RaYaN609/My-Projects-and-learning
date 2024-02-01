#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//NEVER USE THIS FOR ANY SORT OF SECURITY 
int main()
{
//   srand(time(0));
//   int randomnumber=rand()%6 +1;  // rand()% 'max number to be generated'
//   printf("number is %d",randomnumber);
//     return 0;   

//A game
int num= rand()%100 +1;
int guess,guesses,answer;
  
   srand(time(0));
   answer=rand()%1000+1;
   guesses=0;
   do
   {
    printf("Guess a number\n");
    scanf("%d",&guess);
    if(guess-answer<100&&guess-answer>0)
    {
     printf("guess is high!\n");   
    }
    else if(guess>answer)
    {
    printf("guess is Too high\n");
    }
    else if (answer-guess<100&&answer-guess>0)
    {
     printf("guess is low!\n");   
    }
    else if (guess<answer)
    {
     printf("guess is Too low\n");   
    }
    else{printf("Correct !!\n");} 
    guesses++;
   } while (guess!=answer);
   printf("Answer is :%d\nNumber of guesses is :\t%d",answer,guesses);
   

}
#include<stdio.h>
 
 int coindispense()
 {  
  int I;  
  int coin=150;
  
   if(coin>=100)
   {
     printf("100 Da Dispent");
     coin=coin-100;
     I=1;
      while(coin>=100)
      {
        coin=coin-100;
        I++;
      }
      printf("\t%d times",I); 
   }

if(I>1){
 printf("\n");
 }
   
   if(coin>=50)
   {
     printf("50 Da Dispent");
     coin=coin-50;
     I=1;
      while(coin>=50)
      {
        coin=coin-50;
        I++;
      }
      printf("\t%d times",I); 
   }
 if(I>1){
 printf("\n");
 }

    if(coin>=20)
    {
     printf("20 Da Dispent");
     coin=coin-20;
    I=1;
      while(coin>=20)
      {
        coin=coin-20;
        I++;
      }
      printf("\t%d times",I); 
    }
 
if(I>1){
 printf("\n");
 }
 
    if(coin>=10)
   {
     printf("10 Da Dispent");
     coin=coin-10;
     I=1;
      while(coin>=10)
      {
        coin=coin-10;
        I++;
      }
      printf("\t%d times",I); 
   }

 return 0; 
 }
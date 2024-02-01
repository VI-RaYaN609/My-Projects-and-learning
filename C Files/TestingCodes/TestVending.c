#include <stdio.h>
#include <stdbool.h>
#include <string.h>
// void coindispense(int coin)
// {
// while (coin>=100)
// {
// printf(" 100 coin Dispented.\n");
// coin=coin-100;
// }
// while (coin>=50)
// {
// printf("50 coin Dispented.\n");
// coin=coin-50;
// }
// while (coin>=20)
// {
// printf("20 coin Dispented.\n");
// coin=coin-20;
// }
// while (coin>=10)
// {
// printf("10 coin Dispented.\n");
// coin=coin-10;
// }
// if (coin==5)
// {
// printf("5 coin Dispented.\n");
// coin=coin;
// }
// printf("you have %d credits Left!!!\n Have a wonderfull day.",coin);

// }
void coindispense(int coin)
 {  
  int I;  
  
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

if(I>=0){
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
 if(I>0){
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
 
if(I>0){
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

 }



int main()
{
int credit,credit1,item,coin,i,j;
int x,y,z;
bool e;
char name1[]="Water";
char name2[]="Juice";
char name3[]="Chocolate bar";
char name[25];
char tf[25];
char Y[]="yes";

printf("\"Insert Coin\"\n");
scanf("%d",&credit);
printf("You have %d credit\n",credit);
printf("Choose Product\"from 1-20(water)21-30(Juices)31-40(chocolate Bar) \"\n ");
scanf("%d",&i);

if(i<21)
{ item=20;
printf("%s is %d Da\n",name1,item);
strcpy(name,name1);

}

else if(i<31)
{ item=40;
printf("%s is %d Da\n",name2,item);
strcpy(name,name2);
j=y;
}

else
{ item=60
;printf("%s is %d Da\n",name3,item)
;strcpy(name,name3);
j=z;
}
  
 
  if(item>credit)
  {
    int need=item-credit;
   coin=credit;
   printf("Do you wish to Insert more coins?(Y/N)\n");
   scanf("%s",&tf);
   strlwr(tf);
   e=strcmp(tf,Y);     //this will compare the user answer with yes if it is the same e will be 0  
          if(e==0)
          {
            do
            {
           printf("\"Insert Coin %dDa\"\n",need);
           scanf("%d",&credit1);
           credit=credit+credit1;
           need=need-credit1;
              
            } while (item>credit);
            
           coin=credit-item;
           printf("Enjoy your %s!!\n",name);
           printf("you have %d credit left.\n",coin);
           coindispense(coin);
           printf("Have a good day!");
          }
          else
           {
           printf("Dispensing....\n");
           coindispense(coin);
           }
  }
  else
{
    if(j==0)
    {
     printf("%d\n",j);
     printf("Can't you see that there is no %s left?\n",name);
    }
    else
      {
   coin=credit-item;
   printf("Enjoy your %s!!\n",name);
   printf("you have %d credit left.\n",coin);
              if(coin==0)
              {
              printf("Have a good day =)"); 
              }
              else
              {
               coindispense(coin);
              }
       }

 }
return 0;  
}
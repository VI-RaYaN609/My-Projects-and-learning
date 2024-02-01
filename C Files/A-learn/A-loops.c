#include <stdio.h>

int main()
{
int i,j;
int k=0;

for(i=1;i<=10;i=i+1)
{
printf("%d\n",i);
}

printf("\n");
i=i-1;
j=-i;


while (j<=0)                                 //! ||= OR | && = AND | ! = NOT for exmple you can type j<=0&& j>-10
{
 printf("%d\n",j);   
 j=j+1;
}

do                                //do while loops will executes a block of code once then check condition if it it true
{
 k=k+1 ;  
 printf("k=%d\t",k);
} while (k<i);
printf("\n");
                                //continue= Skips rest of code and force the next part of the loop
                                //break= Exits a switch/loop
for(i=1;i<=10;i++)
{
  if(i==5){continue;}       //this will make the for statement skip when i== 5
printf("\tcontinue i=%d",i);
}
//
printf("\n");
//
for(i=1;i<=10;i++)
{
  if(i==5){break;}       //this will make the for statement stop when i== 5
printf("\tbreak i=%d",i);
}                     





    return 0;
}
#include <stdio.h>
                     //ToDo                Bitwise operatiors
int main()
{
   // & = AND
   // | = OR
   // ^ = XOR
   // << = LEFT SHIFT
   // >> = RIGHT SHIFT
int x=6;                                 // 6=00000110
int y=12;                                //12=00001100
int z=0;                                 // 0=00000000

      z=x&y;                             // 4=00000100
      printf("AND=%d\n",z);
      z=x|y;                             //14=00001110
      printf("OR=%d\n",z);
      z=x^y;                             //10=00001010
      printf("XOR=%d\n",z);
      z=x<< 1;                           //12=00001100
      printf("LEFT SHIFT=%d\n",z);
      z=x>> 1;                           // 3=00000011
      printf("RIGHT SHIFT=%d\n",z);
    return 0;
}
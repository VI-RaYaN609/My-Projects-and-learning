#include <stdio.h>
#include <string.h>

int main()
{   
    // memory= an array of bytes within ram (street)
    // memory block= a single unit(1 byte) within a memory ,(house)
    // adress = is the location of a memory block inside the memory(house adress)
    // %p to show the adress of a variable 
    
    // int Age=18;
    // printf("adress of Age is:\n%p\n",&Age);
    
    // pointer =  a variables like reference that hold a memory adress of another variable
    //     *   =  indirection operator (value at adress)

    double age=18;
    double *pAge=&age;
    char name[5]="rayan";                // for a single character     =   *pChar=&char;
    char (*pName)[5]=&name;              // for an array (characters or Numbers) =  (*pString)[]=&string;
    

    printf("%p\t",pAge);      // pAge will show the adress of the variable age
    printf("%lf\n",*pAge);     // *pAge will show the variable age
  
    printf("Value of PName       : %s \t",*pName);              // * derefrence (*pName=name )
    printf("Adress of pName(hex) : %p \t",pName);              //%p show variable (address) in Hex(0123456789ABCDEF)
    printf("Adress of pName(dec) : %d\t",pName);               // this will show address in dec
    printf("Size of pName        : %d bytes\t",sizeof(pName));
    printf("ACTUAL address of pName(hex):%p\n",&pName);

    printf("Value of name        : %s \t",name);
    printf("Address of name(hex) : %p \t",&name);
    printf("Adress of name (dec) : %d\t",&name);
    printf("Size of name         : %d bytes\t",sizeof(name));
    printf("ACTUAL address of pName(dec):%d",&pName);
    return 0;
}
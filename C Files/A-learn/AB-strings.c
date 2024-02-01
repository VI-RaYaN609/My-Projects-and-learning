#include <stdio.h>
#include <string.h>   //? you need to type this to use strings

int main(){


char name[]="nibou";
char name2[]="rayan";

// strlwr(name);                                     // convert "name" to lower cases
// strupr(name);                                     // convert "name" to upper cases


// strcat(name,name2);                               // will write "name2" to the end of "name" without space
// strncat(name,name2, 1);                           //will write n from the start of "name2" to the end of "name"


// strcpy(name,name2);                               //copy "name" to "name2"
// strncpy(name,name2, 2);                           // copy n characters of "name2" to "name"


//strset(name, '?');                                 //set all characters of "name " to '  '
//strnset(name, '?', 1);                             //set n characters of "name" to '  '
//strrev(name);                                      //reverse (name)

printf("%s\n",name);

// int result= strlen(name);                         //this will make result= number of characters in "strlen(name)"

//int result= strcmp(name,name2);                 //this will compare "name" and "name2" if they are the same result = 0
//int result= strncmp(name,name2, 1);             //this will compare n characters from name and name2 (right to left)
//int result= strcmpi(name,name2);                // same as strcmp but ignore cases
//int result= strnicmp(name,name2,1)              // same as strncmp but ignore cases

// printf("%d",result);




}
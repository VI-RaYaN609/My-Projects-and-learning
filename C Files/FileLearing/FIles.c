#include <stdio.h>

//ToDo                                     WRITE/APPEND FILE    
            
// int main ()
// {        // w For write(erase and write) |r For read | a For append (write without erase)
    
//     FILE *pF  = fopen("C:\\Users\\VI RaYaN\\Desktop\\VS Code\\C Files\\FileLearing\\test.txt","a");    
           
//     if(pF==NULL)
//     {
//         printf("Unable to open File!");
//     }
//     else
//     {
//     printf("File open successefully\n");
//     fprintf(pF,"\n ************************\n");
//     int j ;
//     for(j=1;j<=5;j++){fprintf(pF,"j= %d\t",j);}
    
//                 fclose(pF);                      // Close File  //! (NEVER PUT * IN FCLOSE)
//     }
//     return 0;
// }

//!                                          READ FILE

// int main()
// {
//     FILE *pF = fopen("C:\\Users\\VI RaYaN\\Desktop\\VS code\\C Files\\FileLearing\\test.txt","r");
   
//     char line[255];
   
//     if(pF == NULL) 
//     {
//         printf("Unable to open File!!");
//     }
//     else{

//      while(fgets(line,255,pF)!= NULL){
//       printf("%s",line);
//       }

//     }
//               fclose(pF);                             //NEVER PUT '*' IN FCLOSE
//     return 0;
// }

//!                                         remove Files

// int main()
// {
//   FILE *pF="test.txt";
//   if(remove("test.txt")==0){printf("File Deleted Successefully");}else{printf("File Not found");}
//   return 0;
// }
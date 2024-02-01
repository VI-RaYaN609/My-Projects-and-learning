#include<stdio.h>
#include<string.h>

int main()
{                                //!array print|scan loop


  // int i,j; 
  // double tab[]={1,2,3,4,5,6,7,8} ;      
  // int rows=sizeof(tab)/sizeof(tab[1]) ;    // this will calculate number of numbers in tab
  
  //     printf("rows=%d\n",rows);
  //    for(i=0;i<rows;i++)
  //    {
  //      printf("give me a number for the table %d\n",i);
  //      scanf("%d",& j) ;
  //      tab[i]=j;
  //    }
  //    for(i=0;i<rows;i++)
  //    {
  //      printf(" %1lf\t",tab[i]); 
  //    }
                           
                           
                             //ToDo 2D array (array which each one of its elements is an array)
                                                            //   {
                                                            //     {1,2,3},          you cant type like 1D array
                            //  int array[2][3];            // =   {6,5,4}          you need to type inside the brackets
                                                            //     };     
                                                           //sizeof(array)= size of array in bytes                                   
                                                  //!2D array print


//    //Variables declaration 
//     int array [2][3];                             
//     int rows=sizeof(array)/sizeof(array[0]) ;                
//     int columns=sizeof(array[0])/sizeof(array[0][0]) ;

// //Display of rows and columns
//     printf("rows= %d\n",rows);
//     printf("columns= %d\n",columns);

// //array values:
//     array[0][0]=1;
//     array[0][1]=2;
//     array[0][2]=3;
//     array[1][0]=4;
//     array[1][1]=5;
//     array[1][2]=6;

//     for(int i=0;i<rows ;i++)
//     {
//       for(int j=0;j<columns ;j++)
//       {
//         printf("%d\t",array[i][j]);
//       } 
//       printf("\n");
//     }                       


                                             //ToDo
                                             //! array of strings


//  char drinks[][10/*max size per element(10 character)*/]={"cola","pepsi","sprite"};
//    // drinks[0]="7up";
//    for(int i=0;i<sizeof(drinks)/sizeof(drinks[0]);i++)
//     {
//       printf("%s\n",drinks[i]); 
//     }
   
//    printf("\n");
//    strcpy(drinks[0],"7up");   

//     for(int i=0;i<sizeof(drinks)/sizeof(drinks[0]);i++)
//     {
//       printf("%s\n",drinks[i]); 
//     }


                                             //Todo
return 0;
}
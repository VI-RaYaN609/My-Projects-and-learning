// write an alogirth that can calculate a table max value and min value and the some and then sort it and print it again
#include<stdio.h>


void scantable(int t[4],int i,int size)
{
  for(i=1;i<=size;i++){
      printf("give me value for Tab[%d]\n",i);
      scanf("%d",&t[i]);
  }
}
void printtable(int t[],int i,int size){
for(i=1;i<=size;i++){
      printf("Tab[%d]=%d\n",i,t[i]);
  }
}
int main()
{
 int max,min,somme;
 int i,j,n;
 
 printf("Give Me Table size **5 is most optimal**\n");
 scanf("%d",&n);
 
 int t[n];
 int size=sizeof(t)/sizeof(t[1]);
 int (*pT)[n]=&t;

  scantable(t,i,size);

    max=t[1];
    min=t[1];
     
     for(i=1;i<=size;i++){
        if(max<t[i]){max=t[i];}
     }
     for(i=1;i<=size;i++){
        if(min>t[i]){min=t[i];}
     }
     somme=t[1];
     for(i=1;i<=size;i++){
        somme=somme+t[i];
     }
    
      printf("max=%d\t,min=%d\t,somme=%d\n",max,min,somme);

      printf("T is:");
      printtable(t,i,size);
      printf("\n\n");
                                         //sorting the array
     for(i=1;i<=size-1;i++){
        for(j=1;j<=size-1;j++){
           if(t[j]>t[j+1]){
             int temp=t[j];
             t[j]=t[j+1];
             t[j+1]=temp; 
           }
        }
     }
    printf("Size of T = %d Bytes\n",sizeof(t));
    printf("address of T is:\t%p\n",pT);
     printf("Sorting table T.....\n T is:\n");
    printtable(t,i,size);

return 0 ;
}
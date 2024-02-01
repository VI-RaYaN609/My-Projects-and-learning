#include<stdio.h>

//struct= reserver multiple 
//typedef= reserve keyword that give an existing datatype a nickname

// struct
struct user
{
char player[25];
char password[25];
int score;
};

//TODO typedef
typedef char player[25];


//! typedef struct
typedef struct {
char Player[25];
char Password[25];
int Score;
}/*nickname here*/USER;

//? array of structs
struct STUDENTS{
  char name;
  double moyenne;
};

int main(){
  //
  struct user user1 = {"rayan","password",125};
  struct user user2 = {"nibou","password",512};
  
  printf("%s\t",user1.player);
  printf("%s\t",user1.password);
  printf("%d\n\n",user1.score);
  
  
  //ToDO
  player player1; 
  player player2;
  printf("give me your name Player 1\n");
  scanf("%s",&player1);
  printf("give me your name Player 2\n");
  scanf("%s",&player2);
  printf("Hello %s %s\n\n",player1,player2);
  //!

  USER Player1={"Dumb","pass",431};
  USER Player2={"stupid","pass",134};
  printf("%s\t%s\t%d\n",Player1.Player,Player1.Password,Player1.Score);
  printf("%s\t%s\t%d",Player2.Player,Player2.Password,Player2.Score);

  //?

  struct STUDENTS students[5];

 int size=sizeof(students)/sizeof(students[0]);
 printf("size is  %s",size);

  for(int i=0;i<=size;i++){
    printf("\ngive me name and moy \n");
    scanf("%s ",&students->name);
    scanf("%lf",&students->moyenne);
  }
  for(int i=0;i<=size;i++){
    printf("%s\t%lf \n",students->name,students->moyenne);
  }
    return 0;
}

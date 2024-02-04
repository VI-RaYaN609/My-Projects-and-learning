from var import*
import time

class Task_information:
    Task_title = str()
    Task_description =str() 
    Task_DueDate = str()
    def Task_create(self):
        self.Task_title = input("Title :").upper()
        self.Task_description = input("Description :\n")
        self.Task_DueDate  = input("Due Date:")

def Quit():
    return False

def Task_make():
    Task = Task_information
    Task.Task_create(self=Task)
    return Task

def ID_Maker():
   if Tasks == dict(): 
    ID=1
    with open("Taskes.txt","r")as file:
     for line in file : 
        ID+=1
     ID =(ID-1)//5 +1  
     
   else :
     keys= list(Tasks.keys())
     keys.reverse()
     ID=keys[0]+1
   return ID

def print_file():
    print("Printing All Taskes",end="")
    print_workingdot(0.75)        
    with open("Taskes.txt","r") as file:
       for line in file :
          print(line,end="")

def Tasks_number():
    i=0
    with open("Taskes.txt","r") as file:   
     for line in file:i+=1
    tasks_available=i/5
    return tasks_available

def Task_Search_Type():
   while True:
    Checker=["title","id","date","due","duedate","due date"]
    Search_type=input("you want to know by (ID,Title,DueDate)? : ").lower()
    if Search_type in Checker:
        break
    else:
       print("Please enter (ID,Title,DueDate)")
   return Search_type

def Task_Search_Type_Title():
   title_view_state=False
   while not title_view_state: 
    title_view=input("Enter the title: ").upper()
    check='  Title: {}\n'.format(title_view)
    with open("Taskes.txt","r") as file:
      LINE=0
      for line in file:
        if line ==check :
          title_view_state=True
          break                     
        LINE+=1
      if not title_view_state:
         print("Searching for Task",end="")
         print_workingdot(0.5)
         print("error 404,Task with the Title not found, Try Again ")
   return LINE      

def Task_Search_Type_ID():
  Line_Found=False
  while not Line_Found:       #this will get the first line of the task 
   ID_input=int(input("Enter task number (ID) : "))
   check ="ID: "+str(ID_input)+" {\n"
   LINE=0

   with open("Taskes.txt","r") as file:
       for line in file:
        LINE+=1
        if line==check:
          Line_Found =True
          break
   if not Line_Found:
      print("Task with an ID of {} was not Found\nPlease enter a valid ID".format(ID_input))

  return LINE

def Task_print(LINE):
   print("Searching For The Task",end="")
   print_workingdot(0.5)
   print("Task Found printing",end="")
   print_workingdot(0.25)
   i=0
   counter=0
   correctline=False
   with open("Taskes.txt","r") as file:
      for line in file :
        i+=1
        if i==LINE:
           correctline=True
        if correctline and counter<5:
          print(line,end="");counter+=1  


def print_workingdot(x):
   print(".",end="");time.sleep(x)
   print(".",end="");time.sleep(x)
   print(".",end="");time.sleep(x)
   print(".")

Tasks = dict()
Tasks_save= dict()


print("Hello This is a Task Tracker")
while running :
  
  while True :  
   
   #userinput checker
    while True :
       userinput = input("Enter action (Add,view,remove,update,save): ").lower()
       input_found = False
       
       for row in user_input:
          if userinput in row:
             input_found = True
             break
       if input_found:
          break 
       else :
          print("Please enter a valid action")


    #Quit
    if userinput =="quit":
        running=Quit()
        break

    #add-task code
    if userinput in add_task:
        task=Task_make()
        ID = ID_Maker()
        print("Loading Information",end="")
        print_workingdot(0.7)
        print("Loading Succesfull!!")
        Tasks.update({ID:task})
        Tasks_save.update({ID:task})                   #This is so when i save tasks doesnt save more than one
        print("")

    #view-task code
    if userinput in view_task:

        #View all tasks
        if userinput in view_alltasks:  
            print_file()
            print("")
        #view A task of choice
        elif userinput in view_singletask:
            
            Search_type=Task_Search_Type() #Task searcher type
             
            if Search_type in ("title"):   #Title search-type
               LINE=Task_Search_Type_Title()  
             
            elif Search_type in ("id"):    #ID search-type
               LINE=Task_Search_Type_ID()
            
            #Task printing 
            Task_print(LINE)
            print("")

    #remove-task code
    if userinput in remove_task:
        #Task searcher type
        Search_type = Task_Search_Type()

        #Title search-type
        if Search_type in ("title"):
           LINE=Task_Search_Type_Title()

        elif Search_type in ("id"):
           LINE = Task_Search_Type_ID()
        
        print("Removing Task",end="")
        print_workingdot(1)
        with open("Taskes.txt","r") as file:
           File_lines=file.readlines()
        File_lines.pop(LINE+3)
        File_lines.pop(LINE+2)
        File_lines.pop(LINE+1)   
        File_lines.pop(LINE)   
        File_lines.pop(LINE-1)   
        with open("Taskes.txt","w") as file:
           for line in File_lines:
              file.write(line)   
        print("Removing Succesfull!",end="\n\n")
    
    #update-task code
    if userinput in update_task:
        #Task searcher type
        Search_type = Task_Search_Type()

        #Title search-type
        if Search_type in ("title"):
           LINE=Task_Search_Type_Title()

        elif Search_type in ("id"):
           LINE = Task_Search_Type_ID()

        with open("Taskes.txt","r") as file:
           File_lines=file.readlines()
        print("Please enter the new information for the task")
        updated_task=Task_make()
        print("Updating Task",end="")    
        print_workingdot(0.5)
        File_lines[LINE]='  Title: {}\n'.format(updated_task.Task_title)
        File_lines[LINE+1]=' Description: {}\n'.format(updated_task.Task_description)
        File_lines[LINE+2]=' Due Date: '+updated_task.Task_DueDate+'}\n'
        with open("Taskes.txt","w") as file:
           for line in File_lines:
              file.write(line)
        print("Updating Succesfull !!",end="\n\n")      

    #save-task code
    if userinput in save_task :
       
       save_succes=False
       with open("Taskes.txt","a") as file :
          index=0
          IDS=list(Tasks_save.keys())
          for line in Tasks_save.items() :
            file.write("ID: "+str(IDS[index])+" {\n  Title: "+task.Task_title+"\n Description: "+task.Task_description+"\n Due Date: "+task.Task_DueDate+"}\n\n")
            index+=1
            save_succes=True

          if save_succes:
             print("Saving",end="")
             print_workingdot(1)
             print("Save Successfull",end="\n\n")
             Tasks_save=dict()           #clean save dictionary so tasks doesnt save more than once
          else:
             print("Saving Unseccesfull",end="\n\n")   


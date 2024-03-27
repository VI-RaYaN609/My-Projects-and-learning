#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

class Task {
    public:
       string desc;
       bool completed;
       
       Task(string desc){
        this->desc = desc;
        this->completed = false;
       }
};
class Todo {
    public :
        vector<Task> tasks;
        
        Todo(){
            loadTask();
        }

        void addTask(){
            string desc ;
            cout << "Enter Description : ";
            cin >> desc;
            tasks.push_back(Task(desc));
            cout << "Task added successfully";
        }
        void removeTask(){
            int i; 
            cout << "Enter number of task you wish to delete : ";
            cin >> i ;
            if( i-1 < tasks.size()){
                tasks.erase(tasks.begin() + i);
                cout << "Task deleted successfully";
            }
            else {
                cout << "Index out of range";
            }
        }
        void markTask(){
            this->viewTasks();
            int i ; 
            cout << "Enter number of task you wish to Mark :";
            cin >> i ;
            if( i-1 < tasks.size()){
                if ( tasks[i-1].completed){
                    tasks[i-1].completed = false;
                    cout << "Task marked as not completed";
                }
                else{
                    tasks[i-1].completed = true;
                    cout << "Task marked as completed";
                }
            }
            else {
                cout << "Index out of range";
            }
        }
        void viewTasks(){
            cout << "Tasks :" << endl;
            for (int i = 0; i < tasks.size(); i++){
                cout << i+1 << ". " << (tasks[i].completed ? "[Completed] " : "[ ] ") << tasks[i].desc << endl;
            }
        }
        void saveTask(){
            ofstream file("task.txt");
            if ( file.is_open()){
                for (int i = 0 ; i <tasks.size();i++){
                    file << tasks[i].desc << "," << tasks[i].completed << endl ;
                }
            }
        }
        void loadTask(){
            ifstream file("task.txt");
            if ( file.is_open()){
                string line ;
                while ( getline(file , line )){
                    int index = line.find(",");
                    string desc = line.substr(0, index);
                    bool completed = line.substr(index+1) == "1" ;

                    tasks.push_back(Task(desc));
                    if(completed){
                        tasks.back().completed = true;
                    }
                }
                cout << "Tasks Loaded " << endl;
            }
        }

};

int main(){
    Todo todo ;

    cout << "Welcome To this basic TodoListManager!" << endl;
    while (1){
        cout << "1. Add a new task" << endl;
        cout << "2. Delete a task" << endl;
        cout << "3. Mark Task " << endl;
        cout << "4. View tasks" << endl;
        cout << "5. Save Tasks" << endl;
        cout << "6. Exit" << endl;
        int choice ;
        do{
            cout << "Enter your choice : ";
            cin >> choice;
        }while(choice <1 || choice > 6);
        cout << "****************************************************************"<<endl;

        switch(choice) {
            case 1:{
                todo.addTask(); 
                break;
            }
            case 2:{
                todo.removeTask();
                break;
            }
            case 3:{
                todo.markTask();
                break;
            }
            case 4:{
                todo.viewTasks();
                break;
            }
            case 5:{
                todo.saveTask();
                break;
            }
            case 6:{
                return 0;
                break;
            }
        }
        choice = 0;
        cout << "****************************************************************"<<endl;
    }
}
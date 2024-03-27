#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <limits>
#include <cctype>

using namespace std;

class Book{
    public:
       string title;
       string author;
       string genre;
       int ISBN;
       int price;

       Book(string title, string author, string genre, int ISBN, int price){
        this->title = title;
        this->author = author;
        this->genre = genre;
        this->ISBN = ISBN;
        this->price = price;
       }


};

bool IsInputNumber(string input){
    for (int i = 0; i < input.size(); i++){
        if (!isdigit(input[i])){
            return false;
        }
    }
    return true;
}

int getStringIndex(const vector<Book>& books,string input){
    bool found = false;
    for (char &c : input){c = tolower(c);}
    for (int i = 0 ; i < books.size(); i++){
        string title = books[i].title;
        string author = books[i].author;
        for (char &c : title) {c = tolower(c);}
        for (char &c : author) {c = tolower(c);}
        if (input == title|| input == author){
            found = true;
            return i;
        }
    }
    if (!found){
        cout << "Book not found with specified information" << endl;
        return -1;
    } 
}



void addBook(vector<Book> &books){
    string title , author , genre;
    int ISBN , price;
    cout << "Enter title: ";
    getline(cin, title);
    cout << "Enter author: ";
    getline(cin, author);
    cout << "Enter genre: ";
    getline(cin, genre);
    cout << "Enter ISBN: ";
    while (!(cin >> ISBN)) {
    cout << "Invalid input. Please enter a valid integer for ISBN: ";
    cin.clear(); // Clear error flags
    cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Discard invalid input
    }
    cout << "Enter price: ";
    while (!(cin >> price)) {
    cout << "Invalid input. Please enter a valid integer for ISBN: ";
    cin.clear(); // Clear error flags
    cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Discard invalid input
    }
    cout << endl;
    Book book(title, author, genre,ISBN, price);
    books.push_back(book);
    cout << "Book added Successfully ." << endl;
}
void removeBook(vector<Book> &books){
    cout << "Enter Book Number: ";
    int index;
    cin >> index;
    if (index < 1 || index > books.size()){
        cout << "Invalid Book Number" << endl;
        return;
    }
    else {
    cout << endl;
    books.erase(books.begin() + index-1);
    cout << "Book removed Successfully ." << endl;
    }
}
void searchBooks(const vector<Book> &books){
    cout << "Enter Book Number/title/author: ";
    string input;
    getline(cin , input);
    cout << endl;
    bool isNumber = IsInputNumber(input);
    int index;
    if(!isNumber ) {
        index = getStringIndex(books, input);
        if (index == -1){
            cout << "Book not found with specified information" << endl;
            return;
        }
    }
    else {
        index = stoi(input) -1;
        if(index < 0 ||index > books.size() -1){
        cout << "Invalid Book Number" << endl;
        return ;
        }
    
    }
    
    cout << "Title: " << books[index].title << endl;
    cout << "Author: " << books[index].author << endl;
    cout << "Genre: " << books[index].genre << endl;
    cout << "ISBN: " << books[index].ISBN << endl;
    cout << "Price: " << books[index].price << endl;
    cout << endl;
}
void displayBooks(const vector<Book> &books){
    cout << "Library Books ("<<books.size()<<") :"<<endl;
    for( int i=0 ; i < books.size() ; i++){
        cout << i+1<<". Title: " << books[i].title << endl;
        cout << "   Author: " << books[i].author << endl;
        cout << "   Genre: " << books[i].genre << endl;
        cout << "   ISBN: " << books[i].ISBN << endl;
        cout << "   Price: " << books[i].price << " Da\n" << endl;
    }
}
void saveBooks(const vector<Book> &books){
    ofstream file("books.txt");
    if ( file.is_open() ){
        for ( int i = 0 ; i < books.size() ; i++ ){
            file <<books[i].title << ";" << books[i].author << ";" << books[i].genre << ";" << books[i].ISBN << ";" << books[i].price << endl;
        }
        cout << "Books Saved successfully." << endl;
    }
    else {
        cout << "Unable to open file. (books.txt)" << endl;
    }
}
void loadBooks(vector<Book> &books){
    ifstream file("books.txt");
    if ( file.is_open()){
        string line,bookinformation[5];
        int pos;
        while ( getline(file , line) ){
            int i = 0;
            while(i < 5){
                pos = line.find(";");
                bookinformation[i] = line.substr(0,pos);
                line = line.substr(pos+1);
                i++;
            }
            Book book(bookinformation[0],bookinformation[1],bookinformation[2],stoi(bookinformation[3]),stoi(bookinformation[4]));
            books.push_back(book);

        }
        cout << "Books Loaded successfully." << endl;
    }
    else {
        cout << "Unable to open file. (books.txt)" << endl;
    }
}
int main(){
    
    vector<Book> books;
    loadBooks(books);

    cout << "Welcome to Simple Library Management System" << endl;
    while(1){
        cout << "1. Add Book" << endl;
        cout << "2. Remove Book" << endl;
        cout << "3. Search Book" << endl;
        cout << "4. Display Books" << endl;
        cout << "5. Save Books" << endl;
        cout << "6. Exit \n" << endl;
        int option,i;
        do{
          cout << "Enter Option : ";
          cin >> option;
          cin.ignore();
          if(option <1 || option >6){cout << "option Entered must be between 0 and 6" <<endl;}
        }while(option <1 || option >6);
        
        cout << "****************************************************************" << endl;
        switch(option){
            case 1:{
                addBook(books);
                break;
            }
            case 2:{
                removeBook(books);
                break;
            }
            case 3:{
                searchBooks(books);
                break;
            }
            case 4:{
                displayBooks(books);
                break;
            }
            case 5:{
                saveBooks(books);
                break;
            }
            case 6:
                return 0;
        }
        cout << "****************************************************************" << endl;
    }
}
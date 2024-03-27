#include <string>
#include <iostream>
#include <fstream>

using namespace std;

int main(){
    ifstream file("books.txt");
    if( file.is_open() ){
        string line,title,author,genre;
        int pos,price,ISBN;
        while ( getline(file , line) ){
            int i  = 0;
            while(i < 5){
                pos = line.find(";");
                cout << line << "  " << pos << endl;
                title = line.substr(0,pos);
                line = line.substr(pos+1);
                i++;
            }

        }
    }

    return 0;
}
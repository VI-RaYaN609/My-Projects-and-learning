#include <string>
#include <iostream>
#include <fstream>

using namespace std;

int main(){
    ifstream file("books.txt");
    if( file.is_open() ){
        string line,information[5];
        int pos;
        while ( getline(file , line) ){
            int i  = 0;
            while(i < 5){
                pos = line.find(";");
                cout << line << "  " << pos << endl;
                information[i] = line.substr(0,pos);
                line = line.substr(pos+1);
                i++;
            }
        }
    }
    return 0;
}

#include <iostream> 
#include <string> 

using namespace std; 

int main() 
{ 
    string word1, word2; 
    cout << "Please enter a word: "; 
//    cin >> word1; 
	getline(cin,word1); 	
    cout << "Please enter a word: "; 
//    cin >> word2; 
	getline(cin,word2);
    
    int word1Length, word2Length;
    word1Length = word1.length(); 
    word2Length = word2.length(); 
    
    if (word1Length > word2Length) 
    {
        cout << " " << word1 << " is longer than " << word2 << endl;
    }//end (word1Lenght > word2Length) 
    
    if (word2Length > word1Length) 
    {
        cout << word2 << " is longer than " << word1 << endl;
    }//end (word2Lenght > word1Length) 

    if (word2Length == word1Length) 
    {
        cout << word2 << " and " <<  word1 << " are the same length" <<  endl;
    }//end (word2Lenght == word1Length) 

    return 0;
}//end main() 

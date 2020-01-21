#include <iostream> 
#include <string> 
#include <vector> 
#include <algorithm> //for sort and count 

using namespace std; 

int main() 
{ 
	vector<double> vDouble; 
	for (int i=0; i<10; i++)
	{
		vDouble.push_back(i); 
	}//end (int i=0; i<10; i++) 

	//Printing Vector Content 
	for (auto item:vDouble) //for loop in python; think about range
	{ 
		cout << item << " ";  
	}//end (auto item:vDouble)  
	cout << endl; 

	for (unsigned int i=0; i<vDouble.size(); i++) 
	{ 
		cout << vDouble[i] << " "; 
	}//end (unsigned int i=0; i<vDouble; i++) 
	cout << endl; 

	for (auto i=begin(vDouble); i!=end(vDouble); i++) 
	{ 
		cout << *i << " "; 
	}//end (auto i=begin(vDouble); i!=end(vDouble); i++)
	cout << endl; 

	//String Problem 	
	vector<string> strVector; 
	cout << "Enter three words: "; 
	for (int i=0; i<3; i++) 
	{ 
		string strElement; 
		cin >> strElement; 
		strVector.push_back(strElement); 
	}//end (int i=0; i<3; i++)

	for (auto item:strVector) 
	{ 
		cout << item << " "; 
	}//end (auto item:strVector) 
	cout << endl; 

	sort(begin(strVector), end(strVector));
	for (auto item:strVector) 
	{ 
		cout << item << " ";
	}//end (auto item:strVector) 
	cout << endl; 	

	int thress = count(begin(vDouble), end(vDouble), 3); 
	cout << "Vector of doubles has " << thress << " elements" << endl; 

	int tees = count(begin(strVector[0]), end(strVector[0]), 't'); 
	cout << "First word has " << tees << " letter t's" << endl;  
	
}//end main 

#include <iostream> 
#include <string> 
#include "main.hpp"

using namespace std; 


int main()
{
	auto a = add(3,4); 
	cout << "3 + 4 = " << a << endl; 
	double b = add(1.3, 2.1, 5); 
	cout << "1.3 + 2.1 + 5 = " << b << endl; 
	auto c = add(add(1,2),add(1.3,3,4),2);
	cout << "1 + 2 + 1.3 + 2 + 3 + 4 = " << c << endl; 
	return 0;
} 



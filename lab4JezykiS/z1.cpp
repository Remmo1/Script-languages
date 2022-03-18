#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <numeric>

int main(int argc, char* argv[])
{
	std :: string line;
	std :: vector<int> input;
	
	while (std :: getline(std :: cin, line))
	{
		int actual = 0;
		try 
		{
			actual = std :: stoi (line);
			input.push_back(actual);
		}
		catch (...) {}
	}
	
	int sum = std :: accumulate (input.cbegin(), input.cend(), 0, [](int acc, int x){return acc + x;});
	printf("Sum is: %d\n", sum);
	return sum;
}

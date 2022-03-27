#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <cstdlib>

int checkErrorAndShow(std :: vector<std :: string>& input, char* argv[], int Nposition, bool isS)
{
	std :: string help = argv[Nposition];
	int numberOfLines = stoi(help);
	int lineDiff = input.size() - numberOfLines;
	if (lineDiff < 0 && !isS)
	{
		std :: cout << "braklo: " + std :: to_string( (-1) * lineDiff ) + " linii do wypisania" << std :: endl;
		return 2;
	}
	else if (lineDiff < 0 && isS)
		return 2;
	
	for (int i = 0; i < numberOfLines; i++)
		std :: cout << input[i] << std :: endl;
	
	return 0;
}

int main(int argc, char* argv[])
{
	
	std :: string line;
	std :: vector<std :: string> input;
	
	while (std :: getline(std :: cin, line))
		input.push_back(line);
	
	if (std::count(input.begin(), input.end(), "/S"))
		return checkErrorAndShow(input, argv, 2, true);
	else 
		return checkErrorAndShow(input, argv, 1, false);
	
}
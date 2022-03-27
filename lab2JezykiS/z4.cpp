#include <iostream>
#include <cstdlib>
#include <string>
#include <unordered_map>
#include <algorithm>
#include <vector>
#include <sstream>

using std :: cout;
using std :: endl;
using std :: string;
using std :: vector;

typedef std::unordered_map<string, int> Mymap;

vector<string> foundedParts(vector<string> arguments, string fromUser)
{
	vector<string> result;
	for (int i = 0; i < arguments.size(); i++) 
	{
		if (fromUser.find(arguments[i]) != string::npos)
			result.push_back(arguments[i]);
	}
	
	return result;
}


int main(int argc, char* argv[])
{
	Mymap parts;
    parts.insert(Mymap::value_type("zderzak", 1));
    parts.insert(Mymap::value_type("drzwi", 2));
    parts.insert(Mymap::value_type("opona", 4));
    parts.insert(Mymap::value_type("swiatla", 8));
    parts.insert(Mymap::value_type("skrzynia_biegow", 16));
    parts.insert(Mymap::value_type("hamulce", 32));
    parts.insert(Mymap::value_type("silnik", 64));

    int returnCode = 0;
	
	vector<string> arguments;
	for (int i = 0; i < argc; i++)
		arguments.push_back(argv[i]);
	
	
	if (argc == 0 || argc > 7)
		return(returnCode);
	
	string input;
	std::getline(std::cin, input);
	
	vector<string> result = foundedParts(arguments, input);
	
    for (int i = 0; i < result.size(); i++)
    {
		string s = result[i];
		std::transform(s.begin(), s.end(), s.begin(), ::tolower);
        Mymap::iterator it = parts.find(s);

        if (it != parts.end())
            returnCode += it->second;
            
    }

	printf("Returning: %d\n", returnCode);
    return(returnCode);
}

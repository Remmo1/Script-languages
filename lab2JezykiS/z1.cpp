#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <cstdlib>

using std::string;
using std::vector;

int main(int argc, char* argv[]) 
{
	
    vector<string> clargs;
    for (int i = 0; i < argc; i++)
        clargs.push_back(argv[i]);
    

    const char *tmp = std::getenv("PATH");
    std::string env_var(tmp ? tmp : "");
    if (env_var.empty())
       return 0;
    
    vector<string> paths;
    std::stringstream env_p(env_var);
    string segment;

    while (std::getline(env_p, segment, ':')) 
        paths.push_back(segment);
	
    std::sort(paths.begin(), paths.end());

    
    if (std::count(clargs.begin(), clargs.end(), "/D"))
    {    
        vector<string> paths_contains;
        for (auto it = paths.begin(); it != paths.end(); ++it) {
            auto current = *it;
            if (std::count(paths_contains.begin(), paths_contains.end(), current)) 
                std::cout << ":" << *it << "	[DUPLICATED]\n";
            else {
                paths_contains.push_back(*it);
                std::cout << ":" << *it << "\n";
            }
            
        }
    } 
	else if (std::count(clargs.begin(), clargs.end(), "/B"))
	{
        for (auto it = paths.begin(); it != paths.end(); ++it) {
            auto current = *it;
            if (current == "") 
                std::cout << ":" << *it << "	[BRAK]\n";
			else 
				std::cout << ":" << *it << "\n";
         
        }
	}
	else 
    {
        for (auto it = paths.begin(); it != paths.end(); ++it) 
            std::cout << ":" << *it << "\n";
    }
    return 0;
}

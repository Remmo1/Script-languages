#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <cstdlib>

int main(int argc, char* argv[]) 
{
	
    std::vector<std::string> clargs;
    for (int count{ 0 }; count < argc; ++count)
    {
        clargs.push_back(argv[count]);
    }

    //get sysenv PATH
    const char *tmp = std::getenv("PATH");
    std::string env_var(tmp ? tmp : "");
    if (env_var.empty()) {
       return 0;
    }
    //split paths and sort lexicographically
    std::vector<std::string> paths;
    std::stringstream env_p(env_var);
    std::string segment;

    while (std::getline(env_p, segment, ':')) {
        paths.push_back(segment);
    }
    std::sort(paths.begin(), paths.end());

    // print paths, if flag "/D" is present add [DUPLICATED] postfix
    // for duplicated items
    
    if (std::count(clargs.begin(), clargs.end(), "/D"))
    {    
        std::vector<std::string> paths_contains;
        for (auto it = paths.begin(); it != paths.end(); ++it) {
            auto current = *it;
            if (std::count(paths_contains.begin(), paths_contains.end(), current)) {
                std::cout << ":" << *it << " [DUPLICATED]\n";
            } else {
                paths_contains.push_back(*it);
                std::cout << ":" << *it << "\n";
            }
            
        }
    } else 
    {
        for (auto it = paths.begin(); it != paths.end(); ++it) {
            std::cout << ":" << *it << "\n";
        }
    }
    return 0;
}

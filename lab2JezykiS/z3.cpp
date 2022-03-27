#include <iostream>
#include <string>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <sstream>

using std::string;
using std::cout;
using std::endl;
using std::vector;


void findInEnvinroment(int argc, char* argv[], char* env[], vector<string>& argumentsV, vector<string>& envVariablesV, bool& quiet)
{
    string actualVariable;
    string actualArgument;

    while (*env != NULL)
    {
        actualVariable = *env;
        for (int i = 0; i < argc; i++)
        {
            actualArgument = argv[i];
            if (actualVariable.find(actualArgument) != string::npos)
            {
                argumentsV.push_back(actualArgument);
                envVariablesV.push_back(actualVariable);
            }
			if (actualArgument == "/S")
				quiet = true;
        }

        *env++;
    }
}

void splitBySrednik(string& value)
{
    // potrzebne do splitowania
    string line;
    const char separator = ';';
    vector<string> outputArray;
    string val;

    // splitujemy po sredniku
    std::stringstream streamData(value);
    while (std::getline(streamData, val, separator))
        outputArray.push_back(val);

    value = outputArray[0] + "\n";
    for (int i = 1; i < outputArray.size(); i++)
        value += ("  " + outputArray[i] + "\n");
}

int main(int argc, char* argv[], char* env[])
{
    vector<string> argumentsV;
    vector<string> envVariablesV;
	bool quiet = false;

    findInEnvinroment(argc, argv, env, argumentsV, envVariablesV, quiet);

    std::sort(argumentsV.begin(), argumentsV.end(), std::greater<string>());
    std::sort(envVariablesV.begin(), envVariablesV.end(), std::greater<string>());

    if (quiet)
        return 0;
	else if (envVariablesV.empty())
	{
		string a = argv[1];
		string help = a + " = NONE";
		char* output = &help[0];
		puts(output);
	}
    else
    {
        for (int i = 0; i < argumentsV.size(); i++)
        {
            puts(argumentsV[i].c_str());
            puts("=");

            if (envVariablesV[i].find(';'))
                splitBySrednik(envVariablesV[i]);

            puts(envVariablesV[i].c_str());
            puts("\n");
        }
    }
}

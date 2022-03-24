#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <vector>
#include <sstream>
#include <bits/stdc++.h>

using std :: string;
using std :: cout;
using std :: endl;

int splitBySpaceAndGetNumber(string s)
{
    const char separator = ' ';

    std::vector <string> outputArray;
    std::stringstream streamData(s);
    std::string val;
    while (std::getline(streamData, val, separator)) {
        outputArray.push_back(val);
    }

    int ret = std::stoi(outputArray[0]);
    outputArray.clear();

    return ret;
}

bool compareInterval(string s1, string s2)
{
    return splitBySpaceAndGetNumber(s1) < splitBySpaceAndGetNumber(s2);
}

int main(int argc, char* argv[])
{
	string FILENAME = "z3_2.txt";
    string SORTED = "z3_2_sorted.txt";

    std::ifstream file;
    file.open(FILENAME);

    if (!file.good())
        return 0;

    std::vector <string> lines;
    string line;
    while (!file.eof())
    {
        std::getline(file, line);
        if (!line.empty())
            lines.push_back(line);
    }
    file.close();

    std::sort(lines.begin(), lines.end(), compareInterval);

    std::ofstream writer;
    writer.open(SORTED);
    if (!writer.good())
        return 0;
	
	for (int i = 0; i < lines.size(); i++)
        writer << lines[i] << endl;

    writer.close();


    return 0;
}

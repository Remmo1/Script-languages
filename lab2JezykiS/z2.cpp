#include<iostream>

int main(int argc, char* argv[], char* env[]) 
{
	puts("Argumenty aplikacji podane z linii konsoli:");
	for(int i = 0; i < argc; i++)
		puts(argv[i]);
	
	puts("Zmienne srodowiskowe:");
	while (*env != NULL)
		puts(*env++);
	
	return 0;
}
@ECHO OFF
DIR *%1 /S /C | FIND "." | FIND /V "DIR" | SORT /+30 /R 
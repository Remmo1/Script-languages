@ECHO OFF
DIR *.* /S /-C | FIND "." | FIND /V "DIR" | SORT /+30 /R 

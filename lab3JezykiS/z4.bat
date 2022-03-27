@ECHO OFF
DIR /C /S /A-D %1 | FIND /V "Directory" | FIND ":" | SORT /+18 /r | head %2
PAUSE

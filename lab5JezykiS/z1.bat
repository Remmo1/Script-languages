@ECHO off

SET max=%1
CALL :start %*
ECHO maksymalna wartosc wynosi: %max% 
EXIT /b

:start
IF -%1-==-- EXIT /B
IF %1 GTR %max% (
	SET /A max=%1
)
SHIFT
GOTO start

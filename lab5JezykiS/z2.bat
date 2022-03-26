@ECHO off

SET /A sum=0
SET /A amountOfNumbers=1

CALL :start %*
SET /A amountOfNumbers=amountOfNumbers - 1

IF %amountOfNumbers% == 0 (
	ECHO srednia wynosi zero
	EXIT /B
)

FOR /F %%N IN ('cscript //nologo eval.vbs "%sum%/%amountOfNumbers%"') DO (
  SET srednia=%%N
)


ECHO srednia wynosi: %srednia%
EXIT /B

:start
IF -%1-==-- EXIT /B

SET /A sum=sum + %1
SET /A amountOfNumbers=amountOfNumbers + 1

SHIFT
GOTO start

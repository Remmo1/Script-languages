@ECHO OFF

CHOICE /C PZ /M "Wcisnij P zeby zobaczyc liczbe przypadkow, Z zeby zobaczyc liczbe zgonow."
SET /A userChoice = %ERRORLEVEL%

SET /P country= Podaj nazwe kraju: 

DEL "z3A.txt"

FOR /F "TOKENS=1,3,5,6,7" %%A IN (COVID.TXT) DO (
	IF %%B GEQ %1 (
		IF %%B LEQ %2 (
			IF %%E == %country% (
				IF %userChoice% == 1 (
					ECHO %%C %%E %%A >> "z3A.txt"
					ECHO %%A %%E %%C
				)ELSE (
					ECHO %%D %%E %%A >> "z3A.txt"
					ECHO %%A %%E %%D
				)			
			)		
		)
	)
) 

sum < z3A.txt
avr < z3A.txt
	
PAUSE

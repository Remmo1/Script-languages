@ECHO OFF

CHOICE /C PZ /M "Wcisnij P zeby zobaczyc liczbe przypadkow, Z zeby zobaczyc liczbe zgonow."
SET /P country= Podaj nazwe kraju: 
SET /A userChoice = %ERRORLEVEL%

FOR /F "TOKENS=1,3,5,6,7" %%A IN (COVID.TXT) DO (
	IF %%B GEQ %1 (
		IF %%B LEQ %2 (
			IF %%E == %country% (
				IF %userChoice% == 1 (
					ECHO %%A %%E %%C
				)ELSE (
					ECHO %%A %%E %%D
				)
				
			)
			
		)
	)
)

	
PAUSE

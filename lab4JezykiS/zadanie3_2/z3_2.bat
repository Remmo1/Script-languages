@ECHO OFF

CHOICE /C BW /M "Wcisnij B zeby zobaczyc najlepsze dni, W zeby zobaczyc najgorsze dni."
SET /A userChoice = %ERRORLEVEL%

SET /P country= Podaj nazwe kraju: 

DEL "z3_2.txt"

FOR /F "TOKENS=1,6,7" %%A IN (COVID.TXT) DO (
	IF %%C == %country% (
		ECHO %%B %%A %%C>> "z3_2.txt"
	)
) 

a.exe

IF %userChoice% == 1 (
	head %1 < "z3_2_sorted.txt"
)Else (
	tail %1 < "z3_2_sorted.txt"
)
	
PAUSE

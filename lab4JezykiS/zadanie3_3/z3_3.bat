@ECHO OFF

SET /P continent= Podaj nazwe kontynentu: 
SET /P month= Podaj miesiac:  

DEL "z3_3.txt"

FOR /F "TOKENS=3,5,11" %%A IN (COVID.TXT) DO (
	IF %%C == %continent% (
		IF %%A == %month% (
			ECHO %%B %%A %%C>> "z3_3.txt"
		)
	)
) 

sum < z3_3.txt

PAUSE
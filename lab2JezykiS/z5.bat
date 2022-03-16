@ECHO OFF

SET /A ZDERZAK=1
SET /A DRZWI=2
SET /A OPONA=4
SET /A SWIATLA=8
SET /A SKRZYNIA=16
SET /A HAMULCE=32
SET /A SILNIK=64

SET /A KOD = %ERRORLEVEL%

SET /A WYNIK="%KOD% & %SILNIK%"
IF %WYNIK% EQU %SILNIK% ECHO zepsuty silnik

SET /A WYNIK="%KOD% & %HAMULCE%"
IF %WYNIK% EQU %HAMULCE% ECHO zepsute hamulce

SET /A WYNIK="%KOD% & %SKRZYNIA%"
IF %WYNIK% EQU %SKRZYNIA% ECHO zepsuta skrzynia

SET /A WYNIK="%KOD% & %SWIATLA%"
IF %WYNIK% EQU %SWIATLA% ECHO zepsute swiatla

SET /A WYNIK="%KOD% & %OPONA%"
IF %WYNIK% EQU %OPONA% ECHO peknieta opona

SET /A WYNIK="%KOD% & %DRZWI%"
IF %WYNIK% EQU %DRZWI% ECHO zepsute drzwi

SET /A WYNIK="%KOD% & %ZDERZAK%"
IF %WYNIK% EQU %ZDERZAK% ECHO zepsuty zderzak
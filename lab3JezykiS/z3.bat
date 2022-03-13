@ECHO OFF
FOR /F %%A IN ('dir /b /s /ad %1^|find /c /v "" ') DO SET COUNT=%%A
ECHO %COUNT%
PAUSE

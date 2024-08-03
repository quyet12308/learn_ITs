@echo off
for /f %%i in (test.txt) do (
    mkdir "%%i"
)
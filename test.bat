::Test bat file
:: @echo off
powershell
echo "Downloading Firefox"
pause
powershell -Command "Invoke-WebRequest https://www.mozilla.org/en-US/firefox/download/thanks/ -Outfile firefox.exe"
cls

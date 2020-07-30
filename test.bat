::Test bat file
powershell 
echo "Downloading Firefox"
pause
powershell -Command "Invoke-WebRequest https://www.mozilla.org/en-US/firefox/download/thanks/ -Outfile Downloads/firefox.exe"
cls

@echo off
setlocal enabledelayedexpansion

for %%f in (*.html) do (
    echo Processing %%f...
    C:\xampp\perl\bin\perl.exe -pi "fix_urls3.pl" "%%f"
)

echo All files processed successfully!
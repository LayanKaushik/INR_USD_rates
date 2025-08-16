@echo off
echo Starting INR USD Rates Web Application...
if exist .env (
    for /f "tokens=1,2 delims==" %%a in (.env) do set %%a=%%b
)
python run_web_app.py
pause

@echo off

set main_location=%cd%
set back_location=%main_location%\Back\Back
set front_location=%main_location%\Front\durachok

start cmd /k "cd %main_location%\Back\Back && pip install -r requirements.txt && REM uvicorn fast:app"
start cmd /k "cd %front_location% && npm i && npm run serve"
TIMEOUT /T 15 /NOBREAK
start "" http://127.0.0.1:8080/


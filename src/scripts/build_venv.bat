@echo off
setlocal enabledelayedexpansion

:: Проверяем, существует ли папка apps
if not exist "apps\" (
    echo Folder "apps" not found!
    pause
    exit /b 1
)

:: Переходим в папку apps
pushd apps

:: Для каждой подпапки в apps создаем venv
for /d %%d in (*) do (
    echo Create venv in folder: %%d
    cd "%%d"
    python -m venv venv
    cd ..
)

:: Возвращаемся обратно
popd

echo Virtual venv is created!
pause
#!/bin/bash

# Проверяем, существует ли папка apps
if [ ! -d "apps" ]; then
    echo "Folder "apps" not found!"
    exit 1
fi

# Переходим в папку apps
cd apps || exit

# Для каждой подпапки в apps создаем venv
for dir in */; do
    dir=${dir%/}  # Убираем слеш в конце
    echo "Create venv in folder: %%d"
    cd "$dir" || continue
    python3 -m venv venv
    cd ..
done

echo "Virtual venv is created!"
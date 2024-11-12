# Установка и запуск:
git clone https://github.com/VitalyMyalkin/google-playwright.git

cd ./google-playwright

python -m venv venv

source venv/Scripts/activate

pip install -r requirements.txt

pytest

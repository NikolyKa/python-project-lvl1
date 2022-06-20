install: #установление зависимостей
	poetry install
brain-games: #запускает brain-games
	poetry run brain-games
build: #собирает программу
	poetry build 
publish: #публикует программу
	poetry publish --dry-run
package-install: #устанавливает пакет
	python3 -m pip install --user dist/*.whl
lint: #проверяет код на чистоту
	poetry run flake8 brain_games


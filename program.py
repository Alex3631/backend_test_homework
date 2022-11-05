print('Я домашка')
# Делаем первый коммит, в кавычках пишем комментарий.
git commit -m "First commit: change program.py"

# Добавили файлы в индекс Git.
git add .

# Добавили эти файлы к предыдущему коммиту.
git commit --amend -m "First commit: new files added" 
print("Hallo")

# git branch - список веток
# git branch new_feature - создать ветку  new_feature-название версии
# git checkout new_feature - переключиться
# git push
# git checkout -b new_feature - создать и переключиться сразу
# git merge new_feature - слить ветку в текущую (я перешел в ветку master, git merge new_feature - и все сливаемся из ветки new_feature в ветку master)
# git branch -d new_feature - удалить ветку

#конфликты  git
#один и тот же файл на разных ветках исправить = то он не знает что правильно а что нет - при обьединении выдаст конфликт. выбираем в файле то что правильно, остальное удаляем - повторно  git push
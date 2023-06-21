# FirstDjangoTodoApp
Udemy　大橋さん　djangoの基礎　TodoApp

マイグレーションはmanage.pyのあるディレクトリで
python3 manage.py makemigrations
これで新しいマイグレーション（models.pyとデータベースの間のより詳細な設計図）ができるので、
エラーがなければ同じディレクトリ内で
python3 manage.py migrate
によって無事にマイグレートが完了する。

ローカルでサーバーを立ち上げる時は
python3 manage.py runserver

管理者画面は
http://localhost:8000/admin/

パスワードや、作業履歴はなどはNotionのDjango TODOAPP作成にて確認。


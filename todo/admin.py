# 管理画面を操作するためのファイル。

from django.contrib import admin
# 下に入力したTodoModelのインポート。
from .models import TodoModel

# Register your models here.

# adminページでテーブルを扱えるようにするコマンド。
# models.pyの継承したクラス名を引数とする。
admin.site.register(TodoModel)
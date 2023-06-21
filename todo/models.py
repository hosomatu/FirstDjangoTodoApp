from django.db import models

PRIORITY = (('danger','high'),('info','normal'),('succes','low'))
# あらかじめ用意されているクラスを継承して使う。このTodoModelはadmin.pyに記載することでadminページで扱えるようになる。
class TodoModel(models.Model):
    # 項目（左）に対して、どんなデータを入れていくかを指定（モデルフィールド）。qiitaとかで調べる。（django モデル　フィールド種類）
    # ちなみにCharFieldは文字列型のデータ。最大何文字か指定しないとエラーになる。
    title = models.CharField(max_length=100)
    # Text.Fieldは長い文字列。
    memo = models.TextField()
    priority = models.CharField(
        max_length= 50,
        choices = PRIORITY,
    )
    duedate = models.DateTimeField()

    # adminページで作成したものをみやすくするために、オブジェクトを文字列で表示するためのコード。
    # selfとは出来上がったオブジェクトひとつひとつのこと。
    def __str__(self):
        return self.title
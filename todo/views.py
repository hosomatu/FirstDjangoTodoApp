# リクエストを受けて、レスポンスを返すファイル。
# viewsは各アプリ内にある。プロジェクトにはない。アプリのurls.pyからリクエストが来たあとの実行する部分を定義する。（関数など）
# 同じアプリ内のurls.pyの下でいうtodoの中身について書いていくファイル。
# urlpatterns = [
#     # urlにaがあったら、views.pyに書いたtodo関数を実行する。
#     path('a/',todo)
# ]


from django.shortcuts import render
from .models import TodoModel
# CRUDのうちのreadを簡単に扱うためにあらかじめ定められたListというクラスを使う。
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy

# httpモジュールの中のhttpresponseをインポートしている。（インポート方法などはググって使う。公式とかqiitaとか）
# from django.http import HttpResponse

# 以下５行は初めにエラー回避のために記載したものなのでコメントアウト。
# # requestを引数としている。（基本的にはrequestとする。わかりやすいから）
# # HttpResponseとはdjangoであらかじめ定められているクラス。クラスから（）の中のオブジェクトを作ってそれをレスポンスとして返している。
# def todo(request):
#     return HttpResponse('')


# あtodoのurls.pyで記載したTodoListについて、内容を記載していく。
# templateのとことは返すページを指定している。、list.htmlを返す。
# modelのところはどのテーブルを使用するかを記載している。上でmodelsからTodoModelをimportするのを忘れない。
class TodoList(ListView):
    template_name = 'list.html'
    model = TodoModel

# aTodoDeltailを作成するよ、DetailViewを継承して。という意味
class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel

class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    # CreateViewを使う時はテーブルのどこにするかをfieldsタグで定めなければいけない。
    fields = ('title','memo','priority','duedate')
    # createが完了したあとにどのURLに遷移するか定める。（定めないとエラー）
    # reverse_lazyはクラスベースドビューのときに使う。
    # reverseとは、urlを逆まわりするイメージ。つまり、urls.pyに戻る。
    success_url = reverse_lazy('list')

class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')

class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    fields = ('title','memo','priority','duedate')
    success_url = reverse_lazy('list')

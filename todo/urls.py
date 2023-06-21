# ここはtodoアプリのurls.pyなので、プロジェクトのurls.pyからリクエストを受けたあとにviews.pyに送るための処理。（最終的にレスポンスを返すための処理）を行う。
# 関数を作成してレスポンスを返すfunctionClassViewと、あらかじめ作られたクラスを継承して使うClassBasedViewとあって、今回は後者。



from django.urls import path
from .views import TodoList,TodoDetail,TodoCreate,TodoDelete,TodoUpdate

urlpatterns = [
    # クラスを継承して使うときは.as_viewという書き方をする。
    # urlを指定できたら、次はviews.pyで、TodoListというオブジェクトの中身を書いていく。
    # 意味は、URLにlistとあったら、views.pyのTodoListを呼び起こすよってこと。
    # name=としているのは、CreateViewを使う時のreverseのとこに指定できるように名前をつけている。
    path('list/', TodoList.as_view(),name = 'list'),
    # DetailViewを使用する時はPKを指定しないといけない。intとは(インテジャー型）整数のこと。
    path('detail/<int:pk>', TodoDetail.as_view(),name = 'detail'),
    path('create/', TodoCreate.as_view(),name = 'create'),
    # deleteの場合もpkを指定する必要がある。
    path('delete/<int:pk>',TodoDelete.as_view(),name='delete'),
    path('update/<int:pk>',TodoUpdate.as_view(),name = 'update'),

]

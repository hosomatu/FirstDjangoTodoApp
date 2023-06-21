# ここはプロジェクトのurls.pyなので、最初にブラウザからリクエストを受け取って、各アプリに対してリクエストを送る。


from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 空欄なのでurlに何も記載がなければ、todoアプリを呼び出す（localhost:8000)todoの中のurls.pyに飛ぶ。
    path('',include('todo.urls'))
]

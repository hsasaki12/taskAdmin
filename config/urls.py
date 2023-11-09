from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),  # 管理画面
    path('', views.index),  # トップページ
    path('detail/<int:pk>/', views.detail),  # 詳細ページ
    path('delete/<int:pk>/', views.delete),  # 削除ページ
    path('update/<int:pk>/', views.update),  # 更新ページ
    path('create/', views.create),  # 新規作成ページ
]
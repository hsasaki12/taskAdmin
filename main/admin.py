from django.contrib import admin
from .models import TodoModel  # 必要なモデルをimport

admin.site.register(TodoModel)  # モデルを管理画面に表示するために記載
from django.shortcuts import render, redirect  # 追記
from django.http import HttpResponse
from main.models import TodoModel

# ヘッダー背景カラー
bg_color_class = ['bc0', 'bc1', 'bc2', 'bc3', 'bc4']
context = {
    'bg_color_class': bg_color_class[1],  # カラーチョイス
}


def index(request):
    object_list = TodoModel.objects.all()
    context["object_list"] = object_list
    return render(request, 'index.html', context)


def detail(request, pk):
    obj = TodoModel.objects.get(pk=pk)
    context["object"] = obj
    return render(request, 'detail.html', context)


def delete(request, pk):
    obj = TodoModel.objects.get(pk=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("/")
    context["object"] = obj
    return render(request, 'delete.html', context)


def update(request, pk):
    obj = TodoModel.objects.get(pk=pk)
    if request.method == "POST":

        obj.title = request.POST.get("title")
        obj.memo = request.POST.get("memo")
        obj.duedate = request.POST.get("duedate")
        image = request.FILES.get('image', None)
        print('imageimageimageimage', image)
        if image is not None:
            obj.image = image
        obj.save()
        return redirect("/")
    context["object"] = obj
    return render(request, "update.html", context)


def create(request):
    if request.method == "POST":
        TodoModel.objects.create(
            title=request.POST.get("title"),
            memo=request.POST.get("memo"),
            duedate=request.POST.get("duedate"),
            image=request.FILES.get('image', None),
        )
        return redirect("/")
    return render(request, "create.html", context)
from django.shortcuts import render
from main.models import TodoModel
from django.conf import settings  # settings.pyの公式のインポート方法
from main import functions
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

def trim_view(request):
    # POSTメソッドの場合にif文を実行
    if request.method == 'POST':
        # name属性がimageのタグからvalueを取得
        im = request.FILES.get('image')

        # name属性がareaのタグからvalueを取得
        area = request.POST.get('area')

        # 元画像のファイル名
        original_filename = im.name

        # トリミング画像のファイル名
        trimmed_filename = f'trimmed_{area}_{im.name}'

        # 元画像の保存先パスを生成
        original_path = settings.IMAGE_DIR / original_filename

        # トリミング画像の保存先パスを生成
        trimmed_path = settings.IMAGE_DIR / trimmed_filename

        # functionsの中のトリミング処理関数を実行
        functions.trim(im, area, original_path, trimmed_path)

        # 各値をテンプレートで使うためにコンテキストで渡す
        context['area'] = area
        context['original_filename'] = original_filename
        context['trimmed_filename'] = trimmed_filename

    return render(request, 'trim.html', context)
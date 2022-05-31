from django.shortcuts import render, redirect
from .models import ArticleModel, CategoryModel
# Create your views here.

def article(request):
    if request.method == "GET":
        category = CategoryModel.objects.all()
        print(category)
        return render(request, 'new.html', {'category': category})

    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        category = request.POST.get('category')

        new_article = ArticleModel()
        new_article.title = title
        new_article.content = content
        new_article.category_id = category
        new_article.save()
        return redirect('/')

def article_list(request, category_id):
    if request.method == "GET":
        article_category_list = ArticleModel.objects.filter(category_id=category_id)
        return render(request, 'category.html', {'category': catecory})


def catecory(request):
    if request.method == "GET":
        catecory = CategoryModel.objects.all()
        return render(request, 'category.html', {'category': catecory})
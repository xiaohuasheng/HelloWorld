from django.http import HttpResponse
from django.shortcuts import render, redirect

from TestModel.models import Test


def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)


# 数据库操作
def testdb(request):
    test1 = Test(name='runoob')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")


def search_post(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)


def link(request, link_id):
    link_obj = Test.objects.get(id=link_id)
    link_obj.click += 1
    link_obj.save()
    return redirect(link_obj.url)


def delete_link(request, link_id):
    link_del = Test.objects.get(id=link_id)
    link_del.delete()
    return HttpResponse("%s删除成功" % link_id)


def add_link(request):
    ctx = {}
    link_list = Test.objects.all().order_by('-click')
    url_list = []
    for link_item in link_list:
        temp = {
            'id': link_item.id,
            'url': link_item.url,
            'description': link_item.description,
        }
        url_list.append(temp)
    ctx['url_list'] = url_list
    if request.POST:
        s_link = Test()
        s_link.url = request.POST['url']
        s_link.description = request.POST['description']
        ctx['rlt'] = ''
        s_link.click = 1
        s_link.save()
    return render(request, "post.html", ctx)

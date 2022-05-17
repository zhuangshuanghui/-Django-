from django.forms import models
from django.shortcuts import render
from .forms import ArticleForm, UserForm, UserProfileForm, LoginForm
from app2005050209 import models
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout#login_required,permission_required
from django.contrib.auth.decorators import login_required,permission_required


def home(request):
    return render(request, "base.html")
# Create your views here.

# 添加文章功能
def addbook(request):
    if request.method == 'POST':
        article = ArticleForm(request.POST)
        if article.is_valid:
            article.save()
            return render(request, 'addbook.html', {'from': article, 'result': "保存成功"})
    else:
        form = ArticleForm()
        return render(request, 'addbook.html', {'form': form})


@login_required
@permission_required("blog.change_page", login_url="/deny/")
# 编辑页面
def editbooks(request, id):
    article = models.Article.objects.get(id=id)  # 获取到对应id的页面
    if request.method == 'POST':
        0
        article = ArticleForm(request.POST, instance=article)
        if article.is_valid():
            article.save()
            return render(request, 'editbooks.html', {'form': article, 'id': id, 'result': '保存成功'})
    else:
        form = ArticleForm(instance=article)
        return render(request, "editbooks.html", {'form': form, 'id': id})

# 显示文章 主页面  带有删除编辑功能


def lookbooks(request):
    article = models.Article.objects.all()
    return render(request, 'lookbooks.html', {'article': article})

# 删除


def deletebooks(request, id):
    result = '删除失败'
    if models.Article.objects.filter(id=id).count() > 0:
        article = models.Article.objects.get(id=id)
        article.delete()
        result = '删除成功'
    return render(request, 'deletebooks.html', {'result': result})


# 单一显示
def onebooks(request, id):
    article = models.Article.objects.get(id=id)
    category = models.Category.objects.get(id=article.category_id)
    return render(request, 'onebooks.html', {'article': article, 'category': category})


# 分类显示文章
def fenleibooks(request, id):
    category = models.Category.objects.get(id=id)
    article = models.Article.objects.filter(category_id=category.id)
    return render(request, "fenleibooks.html", {'article': article})

# 显示所有文章(分页)


def allbooks(request, pagenum=1):
    article = models.Article.objects.all()
    paginator = Paginator(article, 5)
    pageList = paginator.get_page(pagenum)
    return render(request, "allbooks.html", {'pageList': pageList})


def register(request):
    # 布尔值，记录注册是否成功，成功后改为 True
    registered = False
    if request.method == 'POST':
        # UserForm 和 UserProfileForm 中的数据都需要
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        # 两个表单中的数据都要验证通过
        if user_form.is_valid() and profile_form.is_valid():

            # 把 UserForm 中的数据存入数据库
            user = user_form.save()
            # 使用 set_password 方法计算密码哈希值
            user.set_password(user.password)
            user.save()
            # 因为要自行处理 user 属性，所以设定 commit=False，延迟保存模型，以防出现完整性问题
            profile = profile_form.save(commit=False)
            profile.user = user
            # 保存 UserProfile 模型实例
            profile.save()
            # 更新变量的值，成功注册
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        # 不是 HTTP POST 请求，渲染两个 ModelForm 空表单
        user_form = UserForm()
        profile_form = UserProfileForm()
    # 根据上下文渲染模板
    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def loginPage(request):
    logined = False
    if request.method == "POST":
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            username = loginform.cleaned_data["username"]
            password = loginform.cleaned_data["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            logined = True
    else:
        loginform = LoginForm()
    return render(request, "login.html", {
        "login_form": loginform,
        "logined": logined
    })


def logoutPage(request):
    logout(request)
    return render(request, "main.html")


def visitor_cookie_handler(request, response):
    # 获取网站的访问次数
    # 使用 COOKIES.get() 函数读取“visits”cookie
    # 如果目标 cookie 存在，把值转换为整数
    # 如果目标 cookie 不存在，返回默认值 1
    visits = int(request.COOKIES.get('visits', '1'))

    last_visit_cookie = request.COOKIES.get('last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(
        last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')
    # 如果距上次访问已超过一天……
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        # 增加访问次数后更新“last_visit”cookie
        response.set_cookie('last_visit', str(datetime.now()))
    else:
        # 设定“last_visit”cookie
        response.set_cookie('last_visit', last_visit_cookie)
        # 更新或设定“visits”cookie
    #visits = visits + 1
    response.set_cookie('visits', visits, max_age=24*60*60)


def readSession(request):
    stuId = request.session.get('stuId', '没有内容')
    # 返回
    return render(request, "readsession.html", {"stuId": stuId})

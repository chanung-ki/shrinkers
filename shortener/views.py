from django.shortcuts import render, redirect
from shortener.models import Users

# Create your views here.

def index(request):
    user = Users.objects.filter(username='admin').first() # Django의 ORM
    email = user.email if user else '비회원이시군요 ! 회원가입을 해보세요 ㅎㅎ'
    print(email)
    # print(request.user.is_authenticated) # user.is_authenticated => 로그인 여부 검즘
    # if request.user.is_authenticated is False:
    #     email = '비회원이시군요 ! 회원가입을 해보세요 ㅎㅎ'
    return render(request, 'base.html', {'welcome_msg' : '안녕하세용ㅎㅎ', 'member' : f'{email}'})

def redirect_test(request):
    print("Go Redirect")
    return redirect("index_A") # redirect 시에는 Urls.py에 있는 name을 설정해주는 것임
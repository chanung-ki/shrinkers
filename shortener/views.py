from django.shortcuts import render, redirect
from shortener.models import Users
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse 

# Create your views here.

def index(request):
    print(request.user.pay_plan.name)
    user = Users.objects.filter(username='admin').first() # Django의 ORM
    email = user.email if user else '비회원이시군요 ! 회원가입을 해보세요 ㅎㅎ'
    print(email)
    print(request.user.is_authenticated) # user.is_authenticated => 로그인 여부 검즘
    if request.user.is_authenticated is False:
        email = '비회원이시군요 ! 회원가입을 해보세요 ㅎㅎ'
    return render(request, 'base.html', {'welcome_msg' : '안녕하세용ㅎㅎ', 'member' : f'{email}'})

# def redirect_test(request):
#     print("Go Redirect")
#     return redirect("index_A") # redirect 시에는 Urls.py에 있는 name을 설정해주는 것임

@csrf_exempt
def get_user(request, user_id):
    print (user_id)
    if request.method == "GET":
        abc = request.GET.get("abc")
        xyz = request.GET.get("xyz")
        user = Users.objects.filter(pk=user_id).first()
        return render(request, 'base.html', {'user':user, 'params':[abc, xyz]})
    elif request.method == "POST":
        username = request.Get.get('username')
        if username:
            user = Users.objects.filter(pk=user_id).update(username=username)
            return JsonResponse(status=201, data=dict(msg='You just reached with Post Method'), safe=False)
            #status=201, safe=False => 한국어 안깨지게 하기 위함 


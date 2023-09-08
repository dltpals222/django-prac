from django.shortcuts import render
from polls.models import pracTable

# Create your views here.


def index(request):
    return render(request, "polls/index.html")


# * 공통적으로 사용되는 변수
tag_data = {
    "ulList": [
        ["checkbox", ""],
        ["no", "No"],
        ["name", "이름"],
        ["number", "번호"],
        ["nickname", "아이디"],
        ["deposit", "총 입금액"],
        ["score", "현스코어"],
    ],
}


def userManagement(request):
    return render(request, "polls/userManagement.html", tag_data)


def create(request):
    return render(request, "polls/create.html", tag_data)


def update(request):
    return render(request, "polls/update.html", tag_data)

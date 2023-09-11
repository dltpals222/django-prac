from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import mytable
from .forms import MytableForm

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
    "list": [],
}
for i in range(10):
    tag_data["list"].append(i)


def userManagement(request):
    return render(request, "polls/userManagement.html", tag_data)


def create(request):
    if request.method == "POST":
        form = MytableForm(request.POST)
        if form.is_valid():
            # 10개의 필드값 전부 가져오기
            field_values = []
            for i in range(10):
                name = request.POST.get(f"name_{i}")
                number = request.POST.get(f"number_{i}")
                nickname = request.POST.get(f"nickname_{i}")
                deposit = request.POST.get(f"deposit_{i}")
                score = request.POST.get(f"score_{i}")
                if (
                    name != ""
                    and number != ""
                    and nickname != ""
                    and deposit != ""
                    and score != ""
                ):
                    obj = {
                        "name": name,
                        "number": number,
                        "nickname": nickname,
                        "deposit": deposit,
                        "score": score,
                    }
                    field_values.append(obj)

            # DB에 저장하기
            for value in field_values:
                entry = mytable(
                    name=value["name"],
                    number=int(value["number"]),
                    nickname=value["nickname"],
                    deposit=int(value["deposit"]),
                    score=int(value["score"]),
                )
                entry.save()

            return HttpResponseRedirect("polls/create")
    else:
        form = MytableForm()

    return render(request, "polls/create.html", tag_data)


def update(request):
    return render(request, "polls/update.html", tag_data)


def delete(request):
    return render(request, "polls/delete.html", tag_data)

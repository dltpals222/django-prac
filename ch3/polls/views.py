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
            prac_Table = form.save(commit=False)

            # 10개의 필드값 전부 가져오기
            field_values = []
            for i in range(10):
                field_divName = f"field_{i}"
                field_value = request.POST.get(field_divName, "")
                field_values.append(field_value)

            # 비어있는 값이 있는지 확인 후 있으면 제거
            filtered_values = [value for value in field_values if value != ""]

            prac_Table.save()

            return HttpResponseRedirect("polls/create")
    else:
        form = MytableForm()

    return render(request, "polls/create.html", tag_data)


def update(request):
    return render(request, "polls/update.html", tag_data)


def delete(request):
    return render(request, "polls/delete.html", tag_data)

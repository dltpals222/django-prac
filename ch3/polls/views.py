from django import forms
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


MytableFormSet = forms.formset_factory(MytableForm, extra=10)


def create(request):
    if request.method == "POST":
        formset = MytableFormSet(request.POST)
        if formset.is_valid():
            for i in formset:
                if i.is_valid() and i.has_changed():
                    instance = i.save()
            return HttpResponseRedirect("polls/create")
    else:
        formset = MytableFormSet()

    context = {**tag_data, "formset": formset}

    return render(request, "polls/create.html", context)


def update(request):
    return render(request, "polls/update.html", tag_data)


def delete(request):
    return render(request, "polls/delete.html", tag_data)

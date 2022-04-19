from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage
from django.views.generic import DetailView
from . import models


def home(request):
    QnA_list = models.QnA.objects.all()
    paginator = Paginator(QnA_list, 10)
    page_number = request.GET.get("page")
    try:
        QnA = paginator.get_page(page_number)
        return render(request, "home.html", {"QnA": QnA, "QnA_list": QnA_list})
    except EmptyPage:
        return redirect("/")


def QnA(request):
    QnAs = models.QnA.objects.all()
    if request.method == "POST":
        title = request.POST["title"]
        cate = request.POST["category"]
        contents = request.POST["contents"]
        message = request.POST["message"]
        email = request.POST["email"]
        QnA = models.QnA.objects.create(
            title=title, contents=contents, message=message, email=email
        )

        return HttpResponseRedirect(reverse("posts"))
    else:
        return render(request, "posts/QnA.html", {"QnAs": QnAs})


class QnA_detail(DetailView):
    model = models.QnA


def Comment(request):
    pass

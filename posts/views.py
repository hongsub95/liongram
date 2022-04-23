from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage
from django.views.generic import DetailView, UpdateView
from . import models
from . import forms


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
        title = request.POST.get("title")
        cate = request.POST.get("category")
        contents = request.POST.get("contents")
        message = request.POST.get("message")
        email = request.POST.get("email")
        qna = models.QnA(title=title, contents=contents, message=message, email=email)
        qna.save()
        return redirect("posts:QnA_detail", qna.pk)
    return render(request, "posts/QnA.html", {"QnAs": QnAs})


class QnAUpdateView(UpdateView):
    model = models.QnA
    template_name = "posts/QnA_Edit.html"
    fields = (
        "title",
        "contents",
        "message",
        "email",
    )
    success_url = "/"

    def get_object(self):
        qna = get_object_or_404(models.QnA, pk=self.kwargs["pk"])
        return qna


class QnA_detail(DetailView):
    model = models.QnA


def Comment(request, qna_pk):
    Comment = forms.CommentForm(request.POST)
    if Comment.is_valid():
        comment = Comment.save(commit=False)
        comment.qna = get_object_or_404(models.QnA, pk=qna_pk)
        comment.save()
        return redirect("posts:QnA_detail", qna_pk)
    return render(request, "posts/comment.html", {"Comment": Comment})


def Comment_delete(request):
    pass


def Comment_edit(request):
    pass

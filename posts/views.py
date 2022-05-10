from random import choices
from ssl import ALERT_DESCRIPTION_ACCESS_DENIED
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator, EmptyPage
from django.views.generic import DetailView, UpdateView, DeleteView, FormView
from . import models
from . import forms


def home(request):
    QnA_list = models.QnA.objects.all().order_by("-created")
    paginator = Paginator(QnA_list, 10)
    page_number = request.GET.get("page")
    try:
        QnA = paginator.get_page(page_number)
        return render(
            request,
            "home.html",
            {"QnA": QnA, "QnA_list": QnA_list},
        )
    except EmptyPage:
        return redirect("/")


"""
def QnA(request):
    QnA_form = forms.CategoryForm()
    if request.method == "POST":
        title = request.POST.get("title")
        cate = request.POST.get("category")
        is_email = request.POST.get("is_email")
        is_phone = request.POST.get("is_phone")
        contents = request.POST.get("contents")
        message = request.POST.get("message")
        email = request.POST.get("email")
        qna = models.QnA(
            title=title,
            contents=contents,
            category=cate,
            is_email=is_email,
            is_phone=is_phone,
            message=message,
            email=email,
        )
        qna.save()
        return redirect("posts:QnA_detail", qna.pk)
    return render(
        request,
        "posts/QnA.html",
        {"QnA_form": QnA_form, "QnA": QnA},
    )
"""


class CreateQnAView(FormView):
    form_class = forms.QnACreateForm
    template_name = "posts/QnA.html"

    def form_valid(self, form):
        qna = form.save()
        qna.save()
        return redirect(reverse("posts:QnA_detail", kwargs={"pk": qna.pk}))


class QnA_detail(DetailView):
    model = models.QnA

    def get_object(self):
        qna = get_object_or_404(models.QnA, pk=self.kwargs["pk"])
        return qna


class QnAUpdateView(UpdateView):
    model = models.QnA
    template_name = "posts/QnA_Edit.html"
    fields = (
        "title",
        "contents",
        "category",
        "message",
        "email",
    )

    def get_context_data(self, **kwargs):
        context = super(QnAUpdateView, self).get_context_data(**kwargs)
        context["category"] = forms.CategoryForm
        return context

    def get_success_url(self):
        qna_pk = self.kwargs.get("qna_pk")
        return reverse(
            "posts:QnA_detail",
            kwargs={
                "pk": qna_pk,
            },
        )

    def get_object(self):
        qna = get_object_or_404(models.QnA, pk=self.kwargs["qna_pk"])
        return qna


def QnA_delete(request, qna_pk):
    qna = models.QnA.objects.get(pk=qna_pk)
    qna.delete()
    return redirect("/")


def Comment(request, qna_pk):
    Comment = forms.CommentForm(request.POST)
    if Comment.is_valid():
        comment = Comment.save(commit=False)
        comment.qna = get_object_or_404(models.QnA, pk=qna_pk)
        comment.save()
        return redirect("posts:QnA_detail", qna_pk)
    return render(request, "posts/comment.html", {"Comment": Comment})


class Comment_Delete(DeleteView):
    model = models.Comment

    def get_success_url(self):
        qna_pk = self.kwargs.get("qna_pk")
        return reverse("posts:QnA_detail", kwargs={"pk": qna_pk})

    def get_object(self):
        comment = get_object_or_404(models.Comment, pk=self.kwargs["comment_pk"])
        return comment

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


def Comment_edit(request, qna_pk, comment_pk):
    Comment = models.Comment.objects.get(pk=comment_pk)
    return render(
        request, "posts/comment_edit.html", {"Comment": Comment, "qna_pk": qna_pk}
    )


def Comment_update(request, qna_pk, comment_pk):
    Comment = models.Comment.objects.get(pk=comment_pk)
    Comment.comment = request.POST.get("comment")
    Comment.save()
    return redirect(reverse("posts:QnA_detail", kwargs={"pk": qna_pk}))

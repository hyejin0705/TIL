from django.db.models import Q, Count
from django.shortcuts import render, redirect
from .models import Question
from .forms import QuestionForm, CommentForm

# Create your views here.
def index(request):
    questions = Question.objects.order_by('-pk')
    context = {
        'questions': questions,
    }
    return render(request, 'eithers/index.html', context)


def create(request):
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question = question_form.save()
            return redirect('eithers:detail', question.pk)
    else:
        question_form = QuestionForm()
    context = {
        'question_form': question_form,
    }
    return render(request, 'eithers/create.html', context)


def detail(request, question_pk):
    # 계산이 필요한 값
    # 왼쪽을 선택한 댓글의 개수
    # 오른쪽을 선택한 댓글의 개수
    count_a = Count('comment', filter=Q(comment__pick==False))
    count_b = Count('comment', filter=Q(comment__pick==True))
    total_count = Count('comment')

    question = Question.objects.annotate(
        count_a = count_a,
        count_b = count_b,
        total_count = total_count,

    ).get(pk=question_pk)

    # question.count_a    # a를 선택한 댓글의 개수
    # question.count_b    # b를 선택한 댓글의 개수

    if question.total_count == 0:
        a_per = 0
        b_per = 0
    else:
        a_per = round(question.count_a / question.total_count * 100, 2)
        b_per = round(question.count_b / question.total_count * 100, 2)

    context = {
        'question': question,
        'comments': comments,
        'comment_form': comment_form,
        'a_per': a_per,
        'b_per': b_per,
    }
    return render(request, 'eithers/detail.html', context)


def comments_create(request, question_pk):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.question_id = question_pk
        comment.save()
    return redirect('eithers:detail', question_pk)


def random(request):
    pass
    
    context = {
        'question': question, 
        'comments': comments,
        'comment_form': comment_form,
        'a_per': a_per, 
        'b_per': b_per,
    }

    return render(request, 'eithers/detail.html', context)

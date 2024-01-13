<<<<<<< HEAD
# views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Essay, Comment
from .forms import EssayForm , CommentApprovalForm
from django.contrib.auth.decorators import login_required , user_passes_test
from authors.models import Profile_authors

def essay_list(request):
    essays = Essay.objects.all()
    authors = Profile_authors.objects.all()
    return render(request, 'essay_list.html', {'essays': essays,'authors':authors})


def add_comment(request, essay_id):
    essay = get_object_or_404(Essay, id=essay_id)

    if request.method == 'POST':
        text = request.POST.get('text')
        Comment.objects.create(essay=essay, text=text)

    return redirect('essay_list')

def essay_list(request):
    essays = Essay.objects.all()
    return render(request, 'essay_list.html', {'essays': essays})
@login_required
def add_essay(request):
    if request.method == 'POST':
        form = EssayForm(request.POST)
        if form.is_valid():
            essay = form.save(commit=False)
            essay.author = request.user.profile_authors
            form.save()
            return redirect('essay_list')
    else:
        form = EssayForm(initial={'author': request.user.username})  # Set the initial value for the author field

    return render(request, 'add_essay.html', {'form': form})

def update_essay(request,pk):
    essay_id = Essay.objects.get(id=pk)
    form = EssayForm(instance=essay_id)
    if request.method == 'POST':
        form = EssayForm(request.POST , request.FILES ,instance=essay_id)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'update_essay.html',context)

def delete_essay (request,pk):  
    essay_id = Essay.objects.get(id=pk) 
    if request.method == "POST" :
        essay_id.delete()
        return redirect('/')
    context = {'item':essay_id}
    return render(request , 'delete_essay.html',context)

@user_passes_test(lambda u: u.is_superuser)
def comment_approval_page(request):
    comments = Comment.objects.filter(is_approved=False )

    
    forms = []

    if request.method == 'POST':
        # Handle form submissions
        for comment in comments:
            form = CommentApprovalForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('comment_approval_page')

    else:
        # Display comments and forms
        for comment in comments:
            forms.append(CommentApprovalForm(instance=comment))
    return render(request, 'comment_approval_page.html', {'comments': comments, 'forms': forms})
=======
# views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Essay, Comment
from .forms import EssayForm , CommentApprovalForm
from django.contrib.auth.decorators import login_required , user_passes_test
from authors.models import Profile_authors
from django.core.mail import send_mail

def essay_list(request):
    essays = Essay.objects.all()
    authors = Profile_authors.objects.all()
    return render(request, 'essay_list.html', {'essays': essays,'authors':authors})


def add_comment(request, essay_id):
    essay = get_object_or_404(Essay, id=essay_id)

    if request.method == 'POST':
        text = request.POST.get('text')
        Comment.objects.create(essay=essay, text=text)

    return redirect('essay_list')

def essay_list(request):
    essays = Essay.objects.all()
    return render(request, 'essay_list.html', {'essays': essays})
@login_required
def add_essay(request):
    essays = Essay.objects.all()
    if request.method == 'POST':
        form = EssayForm(request.POST)
        if form.is_valid():
            essay = form.save(commit=False)
            essay.author = request.user.profile_authors
            form.save()
            for essay in essays:
                subject = 'Hello Friend!'
                message = 'This is test 4.'
                from_email = 'hamidreshtime@gmail.com'
                recipient_list = [essay.author.email]
                send_mail(subject, message, from_email, recipient_list)            

            return redirect('essay_list')
    else:
        form = EssayForm(initial={'author': request.user.username})  # Set the initial value for the author field

    return render(request, 'add_essay.html', {'form': form})

def update_essay(request,pk):
    essay_id = Essay.objects.get(id=pk)
    form = EssayForm(instance=essay_id)
    if request.method == 'POST':
        form = EssayForm(request.POST , request.FILES ,instance=essay_id)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'update_essay.html',context)

def delete_essay (request,pk):  
    essay_id = Essay.objects.get(id=pk) 
    if request.method == "POST" :
        essay_id.delete()
        return redirect('/')
    context = {'item':essay_id}
    return render(request , 'delete_essay.html',context)

@user_passes_test(lambda u: u.is_superuser)
def comment_approval_page(request):
    comments = Comment.objects.filter(is_approved=False )

    
    forms = []

    if request.method == 'POST':
        # Handle form submissions
        for comment in comments:
            form = CommentApprovalForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('comment_approval_page')

    else:
        # Display comments and forms
        for comment in comments:
            forms.append(CommentApprovalForm(instance=comment))
    return render(request, 'comment_approval_page.html', {'comments': comments, 'forms': forms})
>>>>>>> master

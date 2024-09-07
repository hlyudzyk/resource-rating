from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import LinkForm, ReviewForm
from .models import Link

def detail(request, pk):
    link = get_object_or_404(Link,pk=pk)
    return render(
        request,
        'link/detail.html',
        {
            'link': link
        }
    )

@login_required
def add_link(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            link = form.save()
            return redirect('link:detail',pk=link.pk)

    else:
        form = LinkForm()

    return render(request, 'link/add_link.html', {'form': form})

@login_required
def add_review(request,pk):
    link = get_object_or_404(Link,pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.link = link
            review.user = request.user
            review.save()
            return redirect('link:detail',pk=link.pk)
    else:
        form = ReviewForm()
        return render(request, 'link/add_review.html', {'form': form})



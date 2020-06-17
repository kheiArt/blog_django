from django.shortcuts import render


def posts_list(request):
    n = ['Dasha', 'Moshe', 'Semen']
    return render(request, 'blog/index.html', context={'names': n})

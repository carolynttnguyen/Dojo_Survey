from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')


def survey(request):
    if request.method == 'GET':
        return redirect('/')
    request.session['answers'] = {
        'name': request.POST['name'],
        'location': request.POST['location'],
        'language': request.POST['language'],
        'comment': request.POST['comment']
    }
    return redirect('/result')


def result(request):
    context = {
        'answer': request.session['answers']
    }
    return render(request, 'result_page.html', context)

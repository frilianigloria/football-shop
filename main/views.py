from django.shortcuts import render

def show_main(request):
    context = {
        'appname' : 'Football Shop',
        'name': 'Friliani Gloria',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)

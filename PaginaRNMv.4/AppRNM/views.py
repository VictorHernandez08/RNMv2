from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'AppRNM/index.html')



def about(request):

    return render(request, 'AppRNM/about.html')


def work(request):

    return render(request, 'AppRNM/work.html') 




def contact(request):

    return render(request, 'AppRNM/contact.html') 
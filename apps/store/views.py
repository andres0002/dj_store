from django.shortcuts import render

# Create your views here.

def store(request, *args, **kwargs):
    template_name = 'store.html'
    # print(request.path)
    return render(request, template_name)
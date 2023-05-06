from django.shortcuts import render


# Create your views here.
def compete(request):
    return render(request, 'compete.html')



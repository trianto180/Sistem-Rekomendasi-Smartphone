from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def rekomendasi(request):
    return render(request, 'rekomendasi.html')
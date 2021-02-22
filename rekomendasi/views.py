from django.shortcuts import render
from rekomendasi.models import Smartphone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def smartphone(request):
    smartphones = Smartphone.objects.all()
    page = request.GET.get('page')

    paginator = Paginator(smartphones, 9)
    try:
        smartphones = paginator.page(page)
    except PageNotAnInteger:
        smartphones = paginator.page(1)
    except EmptyPage:
        smartphones = paginator.page(paginator.num_pages)


    konteks = {
        'smartphones': smartphones,
    }
    return render(request, 'smartphone.html', {'smartphones': smartphones}, konteks)

def rekomendasi(request):
    return render(request, 'rekomendasi.html')
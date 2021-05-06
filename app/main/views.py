from .models import *
from django.shortcuts import render, get_object_or_404
from .forms import AstheniaForm


# Create your views here.
def title_view(request):
    astheniesList = Asthenia.objects.all().order_by('onoma')
    context = {
        'astheniesList': astheniesList
    }
    return render(request, "main/titles.html", context)


def info_view(request, id):
    asthenia = get_object_or_404(Asthenia, id=id)
    xaraktiristika=Xaraktiristika.objects.filter(asthenia=asthenia.id)
    sxolio=Sxoleio.objects.filter(asthenia=asthenia.id)
    ekpedeftikoi=Ekpedeftikoi.objects.filter(asthenia=asthenia.id)
    goneis=Goneis.objects.filter(asthenia=asthenia.id)
    perisotera=Perisotera.objects.filter(asthenia=asthenia.id)
    
    
    context={
        'asthenia':asthenia,
        'xaraktiristika':xaraktiristika,
        'sxolio':sxolio,
        'ekpedeftikoi':ekpedeftikoi,
        'goneis':goneis,
        'perisotera':perisotera,
    }
    return render(request, "main/info.html", context)

def edit_content(request, id):
    asthenia = get_object_or_404(Asthenia, id=id)
    xaraktiristika=Xaraktiristika.objects.filter(asthenia=asthenia.id)
    sxolio=Sxoleio.objects.filter(asthenia=asthenia.id)
    ekpedeftikoi=Ekpedeftikoi.objects.filter(asthenia=asthenia.id)
    goneis=Goneis.objects.filter(asthenia=asthenia.id)
    perisotera=Perisotera.objects.filter(asthenia=asthenia.id)
    
    
    context={
        'asthenia':asthenia,
        'xaraktiristika':xaraktiristika,
        'sxolio':sxolio,
        'ekpedeftikoi':ekpedeftikoi,
        'goneis':goneis,
        'perisotera':perisotera,
    }
    # onoma=request.POST.get('onoma')
    # Asthenia.objects.get(id=id)
    # asthenia = get_object_or_404(Asthenia, id=id)
    # xaraktiristika=Xaraktiristika.objects.filter(asthenia=asthenia.id)
    # context={
    #     'form':form
    # }
    return render(request, "main/edit.html", context)

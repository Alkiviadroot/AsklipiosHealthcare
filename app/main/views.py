from django.http.response import HttpResponseRedirect
from .models import *
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import FormView
from django.urls import reverse
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from . import forms 


def title_view(request):
    astheniesList = Asthenia.objects.all().order_by('onoma')
    context = {
        'astheniesList': astheniesList
    }
    return render(request, "main/titles.html", context)


def info_view(request, pk):
    asthenia = get_object_or_404(Asthenia, id=pk)
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

@login_required
def add_content(request):
    if request.method == 'POST':
        form = forms.AstheniaForm(request.POST)
        if form.is_valid():
            form.save()
            onoma = form.cleaned_data['onoma']
            asthenia = get_object_or_404(Asthenia, onoma=onoma)
            return redirect("/"+str(asthenia.id))
    return render(request, "main/add.html", {})


@login_required
def Edit_Info(request, pk):
        obj= get_object_or_404(Asthenia, id=pk)
        
        form = forms.AstheniaForm(request.POST or None, instance= obj)
        context= {'form': form}

        if form.is_valid():
            obj= form.save(commit= False)
            obj.save()
            messages.success(request, "Αποθηκεύτηκε")
            context= {
                    'form': form,
                    }
        return render(request, 'main/edit/edit_info.html', context)

@login_required
def delete(request, pk):
    obj= get_object_or_404(Asthenia, id=pk)
    if request.method=="POST":
        obj.delete()
        return redirect('/')
    context={
        'item':obj,
    }
    return render(request,'main/delete.html',context)

class Edit_Xaraktiristika(SingleObjectMixin, FormView):
    model = Asthenia
    template_name = 'main/edit/edit_xaraktiristika.html'
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Asthenia.objects.all())
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Asthenia.objects.all())
        return super().post(request, *args, **kwargs)
    
    def get_form(self, form_class=None):
        return forms.AstheniaXaraktitistikaFormset(**self.get_form_kwargs(), instance=self.object)
    
    def form_valid(self, form):
        form.save()
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Αποθηκεύτηκε'
        )
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self):
        return reverse('main:edit_xaraktiristika', kwargs={'pk':self.object.pk})
    
class Edit_Sxoleio(SingleObjectMixin, FormView):
    model = Asthenia
    template_name = 'main/edit/edit_sxoleio.html'
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Asthenia.objects.all())
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Asthenia.objects.all())
        return super().post(request, *args, **kwargs)
    
    def get_form(self, form_class=None):
        return forms.AstheniaSxoleioFormset(**self.get_form_kwargs(), instance=self.object)
    
    def form_valid(self, form):
        form.save()
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Αποθηκεύτηκε'
        )
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self):
        return reverse('main:edit_sxoleio', kwargs={'pk':self.object.pk})
    
class Edit_Ekpedeftikoi(SingleObjectMixin, FormView):
    model = Asthenia
    template_name = 'main/edit/edit_ekpedeftikoi.html'
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Asthenia.objects.all())
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Asthenia.objects.all())
        return super().post(request, *args, **kwargs)
    
    def get_form(self, form_class=None):
        return forms.AstheniaEkpedeftikoiFormset(**self.get_form_kwargs(), instance=self.object)
    
    def form_valid(self, form):
        form.save()
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Αποθηκεύτηκε'
        )
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self):
        return reverse('main:edit_ekpedeftikoi', kwargs={'pk':self.object.pk})
    
class Edit_Goneis(SingleObjectMixin, FormView):
    model = Asthenia
    template_name = 'main/edit/edit_goneis.html'
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Asthenia.objects.all())
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Asthenia.objects.all())
        return super().post(request, *args, **kwargs)
    
    def get_form(self, form_class=None):
        return forms.AstheniaGoneisFormset(**self.get_form_kwargs(), instance=self.object)
    
    def form_valid(self, form):
        form.save()
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Αποθηκεύτηκε'
        )
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self):
        return reverse('main:edit_goneis', kwargs={'pk':self.object.pk})
    
class Edit_Sindesmoi(SingleObjectMixin, FormView):
    model = Asthenia
    template_name = 'main/edit/edit_sindesmoi.html'
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Asthenia.objects.all())
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Asthenia.objects.all())
        return super().post(request, *args, **kwargs)
    
    def get_form(self, form_class=None):
        return forms.AstheniaPerisoteraFormset(**self.get_form_kwargs(), instance=self.object)
    
    def form_valid(self, form):
        form.save()
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Αποθηκεύτηκε'
        )
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self):
        return reverse('main:edit_sindesmoi', kwargs={'pk':self.object.pk})
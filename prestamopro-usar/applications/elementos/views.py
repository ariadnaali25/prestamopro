from django.shortcuts import render, redirect

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .models import Prestamo
from .forms import PrestamoForm


# Create your views here.
#class ViewElements(TemplateView):
#    template_name="elementos/index.html"

class ListOfelements(ListView):
    model = Prestamo
    template_name = "elementos/list.html"
    context_object_name = "listaprestamos"

def prestamo_form(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listaprestamo')  # Redireccionar a la lista después de guardar
    else:
        form = PrestamoForm()
    return render(request, 'elementos/index.html', {'form': form})
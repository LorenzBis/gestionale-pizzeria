"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from prodotti.models import Prodotto
from ordini.forms import OrdineForm
from ordini.models import Ordine
from clienti.models import Cliente

def menu_view(request):
    # Lista di pizze 
    menu = Prodotto.objects.all()
    return render(request, 'menu.html', {'menu': menu})

def ordine_view(request):
    if request.method == 'POST':
        form = OrdineForm(request.POST)
        if form.is_valid():
            cliente, created = Cliente.objects.get_or_create(
                email=form.cleaned_data['email'],
                defaults={
                    'nome': form.cleaned_data['nome'],
                    'telefono': form.cleaned_data['telefono'],
                }
            )

            Ordine.objects.create(
                cliente = cliente,
                prodotto= form.cleaned_data['prodotto'],
                quantita= form.cleaned_data['quantita'],
            )
            return render(request, 'grazie.html')
    
    else:
        form = OrdineForm()
    
    return render(request, 'ordine.html', {'form': form})

urlpatterns = [
    path('', lambda request: render(request, 'home.html')),
    path('admin/', admin.site.urls),
    path('menu/', menu_view),
    path('ordine/', ordine_view, name='ordine'),
    path('grazie/', lambda request: render(request, 'grazie.hmtl'), name='grazie'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

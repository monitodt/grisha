from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import ClientForm

from django.shortcuts import render
from .models import Client

def Client_list (request):
    clients = Client.objects.order_by('id')
    return render(request, 'my_app/Client_list.html', {'clients': clients})

def RentContract_list (request):
    html = "<html><body><H1>Второе представление на джанго выполнилось</H1></body></html>"
    return HttpResponse(html)

def Premises_list (request):
    html = "<html><body><H1>Третье представление на джанго выполнилось</H1></body></html>"
    return HttpResponse(html)

def Client_edit(request):
    if request.method == "POST":
      form = ClientForm(request.POST)
      if form.is_valid():
          post = form.save(commit=False)
          post.author = request.user
          post.save()
          return redirect('../../')
    else:
      form = ClientForm()
      return render(request, 'my_app/client_edit.html', {'form': form})

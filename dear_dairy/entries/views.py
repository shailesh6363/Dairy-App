from django.shortcuts import render,redirect
from .models import Entries
from django.contrib import messages
from .forms import EntryForm
# Create your views here.
def index(request):
    entries = Entries.objects.all()
    context = {'entries': entries,'title':Entries.title,'text':Entries.text,'name':Entries.name,'date':Entries.date}

    return render(request,'entries/index.html',context)


def add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'Your Quote Is Successfully Posted!!')

           # return redirect('home')
    else:
        form = EntryForm()

    context = {'form' : form}

    return render(request, 'entries/add.html', context)
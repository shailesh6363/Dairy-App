from django.shortcuts import render, redirect
from .models import Entries
from django.contrib import messages
from .forms import EntryForm

# Create your views here.
def index(request):
    entries = Entries.objects.all()
    context = {
        "entries": entries,
        "title": Entries.title,
        "text": Entries.text,
        "name": Entries.name,
        "date": Entries.date,
    }

    return render(request, "entries/index.html", context)


# def add(request):
#     if request.method == 'POST':
#         form = EntryForm(request.POST)

#         if form.is_valid():
#             form.save()
#             messages.success(request,'Your Quote Is Successfully Posted!!')

#            # return redirect('home')
#     else:
#         form = EntryForm()

#     context = {'form' : form}

#     return render(request, 'entries/add.html', context)


def add(request):
    context = {}
    if request.method == "POST":
        title_data = request.POST.get("title")
        name_data = request.POST.get("name")
        quote_data = request.POST.get("quote")

        entry_object = Entries(title=title_data, text=quote_data, name=name_data)
        entry_object.save()
        context["msg"] = "entry has been saved"
        return render(request, "entries/add.html", context)
    else:
        return render(request, "entries/add.html")

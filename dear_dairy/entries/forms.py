from django.forms import ModelForm
from .models import Entries

class EntryForm(ModelForm):
    class Meta:
        model = Entries
        fields = ('title','name','text' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class' : 'form-control', 'placeholder' : 'Enter Your Title'})
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Your Name'})
        self.fields['text'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your Quote'})
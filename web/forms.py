from django import forms
from web.models import Book, Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publish_date', 'summary', 'page_count', 'language', 'available']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-title', 'placeholder': 'Enter book title'}),
            'publish_date': forms.DateInput(attrs={'class': 'input-date', 'type': 'date'}),
            'summary': forms.Textarea(attrs={'class': 'input-summary', 'rows': 4, 'placeholder': 'Enter book summary'}),
            'page_count': forms.NumberInput(attrs={'class': 'input-page-count', 'placeholder': 'Enter number of pages'}),
            'language': forms.TextInput(attrs={'class': 'input-language', 'placeholder': 'Enter language'}),
            'available': forms.CheckboxInput(attrs={'class': 'input-available'}),
        }
    
        author = forms.ModelChoiceField(queryset=Author.objects.all(), 
                                    widget=forms.Select(attrs={'class': 'input-author', 'placeholder': 'Select author'}))

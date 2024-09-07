from django import forms
from .models import Link,Review

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['name', 'url']
        widgets = {
            'name':forms.TextInput(attrs={'class':'py-4 px-6 bg-slate-100 '
                                                  'border border-slate-300 w-full rounded-xl mt-2'}),
            'url': forms.URLInput(attrs={'class': 'py-4 px-6 bg-slate-100 '
                                                    'border border-slate-300 w-full rounded-xl mt-2'}),

        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'content']
        widgets = {
            'rating':forms.NumberInput(attrs={'class':'py-4 px-6 bg-slate-100 '
                                                  'border border-slate-300 w-full rounded-xl mt-2'}),
            'content':forms.Textarea(attrs={'class':'py-4 px-6 bg-slate-100 '
                                                  'border border-slate-300 w-full rounded-xl mt-2'})
        }
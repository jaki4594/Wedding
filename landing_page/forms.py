from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
guest_number = [
        ('', 'How many guests?'),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
]

class GuestForm(forms.Form):
    name = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Your name'}))
    # guests = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)],label="",widget=forms.NumberInput(attrs={'placeholder':'How many guests you bring?'}))
    # guests = forms.ChoiceField(choices=[(x,x)for x in range(1,5)].insert('','Test'))
    guests = forms.ChoiceField(label="",choices=guest_number)#widget=forms.NumberInput(attrs={'placeholder':'How many guests you bring?'})
    message = forms.CharField(required=False,label="",widget=forms.Textarea(attrs={'placeholder':'Your message (optional)'}))
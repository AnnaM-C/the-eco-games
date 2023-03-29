from django import forms 
from .models import *
import random

# TO DO: reshuffle everytime app is launched or reshuffle everytime page is reloaded in view? I have functionality for both
# PROS and CONS
# Filtering in form; advantage is if user comes back to page it won't change; disadvantage is won't get variety
# Filtering in view; advantage is that user is presented with other options more frequently

class UserActivityForm(forms.ModelForm):

    # items = list(Activity.objects.all())

    # random_items = random.sample(items, 3)

    # queryset=Activity.objects.filter(id__in=[getattr(id,'id') for id in random_items])

    activities = forms.ModelMultipleChoiceField(queryset=Activity.objects.all(),widget=forms.CheckboxSelectMultiple)
    
    # create meta class

    class Meta:

        model = ActivityLog
        fields = ['date', 'challenger', 'activities']
        widgets= {
            'challenger': forms.HiddenInput(),
        }
        date=forms.DateField()
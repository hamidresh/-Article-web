# forms.py
from django import forms
from .models import Essay , Comment

class EssayForm(forms.ModelForm):
    class Meta:
        model = Essay
        exclude = ['author']

    def __init__(self, *args, **kwargs):
        super(EssayForm, self).__init__(*args, **kwargs)
        if 'author' in self.fields:
            self.fields['author'].widget.attrs['readonly'] = True 


class CommentApprovalForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['is_approved']
        
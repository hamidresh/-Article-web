# forms.py
from django import forms
from .models import Essay , Comment

class EssayForm(forms.ModelForm):
    class Meta:
        model = Essay
        exclude = ['author']  # Exclude the author field from the form

    def __init__(self, *args, **kwargs):
        super(EssayForm, self).__init__(*args, **kwargs)
        # Check if 'author' is in self.fields before setting readonly attribute
        if 'author' in self.fields:
            self.fields['author'].widget.attrs['readonly'] = True  # Make the author field non-editable


class CommentApprovalForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['is_approved']
        
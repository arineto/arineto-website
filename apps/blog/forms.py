from django import forms
from apps.blog.models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('post', 'author', 'email', 'website', 'content',)
        widgets = {
            'content': forms.Textarea(attrs={'rows': 6}),
        }

    def __init__(self, post=None, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['post'].widget = forms.HiddenInput()
        if post:
            self.fields['post'].initial = post

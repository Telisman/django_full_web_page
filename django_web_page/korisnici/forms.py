from django import forms
from .models import Post,Comment,TaskCategory

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('task_title','task_discription','task_category','recommended_tools','budget','postUser',)
        widgets = {
            # 'postUser': forms.Select(attrs={'class':'form-control'}),
            'postUser': forms.TextInput(attrs={'class': 'form-control','value':'', 'id':'user','type':'hidden'}),
            'task_title': forms.TextInput(attrs={'class':'form-control'}),
            'task_discription': forms.Textarea(attrs={'class':'form-control'}),
            'task_category': forms.Select(attrs={'class':'form-control'}),
            'recommended_tools': forms.TextInput(attrs={'class':'form-control'}),
            'budget': forms.NumberInput(attrs={'min': '0', 'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(PostForm, self).__init__(*args, **kwargs)
        self.initial['task_category'] = self.request

class updatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('task_discription','recommended_tools','budget')
        widgets = {
            'task_discription': forms.Textarea(attrs={'class':'form-control'}),
            'recommended_tools': forms.TextInput(attrs={'class':'form-control'}),
            'budget': forms.NumberInput(attrs={'min': '0', 'class': 'form-control'}),
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body','user','Mid')
        widgets = {
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'post': forms.Select(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'user': forms.TextInput(attrs={'class':'form-control'}),
            'Mid': forms.NumberInput(attrs={'class':'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['user'].label = "Your name:"
        self.fields['user'].initial = self.request.user.username
        self.fields['Mid'].initial = self.request.user.pk
        self.fields['user'].widget.attrs['readonly'] = True
        self.fields['Mid'].widget.attrs['readonly'] = True
        self.fields['Mid'].widget = forms.HiddenInput()
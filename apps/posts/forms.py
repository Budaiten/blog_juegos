from django import forms    
from .models import Post
from django.forms import Textarea

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NuevoPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('categoria', 'titulo', 'subtitulo', 'texto', 'imagen', 'autor')

        widgets = {
            'categoria':forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'titulo': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'subtitulo': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'texto': Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'imagen': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
        }

        def save(self, commit=True):
            if hasattr(self, 'request') and self.request.user.is_authenticated:
                self.instance.autor = self.request.user
            return super().save(commit)
class EditarPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'subtitulo', 'texto', 'imagen')

        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'subtitulo': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'texto': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'imagen': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
        }

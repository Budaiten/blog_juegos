from django import forms    
from .models import Post

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NuevoPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('categoria', 'titulo', 'subtitulo', 'texto', 'imagen','fecha')

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
            'texto': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'imagen': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'fecha': forms.DateTimeField(attrs={
                'class': INPUT_CLASSES
            }),
        }

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

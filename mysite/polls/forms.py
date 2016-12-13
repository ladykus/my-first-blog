from django import forms #импорт формы django
from .models import Post #импорт модели

class PostForm(forms.ModelForm): #PostForm имя формы
	class Meta:
		model = Post #какая модель используется
		fields = ('title', 'text',) #поля формы
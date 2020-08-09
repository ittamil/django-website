from django.forms import ModelForm
from django import forms
#from ittamilapp.models import CommentModel, PostModel, UserModel, UserDashBoardModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from ittamilapp.models import AuthorProfileModel
from ckeditor.widgets import CKEditorWidget
from ittamilapp.models import Comment, PostModel, UserModel, UserDashBoardModel

#class CommentForm(ModelForm):
#    class Meta:
#        model = CommentModel
#        fields = {  
#            'name',          
#            'email',
#            'body',
#        }
#
class UserDashBoardForm(ModelForm):
    class Meta:
        model = PostModel
        fields = {            
            'author',
            'title',
            'slug',
            'cover_image',
            'content',
            'status',
        }  
               

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = UserModel
        fields = {
            'first_name',
            'last_name',  
            'username',
           }

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.username=self.cleaned_data['username']
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        if commit:
            user.save()
        return user    

class EditProfileForm(UserChangeForm):
    class Meta:
        model = AuthorProfileModel
        fields = {
            'last_name',
            'first_name',
            'About_Yourself',
            'FaceBook_Profile',
            'Github_Profile',
            'Instagram_Profile',
            'LinkedIn_Profile',
            'Telegram_Profile',
            'UG_Degree_Name',
            'Skill',
        }
            


class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Text goes here!!!', 'rows':'4', 'cols':'50'}))
    class Meta:
        model = Comment
        fields = ('content',)
from django import forms


class UserDataForm(forms.Form):
    user_name = forms.CharField(label='Name', max_length=20)
    email = forms.EmailField(label='Email')
    weight = forms.IntegerField(label='Weight', min_value=0, max_value=300)
    gender = forms.ChoiceField(label='Gender', choices=[('male','male'), ('female','female')],widget=forms.RadioSelect())

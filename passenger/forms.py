from django import forms
from .models import UserAccount
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm ,UserChangeForm
class UserAccountForm(UserCreationForm):
    nid = forms.CharField(required=True,max_length=6)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name' , 'email','nid']

    def save(self, commit=True):
        our_user = super().save(commit=False)
        # email = self.cleaned_data['email']
        if commit == True:
            our_user.is_active = False
            our_user.save() 
            nid = self.cleaned_data.get('nid')
            UserAccount.objects.create(
                user = our_user,
                nid = nid,
            )
        return our_user
    

class UserAccountChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password')
        


class DepositForm(forms.ModelForm):
    amount = forms.DecimalField(decimal_places=2, max_digits=12)
    class Meta:
        model = UserAccount
        fields = [
            'amount'
        ]
        
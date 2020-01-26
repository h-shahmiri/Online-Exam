from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control col-md-8","id":"regname","placeholder":"Username"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control col-md-8","id":"reglname","placeholder":"Password"
    }))



class RegisterForm(forms.Form):
    firstname = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control col-md-8", "id":"firstname", "placeholder":"First"
    }))
    lastname = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control col-md-8", "id":"lastname", "placeholder":"Last"
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control col-md-8", "id":"reglname", "placeholder":"Username"
    }))
    email    = forms.EmailField(widget=forms.TextInput(attrs={
        "class":"form-control col-md-8", "id":"regemail", "placeholder":"Email@gmail.com"
    }))

    def email_valid(self):
        emails = self.cleaned_data['email']
        if "gmail.com" not in emails:
            raise forms.ValidationError("Pls use @gmail.com")
        return emails

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control col-md-8","id":"regpass"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control col-md-8","id":"regpass2"
    }))

    def pass_valid(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError("Passwords is not match")
        return password1

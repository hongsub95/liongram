from django import forms
from users import models as users_models


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "패스워드를 적어주세요"}),label="패스워드")
    
    class Meta:
        model = users_models.User
        fields = ("email",)
        widgets = {
            "email": forms.EmailInput(attrs={"placeholder": "이메일을 적어주세요"})
        }
    
    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = users_models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("이메일 혹은 패스워드가 틀립니다"))
        except users_models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("이메일 혹은 패스워드가 틀립니다"))


class SignupForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "패스워드를 입력해 주세요"}),
        label="비밀번호 1차",
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "다시 패스워드를 입력해 주세요"}),
        label="비밀번호 2차",
    )

    class Meta:
        model = users_models.User
        fields = ("email","first_name","gender","phone","birthday")
        widgets = {
            "email": forms.TextInput(attrs={"placeholder": "이메일을 입력해 주세요"}),
            "first_name":forms.TextInput(attrs={"placeholder":"이름을 적어주세요"}),
            "phone":forms.TextInput(attrs={"placeholder":"전화번호를 입력해주세요"}),
        }
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            users_models.User.objects.get(email=email)
            raise forms.ValidationError("이미 가입된 이메일 입니다")
        except users_models.User.DoesNotExist:
            return email

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password != password1:
            raise forms.ValidationError("패스워드가 일치하지 않습니다")
        else:
            return password
    
    def save(self):
        user = super().save(commit=False)
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user.username = email
        user.set_password(password)
        user.save()
    
        

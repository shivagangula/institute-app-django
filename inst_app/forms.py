from django import forms
from multiselectfield import MultiSelectFormField
class RegForm(forms.Form):
    frist_name = forms.CharField(
        label='enter your name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your name'
            }
        )
    )
    last_name = forms.CharField(
        label='enter your last name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your last name'
            }
        )
    )
    username = forms.CharField(
        label='enter your username',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your username'
            }
        )
    )
    password1 = forms.CharField(
        label='enter your password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your password'
            }
        )
    )
    password2 = forms.CharField(
        label='re enter your password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 're enter your password'
            }
        )
    )
    email = forms.EmailField(
        label='enter your email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your email'
            }
        )
    )
    mobile = forms.IntegerField(
        label='enter your mobile number',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your number'
            }
        )
    )
    dob = forms.DateTimeField(
        label='enter your name',
        widget=forms.DateTimeInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your dob'
            }
        )
    )



class LoginForm(forms.Form):
    username = forms.CharField(
        label='enter your username',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'enter your username'
            }
        )
    )
    password = forms.CharField(
        label='enter your username',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'enter your password'
            }
        )
    )


class StudentForm(forms.Form):
    name = forms.CharField(
        label='enter your name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your name'
            }
        )
    )
    mobile = forms.IntegerField(
        label='enter your mobile number',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'enter Mobile number'
            }
        )
    )
    email = forms.EmailField(
        label='enter your email',
         widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'enter email'
            }
        )
    )
    COURSE_CHOICES =(
                        ('python','PYTHON'),
                        ('django','DJANGO'),
                        ('rest API','REST API'),
                        ('UI','UI')
                                   )
    courses = MultiSelectFormField(max_length=200,choices=COURSE_CHOICES)
    TRAINER_CHOICES = (
                   ('sai', 'SAI'),
                   ('shiva', 'SHIVA'),
                   ('ganesh', 'GANESH'),
                   ('mahesh', 'MAHESH')
    )
    trainer = MultiSelectFormField(max_length=200, choices=TRAINER_CHOICES)
    TIMING_CHOICES = (
                   ('morning', 'MORNING'),
                   ('afternoon', 'AFTERNOON'),
                   ('evening', 'EVENINHG')
    )
    timings = MultiSelectFormField(max_length=200, choices=TIMING_CHOICES)
    start_date = forms.DateField(
        widget= forms.SelectDateWidget()
    )

class FeedBackForm(forms.Form):
    name = forms.CharField(
        label='enter your name',
        widget=forms.TextInput(
            attrs={
            'class':'form-control',
            'placeholder':'name'
            }

                              )
                )
    rating = forms.IntegerField(
        label='enter your rating',
        widget=forms.NumberInput(
            attrs={
            'class':'form-control',
            'placeholder':'rating'
            }

        )
    )

    feedback = forms.CharField(
        label='enter your Feedback',
        widget=forms.Textarea(
            attrs={
            'class':'form-control',
            'placeholder':'Feedback'
            }

        )
    )
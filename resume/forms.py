from django import forms
from .models import Resume
GRNDER_CHOICES=[
    ('Male','Male'),
    ('Female','Femail')
]
JOB_CHOICES=[
    ('Delhi',"Delhi"),
    ('Pune','Pune'),
    ('Mumbai','Mumbai'),
    ('Gujarat','Gujarat')
]
class ResumeForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=GRNDER_CHOICES,widget=forms.RadioSelect)
    job_city=forms.MultipleChoiceField(label='Preferred job city',choices=JOB_CHOICES,widget=forms.CheckboxSelectMultiple)
    
    class Meta:
        model = Resume
        fields = ('name','dob','gender','locality','city','pin','state','mobile','email','job_city','profile_image','my_file')
        labels={'name':'Full Name','dob':"Date of Birth",'locality':'Village','pin':'Pin Code',"mobile":'Mobile No.','email':'Email ID','profile_image':'Profile Image','my_file':'Documents'}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-select'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})
        }


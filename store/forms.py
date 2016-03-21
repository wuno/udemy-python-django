from django import forms 

class ReviewForm(forms.Form):
	text= forms.CharField(widget=forms.Textarea, label='')
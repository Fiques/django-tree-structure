from django import forms
from .models import Company


class CompanyForm(forms.ModelForm):
	parent = forms.CharField(widget=forms.HiddenInput(
		attrs={'class': 'parent'}), required=False)

	class Meta:
		model = Company
		fields = ('name', 'earnings',)

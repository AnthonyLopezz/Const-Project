from StoreApp.models import Product, CategoryProd
from django import forms


class FormProduct(forms.ModelForm):
    name = forms.CharField(label="Name", required=True, max_length=25,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label="Description", required=True, max_length=500,
                                  widget=forms.Textarea(attrs={'class': 'form-control'}))
    platform = forms.CharField(label="Size", required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    classification = forms.CharField(label="Type", required=True,
                                     widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.IntegerField(label="Price", required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        fields = {'name',
                  'category',
                  'image',
                  'description',
                  'platform',
                  'classification',
                  'price'}


class FormService(forms.ModelForm):
    title = forms.CharField(label="Title", required=True, max_length=25,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label="Content", required=True, max_length=500,
                                  widget=forms.Textarea(attrs={'class': 'form-control'}))
    link = forms.CharField(label="Link", required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        fields = {'title',
                  'content',
                  'link',
                  'image'}

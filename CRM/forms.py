# -*- encoding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User, Group
from CRM.models import *

class EventForm(forms.ModelForm):
    dt = forms.DateTimeField(label=u'Дата', widget = forms.HiddenInput())
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(), label=u'Кому', widget = forms.HiddenInput())

    class Meta:
        fields = ('customer', 'name', 'dt', 'place')
        model = Calendar

class CustomerForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.filter(is_superuser=False), empty_label=None, label=u'Владелец', to_field_name='id')

    class Meta:
        fields = ('user', 'name', 'photo','phone','mob_phone','other_phone','email','skype','note')
        model = Customer

# FILE_TYPE = (
#     (1, 'Списания'),
#     (2, 'Начисления'),
# )
# class UploadForm(forms.ModelForm):
#     _type = forms.ChoiceField(label=u'Тип файла', required=True, choices=FILE_TYPE)

#     class Meta:
#         fields = ('fd', 'td', '_file',)
#         model = FileUpload

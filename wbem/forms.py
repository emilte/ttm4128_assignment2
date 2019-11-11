from django import forms
from pywbem import WBEMConnection



class ClassForm(forms.Form):

    classname = forms.CharField(max_length=200, required=False)
    #namespace = forms.CharField(max_length=200, required=False)
    #instance = forms.CharField(max_length=200, required=False)
    #other_var = forms.CharField(max_length=200, required=False)

    function_choices = [
        (1, 'EnumerateClassNames'),
    ]
    function = forms.ChoiceField(choices=function_choices)

    def __init__(self, *args, **kwargs):
        super(ClassForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class EiForm(forms.Form):
    # Order is important

    classname = forms.CharField(max_length=200, required=True)
    namespace = forms.CharField(max_length=200, required=False)
    deep_inheritance = forms.BooleanField(initial=True, required=False)
    include_qualifiers = forms.BooleanField(required=False)
    include_class_origin = forms.BooleanField(required=False)

    required_css_class = 'required'

    method = 'EnumerateInstances'


    def __init__(self, *args, **kwargs):
        super(EiForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class EinForm(forms.Form):
    # Order is important

    classname = forms.CharField(max_length=200, required=True)
    namespace = forms.CharField(max_length=200, required=False)

    required_css_class = 'required'

    method = 'EnumerateInstanceNames'


    def __init__(self, *args, **kwargs):
        super(EinForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})



class GiForm(forms.Form):
    # Order is important

    instance_name = forms.CharField(max_length=200, required=True)
    include_class_origin = forms.BooleanField(required=False)

    required_css_class = 'required'

    method = 'GetInstance'
    short_name = 'gi'


    def __init__(self, *args, **kwargs):
        super(GiForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class EcnForm(forms.Form):
    # Order is important
    namespace = forms.CharField(max_length=200, required=False)
    classname = forms.CharField(max_length=200, required=False)
    deep_inheritance = forms.BooleanField(initial=False, required=False)

    required_css_class = 'required'

    method = 'EnumerateClassNames'
    short_name = 'ecn'

    def __init__(self, *args, **kwargs):
        super(EcnForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class GcForm(forms.Form):
    # Order is important
    ClassName = forms.CharField(max_length=200, required=True)
    namespace = forms.CharField(max_length=200, required=False)
    LocalOnly = forms.BooleanField(initial=True, required=False)
    IncludeQualifiers = forms.BooleanField(required=False)
    IncludeClassOrigin = forms.BooleanField(required=False)


    required_css_class = 'required'

    method = 'GetClass'
    short_name = 'gc'

    def __init__(self, *args, **kwargs):
        super(type(self), self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

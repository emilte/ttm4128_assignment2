from django import forms

class EiForm(forms.Form):
    # Order is important

    classname = forms.CharField(max_length=200, required=True)
    namespace = forms.CharField(max_length=200, required=False)
    deep_inheritance = forms.BooleanField(initial=True, required=False)
    include_qualifiers = forms.BooleanField(required=False)
    include_class_origin = forms.BooleanField(required=False)

    required_css_class = 'required'

    method = 'EnumerateInstances'
    short_name = 'ei'

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
    short_name = 'ein'

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


class EqForm(forms.Form):
    # Order is important
    namespace = forms.CharField(max_length=200, required=False)

    required_css_class = 'required'

    method = 'EnumerateQualifiers'
    short_name = 'eq'

    def __init__(self, *args, **kwargs):
        super(type(self), self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class GqForm(forms.Form):
    # Order is important
    QualifierName = forms.CharField(max_length=200, required=True)
    namespace = forms.CharField(max_length=200, required=False)

    required_css_class = 'required'

    method = 'GetQualifier'
    short_name = 'gq'

    def __init__(self, *args, **kwargs):
        super(type(self), self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class NetworkForm(forms.Form):
    INFO_CHOICES = [("mac_address","MAC Address"),("general","Interface info")]
    IFACE_CHOICES= [("eth0","IPv4_eth0"	),("lo","IPv4_lo")]
    interfaces_choice = forms.CharField(label='Which interface would you like information about?', widget=forms.Select(attrs={'class':'form-control'},choices=IFACE_CHOICES))
    interface_info_pre= forms.MultipleChoiceField(label="What info do you want from the interface?", widget=forms.CheckboxSelectMultiple, choices=INFO_CHOICES)






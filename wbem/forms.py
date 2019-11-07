from django import forms



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

from django import forms


# Apply BootStrap to From and ModelForm

class BootStrap:
    bootstrap_exclude_fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name in self.bootstrap_exclude_fields:
                continue

            if field.widget.attrs:
                field.widget.attrs["class"] = "form-input form-control"
                field.widget.attrs["placeholder"] = field.label
            else:
                field.widget.attrs = {"class": "form-input form-control", "placeholder": field.label}


class BootStrapModelForm(BootStrap, forms.ModelForm):
    pass


class BootStrapForm(BootStrap, forms.Form):
    pass

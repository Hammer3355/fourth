from django.forms import ModelForm
from .models import Project
from django import forms


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link', 'tags']

        widgets = {'tags': forms.CheckboxSelectMultiple()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

        # self.fields['title'].widget.attrs.update({'class': 'input'})
        # self.fields['description'].widget.attrs.update({'class': 'input'})
        # self.fields['demo_link'].widget.attrs.update({'class': 'input'})
        # self.fields['source_link'].widget.attrs.update({'class': 'input'})
        # self.fields['featured_image'].widget.attrs.update({'class': 'input'})
        # self.fields['tags'].widget.attrs.update({'class': 'input'})

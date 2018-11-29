from django import forms
from .models import Image
from urllib import request
from django.core.files.base import ContentFile
from django.utils.text import slugify

class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'url', 'description')
        widgets = {
            'url' : forms.HiddenInput,
            }

    # Django allows you to define form methods to clean specific fields
    # by using the clean_<fieldname>() notation
    # we use this here to clean the url and make sure it's using a valid extension.
    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png', 'gif']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('The given URL does not match valid image extensions.')
        return url

    # we override the forms.ModelForm.save() method keeping parameters required
    # by ModelForm.
    # commit defaults to true but is changed to false on the next line
    def save(self, force_insert=False,
             force_update=False,
             commit=True):
        # create new image instance and call save() with commit=False
        image = super(ImageCreateForm,self).save(commit=False)
        # get the url from the cleaned_data dictionary
        image_url = self.cleaned_data['url']
        # create the name of the image from the title and the extension
        image_name = '{}.{}'.format(slugify(image.title),
                                    image_url.rsplit('.',1)[1].lower())
        # download image from the given URL
        response = request.urlopen(image_url)
        # save=False to avoid saving to the DB yet
        image.image.save(image_name,
                         ContentFile(response.read()),
                         save=False)
        if commit:
            image.save()
        return image

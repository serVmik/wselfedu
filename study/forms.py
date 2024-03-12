from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from english.models import WordModel


class CreateWordForm(forms.ModelForm):
    """Create word form.
    create_word_form.html
    """

    class Meta:
        model = WordModel
        fields = ['words_eng', 'words_rus']


class CrispyCreateWordForm(forms.ModelForm):
    """Create word form.
    create_word_form_crispy.html
    """

    class Meta:
        model = WordModel
        fields = ['words_eng', 'words_rus']

    @property
    def helper(self):
        helper = FormHelper()
        helper.form_id = 'id-word-list-form'
        helper.form_class = 'form-horizontal'
        helper.label_class = 'col-lg-2'
        helper.field_class = 'col-lg-8'
        helper.form_method = 'post'
        helper.form_action = 'submit_survey'

        helper.add_input(Submit('submit', 'Submit'))

        return helper
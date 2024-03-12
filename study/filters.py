import django_filters
from crispy_forms.helper import FormHelper

from english.models import WordModel


class WordFilter(django_filters.FilterSet):
    """
    path = /study/filter/
    path_name = study:crispy
    view = views_filter.word_list
    template_name = study/form_filter.html
    """

    class Meta:
        model = WordModel
        fields = {
            'word_count': ['exact'],
            'created_at': ['day__lt', 'day__gt'],
        }

    @property
    def helper(self):
        helper = FormHelper()
        helper.form_id = 'id-word-filter-form'
        helper.form_class = 'blueForms'
        helper.form_method = 'post'
        helper.form_action = 'submit_servey'


        return helper

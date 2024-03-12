from django.views.generic import CreateView

from study.forms import CreateWordForm, CrispyCreateWordForm


class CreateWordView(CreateView):
    template_name = 'study/create_word_form.html'
    form_class = CreateWordForm


class CrispyCreateWordView(CreateView):
    template_name = 'study/create_word_form_crispy.html'
    form_class = CrispyCreateWordForm

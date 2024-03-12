from django.views.generic import TemplateView


class HomeStudyView(TemplateView):
    """Home page study django view."""

    template_name = 'study/home.html'

from django.views.generic import TemplateView


class HomeView(TemplateView):

    template_name = 'landing_page/index.html'

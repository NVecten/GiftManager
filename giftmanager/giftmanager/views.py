from django.views.generic import TemplateView

from .models import Person

class Index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        return {"ahoj":Person.objects.get(name="Albert")}

class Names(TemplateView):
    template_name = "names.html"

    def get_context_data(self, **kwargs):
        return {"object":Person.objects.all()}


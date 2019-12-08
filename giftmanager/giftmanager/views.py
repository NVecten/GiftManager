from django.views.generic import TemplateView

from .models import Person, GiftToPerson

class Index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):

        for person in {"persons":Person.objects.all()}:



            '''
            for gift in {"gifts": GiftToPerson.objects.filter(person__id = person.id )}:
            pass
            '''

        return {"persons":Person.objects.all()}

class Names(TemplateView):
    template_name = "names.html"

    def get_context_data(self, **kwargs):
        return {"object":Person.objects.all()}



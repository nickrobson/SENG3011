# doc.py
# SENG3011 - Cool Bananas
#
# Reads the documentation page and presents it.

from django.template.loader import get_template
from django.http import HttpResponse

from ...utils import SingletonView

class DocView(SingletonView):

    def __init__(self):
        template = get_template('assets/api/doc.html')
        self.content = template.render()

    def get(self, request):
        return HttpResponse(self.content, content_type='text/html')

# query.py
# SENG3011 - Cool Bananas
#
# Displays homepage with list of revisions of code

from django.template.loader import get_template
from django.views import View
from django.http import HttpResponse, HttpResponseBadRequest


from ..core import gitutils

import subprocess


class HomepageView(View):
    def __init__(self):
        versionList = gitutils.get_git_tags()

        versions = []
        for versionNumber in versionList:
            dotSeparatedVersion = versionNumber.replace("_", ".")
            version = {
                'number': dotSeparatedVersion,
                'link': "https://github.com/nickrobson/SENG3011/tree/" + versionNumber,
                'tagDescription': gitutils.get_description(versionNumber),
                'downloadLink': "tag/" + dotSeparatedVersion
            }
            versions.append(version)

        template = get_template('assets/demo-webpage.html')
        self.content = template.render({'versions': versions})

    def get(self, request):
        return HttpResponse(self.content, content_type='text/html')


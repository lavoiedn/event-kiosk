from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404
from .models import Kiosk
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

class KioskView(TemplateView):

    template_name = "kiosk.html"

    def get_context_data(self, **kwargs):
        slug = kwargs['name']

        kiosk = get_object_or_404(Kiosk, name=slug)

        context = super(KioskView, self).get_context_data(**kwargs)
        context['kiosk'] = kiosk.name
        return context

@csrf_exempt
def kiosk_data(request, **kwargs):
    slug = kwargs['name']
    kiosk = get_object_or_404(Kiosk, name=slug)

    # construct the JSON representation of the kiosk

    slides = []
    for slide in kiosk.presentation.slides.all():
        slides.append(slide.to_json())

    presentation = {
        'transitionTime': kiosk.presentation.transitionTime * 1000,
        'pauseTimeOnTouch': kiosk.presentation.pauseTimeOnTouch * 1000,
        'slides': slides
    }

    kiosk = {'presentation': presentation}

    return JsonResponse(kiosk)
from django.shortcuts import get_object_or_404, redirect, render, get_list_or_404
from .models import *

class ObjectDetailMixin:
    model = None
    template = None
    def get(self, request, name):
        obj = get_object_or_404(self.model, name=name)
        context = {self.model.__name__.lower(): obj}
        return render(request, self.template, context=context)

class RenderMixin:
    template = None
    context = None
    def get(self, request):
        return render(request, self.template, context=self.context)

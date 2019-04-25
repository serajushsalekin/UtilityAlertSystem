from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView
from .forms import ComplainForm
from .models import ComplainBox


class ComplainCreate(CreateView):
    template_name = 'complain.html'
    form_class = ComplainForm
    success_url = reverse_lazy('complain')


class ComplainList(ListView):
    template_name = 'complain_list.html'
    model = ComplainBox


class ComplainDetail(DetailView):
    template_name = 'complain-details.html'
    model = ComplainBox


class ComplainDelete(DeleteView):
    model = ComplainBox


def complain_delete(request, id):
    data = dict()
    complain = get_object_or_404(ComplainBox, id=id)
    if request.method == 'POST':
        complain.delete()
        data['form_is_valid'] = True
        complainbox_list = ComplainBox.objects.all()
        data['complain_list'] = render_to_string('snippets/list_snippets.html', {'complainbox_list': complainbox_list})
    else:
        context = {'complain': complain}
        data['html_form'] = render_to_string('complain_delete.html', context, request=request)

    return JsonResponse(data)

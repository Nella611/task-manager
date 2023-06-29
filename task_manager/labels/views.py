from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.utils.translation import gettext
from django.db.models.deletion import ProtectedError
from task_manager.logger_config import logger

from task_manager.labels.models import Label
from task_manager.labels.forms import LabelForm



class LabelListView(LoginRequiredMixin, ListView):
    model = Label
    template_name = 'labels/list.html'
    context_object_name = 'labels'


class LabelCreateView(LoginRequiredMixin, CreateView):
    template_name = 'labels/create.html'
    form_class = LabelForm
    success_url = reverse_lazy('labels_list')

    def form_valid(self, form):
        logger.debug('Label status crete valid')
        form.instance.author = self.request.user
        messages.success(self.request, gettext('Метка успешно создана'))
        return super().form_valid(form)


class LabelUpdateView(LoginRequiredMixin, UpdateView):
    model = Label
    template_name = 'labels/update.html'
    form_class = LabelForm
    success_url = reverse_lazy('labels_list')

    def form_valid(self, form):
        logger.debug('Label status update valid')
        messages.success(self.request, gettext('Метка успешно изменена'))
        return super().form_valid(form)


class LabelDeleteView(LoginRequiredMixin, DeleteView):
    model = Label
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('labels_list')


    def form_valid(self, form):
        messages.success(self.request, gettext('Метка успешно удалена'))
        return super().form_valid(form)


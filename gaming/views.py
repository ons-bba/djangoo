from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Séance

class SéanceListView(ListView):
    model = Séance
    template_name = 'gaming/séance_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['joueur_connecté'] = self.request.user.username if self.request.user.is_authenticated else None
        return context

class SéanceCreateView(CreateView):
    model = Séance
    fields = '__all__'
    template_name = 'gaming/séance_form.html'
    success_url = reverse_lazy('séance-list')

class SéanceUpdateView(UpdateView):
    model = Séance
    fields = '__all__'
    template_name = 'gaming/séance_form.html'
    success_url = reverse_lazy('séance-list')

class SéanceDeleteView(DeleteView):
    model = Séance
    template_name = 'gaming/séance_confirm_delete.html'
    success_url = reverse_lazy('séance-list')

class SéanceDetailView(DetailView):
    model = Séance
    template_name = 'gaming/séance_detail.html'
    pk_url_kwarg = 'code'
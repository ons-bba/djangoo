from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from .models import Seance
from .forms import SeanceForm

class SeanceListView(ListView):
    model = Seance
    template_name = 'core/seance_list.html'
    context_object_name = 'seances'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        User = get_user_model()
        # Ici on récupère tous les joueurs actifs (is_active=True) qui ne sont pas staff
        context['joueurs_connectes'] = User.objects.filter(is_active=True, is_staff=False)
        return context

class SeanceCreateView(CreateView):
    model = Seance
    form_class = SeanceForm
    template_name = 'core/seance_form.html'
    success_url = reverse_lazy('seance_list')

class SeanceUpdateView(UpdateView):
    model = Seance
    form_class = SeanceForm
    template_name = 'core/seance_form.html'
    success_url = reverse_lazy('seance_list')

def seance_delete(request, code):
    seance = get_object_or_404(Seance, code=code)
    if request.method == 'POST':
        seance.delete()
        return redirect('seance_list')
    return render(request, 'core/seance_confirm_delete.html', {'seance': seance})

def seance_detail(request, code):
    seance = get_object_or_404(Seance, code=code)
    return render(request, 'core/seance_detail.html', {'seance': seance})

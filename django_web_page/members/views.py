from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.urls import reverse_lazy
from .forms import SingUpForm,EditProfile
from django.views.generic import DetailView
from korisnici.models import Post

class UserRegisterView(generic.CreateView):
    form_class = SingUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditProfileView(generic.UpdateView):
    form_class = EditProfile
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

      		  

    def get_object(self):
        return self.request.user


# class ShowProfile(DetailView):
#     model = Profile
#     context_object_name = 'profile'
#     template_name = 'user_profile.html'
#
#     # def get_queryset(self):  # get_queryset biblioteka iz paythona
#     #     return CustomKorisnici.objects.all()
#
#     def get_context_data(self, *args, **kwargs):
#         users = Profile.objects.all()
#         context = super(ShowProfile, self).get_context_data(*args, **kwargs)
#         page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
#         context["page_user"] = page_user
#         return context
#
#

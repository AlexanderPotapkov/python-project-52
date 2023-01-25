from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect
from django.db.models import ProtectedError

from .models import User
from .forms import Register
from task_manager.utils.texts import MessagesForUser, TitlesName

flash = MessagesForUser()
title_names = TitlesName()


class UserList(ListView):
    model = User
    context_object_name = 'users_list'
    template_name = 'users/users_list.html'


class RegisterUser(SuccessMessageMixin, CreateView):
    model = User
    form_class = Register
    template_name = 'users/create_and_update_user.html'
    success_url = reverse_lazy('login')
    success_message = flash.user_create
    extra_context = {'header': title_names.reg,
                     'button_name': title_names.to_reg}


class UpdateUser(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    form_class = Register
    template_name = 'users/create_and_update_user.html'
    success_url = reverse_lazy('users_list')
    extra_context = {'header': title_names.update_user,
                     'button_name': title_names.update}
    login_url = reverse_lazy('login')

    def test_func(self):
        user = self.get_object()
        return self.request.user.id == user.id

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        messages.success(self.request, flash.user_update)
        return redirect(self.success_url)

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            message = flash.no_rigths_for_user
            url = reverse_lazy('users_list')
        else:
            message = flash.login
            url = self.login_url
        messages.warning(self.request, message)
        return redirect(url)


class DeleteUser(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    success_url = reverse_lazy('users_list')
    template_name = 'users/delete_user.html'
    extra_context = {'deltitle': title_names.to_del_user}
    login_url = reverse_lazy('login')

    def test_func(self):
        user = self.get_object()
        return self.request.user.id == user.id

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            message = flash.no_rigths_for_user
            url = self.success_url
        else:
            message = flash.login
            url = self.login_url
        messages.warning(self.request, message)
        return redirect(url)

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(self.request, flash.user_delete)
            return redirect(self.success_url)
        except ProtectedError:
            messages.warning(self.request,
                             flash.no_delete_user)
            return redirect(success_url)

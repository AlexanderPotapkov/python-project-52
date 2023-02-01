from django.test import SimpleTestCase
from django.urls import reverse, resolve

from task_manager.apps.users.views import UsersView, \
    RegisterUser, UpdateUser, DeleteUser


class TestUsersUrls(SimpleTestCase):
    def test_user_view(self):
        url = reverse('users')
        self.assertEquals(resolve(url).func.view_class, UsersView)

    def test_user_create(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func.view_class, RegisterUser)

    def test_user_update(self):
        url = reverse('update', args='1')
        self.assertEquals(resolve(url).func.view_class, UpdateUser)

    def test_user_delete(self):
        url = reverse('delete', args='1')
        self.assertEquals(resolve(url).func.view_class, DeleteUser)

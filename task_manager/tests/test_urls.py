from django.test import SimpleTestCase
from django.urls import reverse, resolve

from task_manager.views import IndexView, LoginUser, LogoutUser


class TestTaskManagerUrls(SimpleTestCase):
    def test_main_page(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, IndexView)

    def test_login_user(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, LoginUser)

    def test_logout_user(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func.view_class, LogoutUser)

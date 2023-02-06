from django.test import SimpleTestCase, Client, TestCase
from django.urls import reverse, resolve

from .views import StatusesView, CreateStatus, UpdateStatus, DeleteStatus


class TestStatusesUrls(SimpleTestCase):

    def test_user_view(self):
        url = reverse('statuses')
        self.assertEquals(resolve(url).func.view_class, StatusesView)

    def test_status_create(self):
        url = reverse('create_status')
        self.assertEquals(resolve(url).func.view_class, CreateStatus)

    def test_user_update(self):
        url = reverse('update_status', args='1')
        self.assertEquals(resolve(url).func.view_class, UpdateStatus)

    def test_user_delete(self):
        url = reverse('delete_status', args='1')
        self.assertEquals(resolve(url).func.view_class, DeleteStatus)

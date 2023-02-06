from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from django.core.exceptions import ObjectDoesNotExist

from .views import StatusesView, CreateStatus, UpdateStatus, DeleteStatus
from .models import Status
from ..users.models import User


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


class StatusesViewsTest(TestCase):
    fixtures = ['statuses.json', 'users.json']

    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.client.force_login(self.user)
        self.statuses_url = reverse('statuses')
        self.create_url = reverse('create_status')
        self.update_url = reverse('update_status', args=[1])
        self.delete_url = reverse('delete_status', args=[1])
        self.form1 = {"name": "status"}

    def test_statuses_view_GET(self):
        self.status1 = Status.objects.get(pk=1)
        self.status2 = Status.objects.get(pk=2)
        response = self.client.get(self.statuses_url)
        response_tasks = list(response.context['statuses'])
        self.assertEquals(response.status_code, 200)
        self.assertQuerysetEqual(response_tasks, [self.status1, self.status2])
        self.assertTemplateUsed(response, 'statuses/statuses.html')

    def test_create_status_GET(self):
        response = self.client.get(self.create_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'crud/create_and_update.html')

    def test_create_status_POST(self):
        response = self.client.post(self.create_url, self.form1)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, self.statuses_url)
        self.assertTrue(Status.objects.get(pk=3))

    def test_update_status_GET(self):
        response = self.client.get(self.update_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'crud/create_and_update.html')

    def test_update_status_POST(self):
        response = self.client.post(self.update_url, self.form1)
        self.status = Status.objects.get(pk=1)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.status.name, self.form1['name'])
        self.assertRedirects(response, self.statuses_url)

    def test_delete_status_GET(self):
        response = self.client.get(self.delete_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'crud/delete.html')

    def test_delete_not_used_status_POST(self):
        response = self.client.post(self.delete_url)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, self.statuses_url)

    def test_delete_used_status_POST(self):
        self.status1 = Status.objects.get(pk=1)
        response = self.client.post(self.delete_url)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, self.statuses_url)
        with self.assertRaises(ObjectDoesNotExist):
            Status.objects.get(pk=1)

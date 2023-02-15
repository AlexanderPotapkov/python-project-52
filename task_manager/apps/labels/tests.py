from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from django.core.exceptions import ObjectDoesNotExist

from .views import LabelsView, CreateLabel, UpdateLabel, DeleteLabel
from ..users.models import User
from ..labels.models import Label


class TestLabelsUrls(SimpleTestCase):

    def test_labels_view(self):
        url = reverse('labels')
        self.assertEquals(resolve(url).func.view_class, LabelsView)

    def test_label_create(self):
        url = reverse('create_label')
        self.assertEquals(resolve(url).func.view_class, CreateLabel)

    def test_label_update(self):
        url = reverse('update_label', args='1')
        self.assertEquals(resolve(url).func.view_class, UpdateLabel)

    def test_label_delete(self):
        url = reverse('delete_label', args='1')
        self.assertEquals(resolve(url).func.view_class, DeleteLabel)


class TestLabelsViewsWithoutAuth(TestCase):

    def setUp(self):
        self.login = reverse('login')
        self.urls = [
            reverse('labels'),
            reverse('create_label'),
            reverse('delete_label', args='1'),
            reverse('update_label', args='1')
        ]

    def test_no_auth(self):
        for url in self.urls:
            response = self.client.get(url)
            self.assertRedirects(response, self.login)


class TestLabelsViews(TestCase):
    fixtures = ['users.json', 'tasks.json', 'statuses.json', 'labels.json']

    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.label1 = Label.objects.get(pk=1)
        self.label2 = Label.objects.get(pk=2)
        self.client.force_login(self.user)
        self.labels_url = reverse('labels')
        self.create_url = reverse('create_label')
        self.update_url = reverse('update_label', args=[1])
        self.delete_url = reverse('delete_label', args=[1])
        self.form1 = {'name': 'New label'}

    def test_labels_view_GET(self):
        response = self.client.get(self.labels_url)
        response_labels = list(response.context['labels'])
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response_labels, [self.label1, self.label2])
        self.assertTemplateUsed(response, 'labels/labels.html')

    def test_create_label_GET(self):
        response = self.client.get(self.create_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'crud/create_and_update.html')

    def test_create_label_POST(self):
        response = self.client.post(self.create_url, self.form1)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, self.labels_url)
        self.assertTrue(Label.objects.get(pk=3))

    def test_update_label_GET(self):
        response = self.client.get(self.update_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'crud/create_and_update.html')

    def test_update_label_POST(self):
        response = self.client.post(self.update_url, self.form1)
        self.label = Label.objects.get(pk=1)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.label.name, self.form1['name'])
        self.assertRedirects(response, self.labels_url)

    def test_delete_not_used_label_GET(self):
        response = self.client.get(self.delete_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'crud/delete.html')

    def test_delete_not_used_label_POST(self):
        response = self.client.post(self.delete_url)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, self.labels_url)
        with self.assertRaises(ObjectDoesNotExist):
            Label.objects.get(pk=3)

    def delete_used_label_GET(self):
        response = self.client.get(self.delete_url)
        self.assertRedirects(response, self.labels_url)

    def delete_used_label_POST(self):
        response = self.client.post(self.delete_url)
        self.assertRedirects(response, self.labels_url)
        self.assertEqual(len(Label.objects.all()), 2)

from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve

from .views import LabelsView, CreateLabel, UpdateLabel, DeleteLabel


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

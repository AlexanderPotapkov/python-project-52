from django.test import SimpleTestCase, Client, TestCase
from django.urls import reverse, resolve

from .views import UsersView, RegisterUser, UpdateUser, DeleteUser
from .models import User
from .forms import RegisterUserForm


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


class UsersViewsTest(TestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.client = Client()
        self.users_url = reverse('users')
        self.register_user_url = reverse('register')
        self.update_user_url = reverse('update', args=[1])
        self.delete_user_url = reverse('delete', args=[1])
        self.login_url = reverse('login')
        self.user1 = User.objects.get(pk=1)
        self.user2 = User.objects.get(pk=2)
        self.form1 = {
            'username': 'NewUser',
            'last_name': 'last',
            'first_name': 'first',
            'password1': 'password12345678',
            'password2': 'password12345678'
        }

    def test_users_view_GET(self):
        response = self.client.get(self.users_url)
        self.assertEquals(response.status_code, 200)
        response_tasks = list(response.context['users'])
        self.assertQuerysetEqual(response_tasks, [self.user1, self.user2])
        self.assertTemplateUsed(response, 'users/users.html')

    def test_register_user_view_GET(self):
        response = self.client.get(self.register_user_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'crud/create_and_update.html')

    def test_register_user_view_POST(self):
        response = self.client.post(self.register_user_url, self.form1)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, self.login_url)
        self.assertTrue(User.objects.get(pk=3))

    def test_update_user_view_GET(self):
        self.client.force_login(self.user1)
        response = self.client.get(self.update_user_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'crud/create_and_update.html')

    def test_update_user_view_POST(self):
        self.client.force_login(self.user1)
        response = self.client.post(self.update_user_url, self.form1)
        updated_user = User.objects.get(pk=1)
        self.assertRedirects(response, self.users_url)
        self.assertEqual(updated_user.username, self.form1['username'])

    def test_update_user_without_permission_GET(self):
        self.client.force_login(self.user2)
        response = self.client.get(self.update_user_url)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, self.users_url)

    def test_update_user_without_permission_POST(self):
        self.client.force_login(self.user2)
        user1 = User.objects.get(pk=1)
        response = self.client.post(self.update_user_url, self.form1)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, self.users_url)
        self.assertFalse(user1.username == self.form1['username'])

    def test_delete_user_GET(self):
        self.client.force_login(self.user1)
        response = self.client.get(self.delete_user_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'crud/delete.html')

    def test_delete_user_POST(self):
        self.client.force_login(self.user1)
        response = self.client.post(self.delete_user_url)
        self.assertRedirects(response, self.users_url)

    def test_delete_user_without_permissions_GET(self):
        self.client.force_login(self.user2)
        response = self.client.get(self.delete_user_url)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, self.users_url)

    def test_delete_user_without_permissions_POST(self):
        self.client.force_login(self.user2)
        user1 = User.objects.get(pk=1)
        response = self.client.post(self.update_user_url)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, self.users_url)
        self.assertFalse(user1.username == self.form1['username'])


class TestUserForms(SimpleTestCase):
    databases = '__all__'

    def test_register_form_with_valid_data(self):
        form = RegisterUserForm(data={
            'username': 'NewUser',
            'password1': 'password12345678',
            'password2': 'password12345678'
        })
        self.assertTrue(form.is_valid())

    def test_form_no_data(self):
        form = RegisterUserForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

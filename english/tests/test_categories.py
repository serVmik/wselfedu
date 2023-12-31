"""
Test CRUD categories.

For now:
    - can reade categories: admin, auth user;
    - can create, update and delete categories: admin.

Fixtures are created and taken from the db-wse-fixtures.sqlite3, contain:
    - users: admin, user1;
    - categories: category1, category2.
"""

from django.test import TestCase
from django.urls import reverse_lazy

from contrib_app.contrib_test import flash_message_test
from english.models import CategoryModel
from users.models import UserModel


class TestListCategories(TestCase):
    """Test list categories."""

    fixtures = [
        'english/tests/fixtures/categories.json',
        'english/tests/fixtures/users.json',
    ]

    def setUp(self):
        """Preparing the testing environment."""
        self.admin = UserModel.objects.get(username='admin')
        self.user = UserModel.objects.get(username='user1')
        self.category_name1 = CategoryModel.objects.get(pk=1).name
        self.category_name2 = CategoryModel.objects.get(pk=2).name
        self.list_url = reverse_lazy('eng:categories_list')

        self.no_permissions_message = 'Вы пока не можете делать это'
        self.no_permissions_redirect = reverse_lazy('home')

    #################################
    # Test list with permissions. #
    #################################
    def test_get_list_by_admin(self):
        """Get method by admin."""
        self.client.force_login(self.admin)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)

        # Does the categories list page contain a categories?
        response = self.client.get(self.list_url)
        html = response.content.decode()
        self.assertInHTML(self.category_name1, html)
        self.assertInHTML(self.category_name2, html)

    def test_get_list_by_user(self):
        """Get method by auth user."""
        self.client.force_login(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)

    ####################################
    # Test list with no permissions. #
    ####################################
    def test_get_list_by_not_auth(self):
        """Get method by not auth user."""
        response = self.client.get(self.list_url)
        self.assertRedirects(response, self.no_permissions_redirect, 302)
        flash_message_test(response, self.no_permissions_message)


class TestCreateCategory(TestCase):
    """Test create category."""

    fixtures = [
        'english/tests/fixtures/categories.json',
        'english/tests/fixtures/users.json',
    ]

    def setUp(self):
        """Preparing the testing environment."""
        self.admin = UserModel.objects.get(username='admin')
        self.user = UserModel.objects.get(username='user1')
        self.new_category = {'name': 'new_category'}

        self.create_url = reverse_lazy('eng:categories_create')
        self.success_url = reverse_lazy('eng:categories_list')
        self.success_message = 'Категория добавлена'
        self.no_permissions_message = 'Вы пока не можете делать это'
        self.no_permissions_redirect = reverse_lazy('home')

    #################################
    # Test create with permissions. #
    #################################
    def test_get_create_by_admin(self):
        """Get method by admin."""
        self.client.force_login(self.admin)
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, 200)

    def test_post_create_by_admin(self):
        """Post method by admin."""
        self.client.force_login(self.admin)
        response = self.client.post(self.create_url, self.new_category)
        self.assertRedirects(response, self.success_url, 302)
        flash_message_test(response, self.success_message)

        # Does the category list page contain a new category?
        response = self.client.get(self.success_url)
        self.assertInHTML(self.new_category['name'], response.content.decode())

    ####################################
    # Test create with no permissions. #
    ####################################
    def test_get_create_by_user(self):
        """Get method by auth user."""
        self.client.force_login(self.user)
        response = self.client.get(self.create_url)
        self.assertRedirects(response, self.no_permissions_redirect, 302)
        flash_message_test(response, self.no_permissions_message)

    def test_post_create_by_user(self):
        """Post method by auth user."""
        self.client.force_login(self.user)
        response = self.client.post(self.create_url, self.new_category)
        self.assertRedirects(response, self.no_permissions_redirect, 302)
        flash_message_test(response, self.no_permissions_message)

    def test_get_create_not_auth(self):
        """Get method by not auth user."""
        response = self.client.get(self.create_url)
        self.assertRedirects(response, self.no_permissions_redirect, 302)
        flash_message_test(response, self.no_permissions_message)

    def test_post_create_not_auth(self):
        """Post method by not auth user."""
        response = self.client.post(self.create_url, self.new_category)
        self.assertRedirects(response, self.no_permissions_redirect, 302)
        flash_message_test(response, self.no_permissions_message)


class TestUpdateCategory(TestCase):
    """Test update category."""

    fixtures = [
        'english/tests/fixtures/categories.json',
        'english/tests/fixtures/users.json',
    ]

    def setUp(self):
        """Preparing the testing environment."""
        self.admin = UserModel.objects.get(username='admin')
        self.user = UserModel.objects.get(username='user1')
        self.category = CategoryModel.objects.get(pk=1)
        self.updated_category = {'name': 'updated_category'}

        self.update_url = reverse_lazy(
            'eng:categories_update', kwargs={'pk': 1}
        )
        self.success_url = reverse_lazy('eng:categories_list')
        self.success_message = 'Категория изменена'
        self.no_permissions_message = 'Вы пока не можете делать это'
        self.no_permissions_redirect = reverse_lazy('home')

    #################################
    # Test update with permissions. #
    #################################
    def test_get_update_by_admin(self):
        """Get method by admin."""
        self.client.force_login(self.admin)
        response = self.client.get(self.update_url)
        self.assertEqual(response.status_code, 200)

    def test_post_update_by_admin(self):
        """Post method by admin."""
        self.client.force_login(self.admin)
        response = self.client.post(self.update_url, self.updated_category)
        self.assertRedirects(response, self.success_url, 302)
        flash_message_test(response, self.success_message)

        # Does the category list page contain an updated category?
        response = self.client.get(self.success_url)
        html = response.content.decode()
        self.assertInHTML(self.updated_category['name'], html)

    ####################################
    # Test update with no permissions. #
    ####################################
    def test_get_update_by_user(self):
        """Get method by auth user."""
        self.client.force_login(self.user)
        response = self.client.get(self.update_url)
        self.assertRedirects(response, self.no_permissions_redirect, 302)
        flash_message_test(response, self.no_permissions_message)

    def test_post_update_by_user(self):
        """Post method by auth user."""
        self.client.force_login(self.user)
        response = self.client.post(self.update_url, self.updated_category)
        self.assertRedirects(response, self.no_permissions_redirect, 302)
        flash_message_test(response, self.no_permissions_message)

        # Does the category list page contain a not updated category?
        response = self.client.get(self.success_url)
        html = response.content.decode()
        self.assertInHTML(self.category.name, html)

    def test_get_update_not_auth(self):
        """Get method by not auth user."""
        response = self.client.get(self.update_url)
        self.assertRedirects(response, self.no_permissions_redirect, 302)
        flash_message_test(response, self.no_permissions_message)

    def test_post_update_not_auth(self):
        """Post method by not auth user."""
        response = self.client.post(self.update_url, self.updated_category)
        self.assertRedirects(response, self.no_permissions_redirect, 302)
        flash_message_test(response, self.no_permissions_message)

        # Does the db contain a category name?
        self.assertTrue(CategoryModel.objects.filter(
            name=self.category.name
        ).exists())


class TestDeleteCategory(TestCase):
    """Test delete category."""

    fixtures = [
        'english/tests/fixtures/categories.json',
        'english/tests/fixtures/users.json',
    ]

    def setUp(self):
        """Preparing the testing environment."""
        self.admin = UserModel.objects.get(username='admin')
        self.user = UserModel.objects.get(username='user1')
        self.deleted_category = CategoryModel.objects.get(pk=1)

        self.delete_url = reverse_lazy(
            'eng:categories_delete', kwargs={'pk': 1}
        )
        self.success_url = reverse_lazy('eng:categories_list')
        self.success_message = 'Категория удалена'
        self.no_permissions_message = 'Вы пока не можете делать это'
        self.no_permissions_redirect = reverse_lazy('home')

    #################################
    # Test delete with permissions. #
    #################################
    def test_get_delete_by_admin(self):
        """Get method by admin."""
        self.client.force_login(self.admin)
        response = self.client.get(self.delete_url)
        self.assertEqual(response.status_code, 200)

    def test_post_delete_by_admin(self):
        """Post method by admin."""
        self.client.force_login(self.admin)
        response = self.client.post(self.delete_url)
        self.assertRedirects(response, self.success_url, 302)
        flash_message_test(response, self.success_message)

        # Does the db contain a deleted category?
        self.assertFalse(CategoryModel.objects.filter(pk=1).exists())

    ####################################
    # Test delete with no permissions. #
    ####################################
    def test_get_delete_by_user(self):
        """Get method by auth user."""
        self.client.force_login(self.user)
        response = self.client.get(self.delete_url)
        self.assertRedirects(response, self.no_permissions_redirect, 302)
        flash_message_test(response, self.no_permissions_message)

    def test_post_delete_by_user(self):
        """Post method by auth user."""
        self.client.force_login(self.user)
        response = self.client.post(self.delete_url)
        self.assertRedirects(response, self.no_permissions_redirect, 302)
        flash_message_test(response, self.no_permissions_message)

        # Does the db contain a category?
        self.assertTrue(CategoryModel.objects.filter(pk=1).exists())

    def test_get_delete_not_auth(self):
        """Get method by not auth user."""
        response = self.client.get(self.delete_url)
        self.assertRedirects(response, self.no_permissions_redirect, 302)
        flash_message_test(response, self.no_permissions_message)

    def test_post_delete_not_auth(self):
        """Post method by not auth user."""
        response = self.client.post(self.delete_url)
        self.assertRedirects(response, self.no_permissions_redirect, 302)
        flash_message_test(response, self.no_permissions_message)

        # Does the db contain a category?
        self.assertTrue(CategoryModel.objects.filter(pk=1).exists())

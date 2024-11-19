from django.test import TestCase
from django.urls import reverse


class URLTestCase(TestCase):
    def test_main_page_status_code(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)
        
    def test_admin_page_status_code(self):
        response = self.client.get("/admin/")
        self.assertEqual(response.status_code, 302)
        
    # def test_profile_page_status_code(self):
    #     response = self.client.get("/user/profile/")
    #     self.assertEqual(response.status_code, 200)
            
    # def test_cart_page_status_code(self):
    #     response = self.client.get("/user/cart/")
    #     self.assertEqual(response.status_code, 200)
        

class TemplateTestCase(TestCase):
    def test_main_view_template(self):
        response = self.client.get("")
        self.assertTemplateUsed(response, 'main/index.html')
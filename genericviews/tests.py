from django.test import TestCase
from .models import Product


class ProductTest(TestCase):
    def create_product(self, name = "manish", rollNo="173050058", mobile="8574353782"):
        return Product.objects.create(name=name,
                                      rollNo=rollNo,
                                      mobile=mobile)

    def test_product_creation(self):
        a = self.create_product()
        self.assertTrue(isinstance(a,Product))
        self.assertEqual(a.__str__(), a.rollNo + "_" + str(a.id))

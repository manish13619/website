from django.test import TestCase
from .models import Product


class ProductTest(TestCase):
    def create_product(self, name = "manish", rollNo="173050058", mobile="8574353782"):
        return Product.objects.create(name=name,
                                      rollNo=rollNo,
                                      mobile=mobile)

    def create_rollno(self,rollNo="173040049"):
        return Product.objects.create(rollNo=rollNo)

    def test_product_creation(self):
        a = self.create_product(name="ravi",rollNo="173050052", mobile="7834568978")
        self.assertTrue(isinstance(a,Product))
        self.assertEqual(a.__str__(), a.rollNo + "_" + str(a.id))

        b = self.create_product()
        self.assertTrue(isinstance(a, Product))
        self.assertEqual(b.__str__(), b.rollNo + "_" + str(b.id))

    def test_getrollno(self):
        a = self.create_rollno()
        self.assertEqual(a.__getrollno__(), a.rollNo)


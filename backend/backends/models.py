from __future__ import unicode_literals
from django.db import models
from django.forms.models import model_to_dict


class Element(models.Model):
	name = models.CharField(max_length=100)
	quantity = models.IntegerField(blank=True,null = True)
	frontimage = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank = True, null = True)
	backimage = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank = True, null = True)
	content_image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank = True, null = True)

	def __str__(self):
		return str(self.quantity) +" " + self.name + "(s)"

	def to_dict(self):
		d = model_to_dict(self)
                d['frontimage'] = self.frontimage.url if self.frontimage else ''
		d['backimage'] = self.backimage.url if self.backimage else ''
		d['content_image'] = self.content_image.url if self.content_image else ''
		return d

class Bundle(models.Model):
	name = models.CharField(max_length=100)
	quantity = models.IntegerField()
	def __str__(self):
		return self.name


class Order(models.Model):
	status = models.BooleanField()
	date_completed = models.DateField(blank=True,null = True)
	date_added = models.DateField()
	def __str__(self):
		return "order No. " +  str(self.id) + " from "+ str(self.date_added)


class BundleElement(models.Model):
        bundle = models.ForeignKey(Bundle,models.CASCADE, related_name='elements')
        element = models.ForeignKey(Element,models.CASCADE, related_name='bundles')
        quantity = models.IntegerField()
        def __str__(self):
#                return "Order No. " + str(self.order.id) + " from " + str(self.order.date_added) + " with bundle " + str(self.bundle) + ". |  Quanti$
		return str(self.bundle) + " " + str(self.element)


class OrderBundles(models.Model):
	bundle = models.ForeignKey(Bundle,models.CASCADE, related_name='orders')
	order = models.ForeignKey(Order,models.CASCADE, related_name='bundles')
	quantity = models.IntegerField()
	def __str__(self):
		return "Order No. " + str(self.order.id) + " from " + str(self.order.date_added) + " with bundle " + str(self.bundle) + ". |  Quantity: " + str(self.quantity)

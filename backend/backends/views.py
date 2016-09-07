from django.shortcuts import render
from django.http import JsonResponse
from backends.models import *
from django.db.models import Prefetch
from django.forms.models import model_to_dict


def return_orders(request):
    query = Order.objects.filter(status = False).prefetch_related('bundles')
    orders = []
    for q in query:
        order_d = model_to_dict(q)
	bundles = []
	for bundle_order in q.bundles.all():
		bundle = bundle_order.bundle
		bundle_d = model_to_dict(bundle)
		bundle_d['elements'] = [be.element.to_dict() for be in bundle.elements.all()]
		bundles.append(bundle_d)
        order_d['bundles'] = bundles
        orders.append(order_d)

    response=JsonResponse({'orders': orders})
    return response

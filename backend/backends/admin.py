from django.contrib import admin
from backends.models import Element
from backends.models import Order
from backends.models import OrderBundles
from backends.models import Bundle
from backends.models import BundleElement


class OrderBundlesInline(admin.TabularInline):
	model = OrderBundles
	#exclude = ("id", )
	#show_change_link = True


class BundleElementInline(admin.TabularInline):
        model = BundleElement


class OrderAdmin(admin.ModelAdmin):
	model = Order
	inlines = [OrderBundlesInline, ]


class BundleAdmin(admin.ModelAdmin):
	model = Bundle
	inlines = [BundleElementInline, ]


admin.site.register(Element)
admin.site.register(Order, OrderAdmin)
#admin.site.register(BundleElement)
admin.site.register(Bundle, BundleAdmin)

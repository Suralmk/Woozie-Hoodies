from django.contrib import admin
import csv
import datetime
from django.http import HttpResponse
# Register your models here.
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
def export_to_csv(modeladmin, request, query):
    opts = modeladmin.model._meta
    content_desposition = f'attachment; filename={opts.verbose_name}.csv '
    response = HttpResponse(content_type='text/csv')
    response["Content-Disposition"] = content_desposition
    csv_writer = csv.writer(response)
    fields = [csv_field for csv_field in opts.get_fields() if not csv_field.many_to_many and not csv_field.one_to_many]
    csv_writer.writerow([field.verbose_name for field in fields])

    for obj in query:
        data_row = []
        for field in fields:
            value = getattr(obj ,field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime("%d/%m/%Y")
            data_row.append(value)
        csv_writer.writerow(data_row)
    return response

export_to_csv.short_description = "Export to Csv"

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'phone_no', 'city', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
    actions = [export_to_csv]

admin.site.register(Order, OrderAdmin)
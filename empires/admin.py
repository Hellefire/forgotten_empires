from django.contrib import admin
from django.contrib.admin.apps import AdminConfig



class MyAdminSite(admin.AdminSite):
    def each_context(self, request):
        context = super().each_context(request)
        context['site_url'] = '/empires/'
        return context


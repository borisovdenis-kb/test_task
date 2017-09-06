from django.contrib import admin
from test_task_app.models import (
    CreditOrganizations, Offers, WorkSheets, Claims
)


class CreditOrganizationsAdmin(admin.ModelAdmin):
    list_display = (
        "org_name",
    )


class OffersAdmin(admin.ModelAdmin):
    list_display = (
        "created_date",
        "changed_date",
        "rotation_start_date",
        "rotation_end_date",
        "title",
        "offer_type",
        "scoring_min",
        "scoring_max",
        "credit_org",
    )


class WorkSheetsAdmin(admin.ModelAdmin):
    list_display = (
        "created_date",
        "changed_date",
        "first_name",
        "last_name",
        "middle_name",
        "birth_day",
        "phone",
        "passport_number",
        "scoring",
    )


class ClaimsAdmin(admin.ModelAdmin):
    list_display = (
        "created_date",
        "sent_date",
        "worksheet",
        "offer",
        "status",
    )


admin.site.register(CreditOrganizations, CreditOrganizationsAdmin)
admin.site.register(Offers, OffersAdmin)
admin.site.register(WorkSheets, WorkSheetsAdmin)
admin.site.register(Claims, ClaimsAdmin)

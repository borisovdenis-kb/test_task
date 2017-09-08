from django.db import models

# Create your models here.
# TODO: Добавить валидацию для полей!!!


class UpdateMixin:
    """
        An mixin that allows you to add a method for any model. 
        By inheritance.

        class ModelName(models.Model, UpdateMixin):
            ...
        obj = ModelName.objects.get(...)
        obj.update(**{field1: value1, ...})
    """
    def update(self, **kwargs):
        if self._state.adding:
            raise self.DoesNotExist

        for field, value in kwargs.items():
            setattr(self, field, value)

        self.clean_fields()
        self.save()


class CreditOrganizations(models.Model, UpdateMixin):
    """
        Таблица создана для того, чтобы было на что ссылаться
        в поле credit_org таблицы Offers.
    """
    org_name = models.CharField(max_length=256, blank=False)


class Offers(models.Model, UpdateMixin):
    """
        Таблица предложений.
    """
    created_date = models.DateTimeField(auto_now_add=True)
    changed_date = models.DateTimeField(auto_now=True)
    rotation_start_date = models.DateTimeField()
    rotation_end_date = models.DateTimeField()
    title = models.CharField(max_length=256, blank=False)
    offer_type = models.CharField(max_length=30, blank=False)
    scoring_min = models.IntegerField(blank=False)
    scoring_max = models.IntegerField(blank=False)
    credit_org = models.ForeignKey(CreditOrganizations)

    class Meta:
        permissions = (
            ("view_offers", "Can see one or several offers."),
        )


class WorkSheets(models.Model, UpdateMixin):
    """
        Таблица анкет клиентов.
    """
    created_date = models.DateTimeField(auto_now_add=True)
    changed_date = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=50, blank=False)  # поле "отчество" оставлено со свойством blank=true
    last_name = models.CharField(max_length=50, blank=False)   # потому, что клиент может быть иностранного
    middle_name = models.CharField(max_length=50, blank=True)  # происхождения или не иметь отчества по другим причинам.
    birth_day = models.DateField()
    phone = models.CharField(max_length=12)
    passport_number = models.CharField(max_length=10)
    scoring = models.IntegerField(blank=False)

    class Meta:
        permissions = (
            ("view_worksheets", "Can see one or several worksheets."),
        )


class Claims(models.Model, UpdateMixin):
    """
        Таблица заявок в кредитную организацию.
    """
    created_date = models.DateTimeField(auto_now_add=True)
    sent_date = models.DateTimeField(blank=True)
    worksheet = models.ForeignKey(WorkSheets)
    offer = models.ForeignKey(Offers)
    status = models.CharField(max_length=10)

    class Meta:
        permissions = (
            ("view_claims", "Can see one or several claims."),
            ("send_claims", "Can send claim."),
        )

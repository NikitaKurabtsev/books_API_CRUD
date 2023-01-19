from rest_framework.validators import UniqueValidator


def email_unique_validation(model):
    return UniqueValidator(queryset=model.objects.all())

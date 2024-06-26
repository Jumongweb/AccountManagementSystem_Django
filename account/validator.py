from django.core.exceptions import ValidationError


def validate_pin(pin):
    if len(pin) < 4:
        return ValidationError("Pin must be at least 4")

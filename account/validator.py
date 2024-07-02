from django.core.exceptions import ValidationError


def validate_pin(pin: str):
    if len(pin) < 4:
        return ValidationError("Pin must be at least 4")


def validate_phone_number(phone_number: str):
    if len(phone_number) < 11:
        return ValidationError("Phone must be at least 11")

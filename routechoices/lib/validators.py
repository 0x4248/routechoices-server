import re
from decimal import Decimal

from django.conf import settings
from django.core.validators import RegexValidator, ValidationError
from django.utils.translation import gettext_lazy as _

import routechoices.lib.luhn as luhn

FLOAT_RE = re.compile(r"^(\-?[0-9]+(\.[0-9]+)?)$")


domain_validator = RegexValidator(
    r"^([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}$", "Please enter a valid domain"
)


def validate_imei(number):
    """Check if the number provided is a valid IMEI number."""
    try:
        matched = re.match(r"^\d{15}$", number)
    except Exception:
        raise ValidationError("Invalid IMEI")
    if not matched:
        raise ValidationError(_("Invalid IMEI (must be 15 characters)"))
    if not luhn.validate(number):
        raise ValidationError(_("Invalid IMEI (check digit does not match)"))


def validate_esn(number):
    """Check if the number provided is a valid ESN number."""
    try:
        matched = re.match(r"^\d-\d{7}$", number)
    except Exception:
        raise ValidationError("Invalid ESN")
    if not matched:
        raise ValidationError(_("Invalid ESN"))


def validate_latitude(value):
    if isinstance(value, (float, int)):
        value = str(value)
    try:
        value = Decimal(value)
    except Exception:
        raise ValidationError(_("not a number"))
    if value < -90 or value > 90:
        raise ValidationError(_("latitude out of range -90.0 90.0"))


def validate_longitude(value):
    if isinstance(value, (float, int)):
        value = str(value)
    try:
        value = Decimal(value)
    except Exception:
        raise ValidationError(_("not a number"))
    if value < -180 or value > 180:
        raise ValidationError(_("longitude out of range -180.0 180.0"))


def validate_nice_slug(slug):
    errors = []
    if re.search(r"[^-a-zA-Z0-9_]", slug):
        errors.append(
            _("Only alphanumeric characters, hyphens and underscores are allowed.")
        )
    if len(slug) < 2:
        errors.append(_("Too short. (min. 2 characters)"))
    elif len(slug) > 32:
        errors.append(_("Too long. (max. 32 characters)"))
    if slug[0] in "_-":
        errors.append(_("Must start with an alphanumeric character."))
    if slug[-1] in "_-":
        errors.append(_("Must end with an alphanumeric character."))
    if "--" in slug or "__" in slug or "-_" in slug or "_-" in slug:
        errors.append(_("Cannot include 2 non alphanumeric characters in a row."))
    if slug.lower() in settings.SLUG_BLACKLIST:
        raise errors.append(_("Forbidden word."))
    if errors:
        raise ValidationError(errors)


def validate_domain_slug(slug):
    errors = []
    if re.search(r"[^-a-zA-Z0-9]", slug):
        errors.append(_("Only alphanumeric characters and hyphens are allowed."))
    if len(slug) < 2:
        errors.append(_("Too short. (min. 2 characters)"))
    elif len(slug) > 32:
        errors.append(_("Too long. (max. 32 characters)"))
    if slug[0] in "-":
        errors.append(_("Must start with an alphanumeric character."))
    if slug[-1] in "-":
        errors.append(_("Must end with an alphanumeric character."))
    if "--" in slug:
        errors.append(_("Cannot include 2 non alphanumeric characters in a row."))
    if slug.lower() in settings.SLUG_BLACKLIST:
        raise errors.append(_("Forbidden word."))
    if errors:
        raise ValidationError(errors)


def validate_image_data_uri(value):
    if not value:
        raise ValidationError(_("Data URI Can not be null"))
    data_matched = re.match(
        r"^data:image/(?P<format>jpeg|png|gif);base64,"
        r"(?P<data_b64>(?:[A-Za-z0-9+/]{4})*"
        r"(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?)$",
        value,
    )
    if not data_matched:
        raise ValidationError(_("Not a base 64 encoded data URI of an image"))


def validate_corners_coordinates(val):
    cal_values = val.split(",")
    if len(cal_values) != 8:
        raise ValidationError(
            _("Corners coordinates must have 8 float values " "separated by commas.")
        )
    for i, val in enumerate(cal_values):
        if not FLOAT_RE.match(val):
            raise ValidationError(
                _("Corners coordinates must only contain float values.")
            )
        if i % 2 == 0:
            validate_latitude(val)
        # do not validate longitude for map over the international date line


custom_username_validators = [
    validate_nice_slug,
]

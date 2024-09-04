from __future__ import unicode_literals

from .helpers import get_django_version

from django.apps import AppConfig
# NOTE: Fixed for fork
if get_django_version() <= 2:
    from django.utils.translation import ugettext_lazy as _
else:
    from django.utils.translation import gettext_lazy as _


class AdsConfig(AppConfig):
    name = 'ads'
    verbose_name = _('Ads Management System')

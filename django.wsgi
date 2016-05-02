
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import sys


# По умолчанию используется версия Django 1.4,
# если вы хотите использовать другие версии, поменяйте эту переменную.
# Возможные значения:  '1.7', '1.6','1.5','1.4'
# Если оставить строку пустой, будет использоваться версия, установленная на сервере.

django_version = '1.9'
activate_this = '/home/hosting_watercolor/env/water2/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
# Добавьте нужные вам пути поиска.
# Если вы получаете ошибку 500 Internal Server Error,
# скорее всего проблема именно в путях поиска.

sys.path.insert(0, '/home/hosting_watercolor/env/water2/lib/python2.7/site-packages')
sys.path.insert(0, '/home/hosting_watercolor/projects/watercolor')

os.environ['DJANGO_SETTINGS_MODULE'] = 'watercolor.settings'

# ------ Ниже этой линии изменения скорее всего не нужны --------
if not hasattr(sys, 'real_prefix'):
    python_lib = "python%d.%d" % (sys.version_info[0], sys.version_info[1])
    if django_version:
        sys.path.insert(0, "/opt/django-%s/lib/%s/site-packages/" % (django_version, python_lib))

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
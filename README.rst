=============================
django-database-email-backend
=============================


Installation::

    pip install django-database-email-backend

Add ``database_email_backend`` to ``INSTALLED_APPS`` and run ``manage.py syncdb`` or
``manage.py migrate django_database_email_backend`` if you are using South.

Add the email backend setting::

    EMAIL_BACKEND = 'database_email_backend.backend.DatabaseEmailBackend'


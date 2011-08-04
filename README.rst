=============================
django-database-email-backend
=============================

django-database-email-backend is a simple email backend for django that delivers emails to the database. All sent
emails can be reviewed and searched in admin. This can be practical while developing where the console backend can't be
used (e.g on a development or staging server).

.. note:: Currently only the plaintext part of the email is saved and displayed. Future versions of
          django-database-email-backend will also display html and attachments.

Installation::

    pip install django-database-email-backend

Add ``database_email_backend`` to ``INSTALLED_APPS`` and run ``manage.py syncdb`` or
``manage.py migrate django_database_email_backend`` if you are using South.

Add the email backend setting::

    EMAIL_BACKEND = 'database_email_backend.backend.DatabaseEmailBackend'


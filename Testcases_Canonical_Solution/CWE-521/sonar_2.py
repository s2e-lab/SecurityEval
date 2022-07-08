'''
Define DATABASE vairable in the settings for a django application
'''


DATABASES = {
    'postgresql_db': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'quickdb',
        'USER': 'sonarsource',
        'PASSWORD': '', 
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users'

    # il faut que je rajoute cette fonction pour que les signaux soient pris en compte
    def ready(self):
        import apps.users.signals

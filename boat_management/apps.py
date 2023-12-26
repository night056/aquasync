from django.apps import AppConfig


class BoatManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'boat_management'

    def ready(self):
        import boat_management.signals
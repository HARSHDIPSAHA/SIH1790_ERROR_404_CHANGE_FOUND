from django.apps import AppConfig


class SurveillanceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'surveillance'

    def ready(self):
        import surveillance.signals  # Ensure signals are imported
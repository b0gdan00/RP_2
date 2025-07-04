from django.apps import AppConfig

class ControlConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'control'

    def ready(self):
        import sys
        if 'runserver' in sys.argv:
            from threading import Thread
            from .data_collectors import collect_data
            print('Starting data collection thread...')
            t = Thread(target=collect_data, daemon=True).start()
            # t.join()  # Wait for the thread to finish (optional, can be removed if you want it to run indefinitely)
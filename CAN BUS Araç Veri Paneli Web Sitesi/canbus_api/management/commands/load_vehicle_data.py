import json
from django.core.management.base import BaseCommand
from canbus_api.models import Vehicle
from django.utils.dateparse import parse_datetime

class Command(BaseCommand):
    help = 'Loads vehicle data from canbus_data.json into the database'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Loading vehicle data...'))

        try:
            with open('canbus_data.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('canbus_data.json not found in the root directory.'))
            return

        for item in data:
            # Plaka formatını boşluksuz hale getiriyoruz, URL'de daha kolay kullanmak için.
            # Örn: "34 ABC 123" -> "34ABC123"
            formatted_vehicle_id = item['vehicle_id'].replace(" ", "")

            Vehicle.objects.update_or_create(
                vehicle_id=formatted_vehicle_id,
                defaults={
                    'timestamp': parse_datetime(item['timestamp']),
                    'status': item['status'],
                    'diagnostics': item['diagnostics'],
                    'location': item['location'],
                }
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully loaded or updated {len(data)} vehicle records.'))
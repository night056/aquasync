# generate_sample_data.py
import random
from boat_management.models import Boat
from user_authentication.models import Owner
from django.contrib.auth.models import User

# Function to generate sample data and add it to the Boat table
def generate_sample_data(num_samples=50):
    owners = Owner.objects.all()
    
    for _ in range(num_samples):
        owner = random.choice(owners) if owners.exists() else None
        Boat.objects.create(
            reg_no=f"REG-{random.randint(1000, 9999)}",
            name=f"Boat-{random.randint(1, 100)}",
            type=random.choice(["Fishing", "Yacht", "Speedboat", "Sailboat"]),
            year_of_make=random.randint(2000, 2023),
            capacity=random.randint(1, 100),
            services=f"Service-{random.randint(1, 5)}",
            lifejacket=random.choice([True, False]),
            fire_extinguisher=random.choice([True, False]),
            location=f"Location-{random.randint(1, 10)}",
            owner=owner,
            availability=random.choice([True, False]),
            active_status=True  # Assuming all generated boats are active
        )

if __name__ == '__main__':
    generate_sample_data()

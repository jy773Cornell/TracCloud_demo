from django.db import models
from utils.UUIDGen import gen_uuid


class MyModelManager(models.Manager):
    prefix = ""

    def prefix(self, prefix):
        self.prefix = prefix

    def create(self, **obj_data):
        # Create UUID with prefix as the primary key
        obj_data[self.prefix] = gen_uuid(self.prefix)

        # Call the super method which does the actual creation
        return super().create(**obj_data)

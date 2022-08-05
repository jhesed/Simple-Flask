from pynamodb.attributes import UnicodeAttribute
from pynamodb.models import Model


class User(Model):
    class Meta:
        table_name = "users"

    account_id = UnicodeAttribute(hash_key=True)
    email = UnicodeAttribute()

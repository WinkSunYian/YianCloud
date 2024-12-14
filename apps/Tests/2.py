from datetime import datetime, timedelta

expiry_date = (datetime.now() + timedelta(days=1)).replace(
    hour=0, minute=0, second=0, microsecond=0
)

print(expiry_date)

from datetime import datetime, timedelta


def days_ago(n: int):
    return datetime.now() - timedelta(days=n)

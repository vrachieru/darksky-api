from datetime import datetime

def date(timestamp):
    try:
        return datetime.utcfromtimestamp(int(timestamp))
    except:
        return None

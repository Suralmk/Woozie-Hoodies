import uuid
import datetime

def get_transaction_number(order_id):
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    random_number = uuid.uuid4().hex[:6]
    transaction_number = f'{timestamp}-{random_number}-{order_id}' if random_number else timestamp
    return transaction_number

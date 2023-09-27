from ippanel import Client


def send_review_order(machine_name, mobile):
    api_key = 'oV49VQNYQv37gwIQsYjAJp8URE3RgL-z06w2sUfTiEY='
    sms = Client(api_key)
    pattern_values = {
        "machine_name": machine_name,
    }

    try:
        bulk_id = sms.send_pattern(
            "n1z10op8x9bmulq",  # pattern code
            "3000505",  # originator
            mobile,  # recipient
            pattern_values,  # pattern values
        )
        message = sms.get_message(bulk_id)
        return message
    except:
        return False


def send_new_order_message(order, mobile):
    api_key = 'oV49VQNYQv37gwIQsYjAJp8URE3RgL-z06w2sUfTiEY='
    sms = Client(api_key)
    pattern_values = {
        "user": f'{order.user.first_name} {order.user.last_name}',
        "operation": order.operationName,
        "department": order.departmentName,
        "description": order.description,
    }

    try:
        bulk_id = sms.send_pattern(
            "xjai0p00umcoe5t",  # pattern code
            "3000505",  # originator
            mobile,  # recipient
            pattern_values,  # pattern values
        )
        message = sms.get_message(bulk_id)
        return message
    except:
        return False


def send_completed_message(order, mobile):
    api_key = 'oV49VQNYQv37gwIQsYjAJp8URE3RgL-z06w2sUfTiEY='
    sms = Client(api_key)
    pattern_values = {
        "order_id": order.orderId,
    }

    try:
        bulk_id = sms.send_pattern(
            "lrawoyx0rzonk14",  # pattern code
            "3000505",  # originator
            mobile,  # recipient
            pattern_values,  # pattern values
        )
        message = sms.get_message(bulk_id)
        return message
    except:
        return False

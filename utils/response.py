def success_response(message, data=None, status_code=200):
    return {
        "status": True,
        "message": message,
        "data": data,
        "code": status_code
    }

def error_response(message, errors=None, status_code=400):
    return {
        "status": False,
        "message": message,
        "errors": errors,
        "code": status_code
    }

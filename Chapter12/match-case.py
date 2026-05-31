# like switch case 

def http_status(status):
    match (status):
        case 200:
            return "ok"
        case 404:
            return "Not found"
        case 500:
            return "Internal Several Error"
        case _:
            return "Unknown status"
        

print(http_status(5))
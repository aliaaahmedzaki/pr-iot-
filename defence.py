def is_safe_command(data):

    if "command" in data:
        return "DROP" not in data["command"]

    return True


def apply_defence(data, attack_type, original_data):

    if attack_type == "Sniffing":
        return "ENCRYPTED_DATA"

    elif attack_type == "MITM":

        if data != original_data:

            return {
                "error":"Tampering detected"
            }

        return data

    elif attack_type == "Replay":

        if data["timestamp"] < original_data["timestamp"]:

            return {
                "error":"Replay blocked"
            }

        return data

    elif attack_type == "Injection":

        if not is_safe_command(data):

            return {
                "error":"Malicious command blocked"
            }

        return data

    elif attack_type == "Brute Force":

        return {
            "status":"Rate limiting applied"
        }

    return data
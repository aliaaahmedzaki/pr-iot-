def sniff_data(data):

    return data


def brute_force_attack():

    return {
        "status":"password guessed"
    }


def mitm_attack(data):

    new_data = data.copy()

    new_data["temperature"] += 15

    return new_data


def replay_attack(data):

    old = data.copy()

    old["timestamp"] -= 100

    return old


def injection_attack():

    return {
        "command":"DROP TABLE users;"
    }
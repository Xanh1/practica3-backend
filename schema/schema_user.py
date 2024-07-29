save_user = {
    "type": "object",
    "required": ["dni", "name", "last-name", "username", "password"],
    "properties": {
        "dni": {
            "type": "string",
            "minLength": 10,
            "maxLength": 10
        },
        "name": {
            "type": "string"
        },
        "last-name": {
            "type": "string"
        },
        "username": {
            "type": "string"
        },
        "password": {
            "type": "string"
        }
    }
}

update_user = {
    "type": "object",
    "required": ["dni", "name", "last-name", "person"],
    "properties": {
        "dni": {
            "type": "string",
            "minLength": 10,
            "maxLength": 10
        },
        "name": {
            "type": "string"
        },
        "last-name": {
            "type": "string"
        },
        "person": {
            "type": "string"
        }
    }
}

auth_user = {
    "type": "object",
    "required": ["username", "password"],
    "properties": {
        "username": {
            "type": "string"
        },
        "password": {
            "type": "string"
        }
    }
}
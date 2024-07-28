create_branch = {
    "type": "object",
    "required" : ["name", "latitude", "longitude"],
    "properties": {
        "name" : {
            "type" : "string"
        },
        "latitude" : {
            "type" : "number",
            "format" : "double"
        },
        "longitude" : {
            "type" : "number",
            "format" : "double"
        },
    }
}
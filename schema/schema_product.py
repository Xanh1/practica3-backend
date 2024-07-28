create_product = {
    "type": "object",
    "required" : ["name", "description"],
    "properties": {
        "name" : {
            "type" : "string"
        },
        "description" : {
            "type" : "string"
        }
    }
}

add_product = {
    "type": "object",
    "required" : ["product", "branch", "price", "stock", "exp_date"],
    "properties": {
        "product" : {
            "type" : "string"
        },
        "branch" : {
            "type" : "string"
        },
        "price" : {
            "type" : "number",
            "format" : "double"
        },
        "stock" : {
            "type" : "integer"
        },
        "exp_date" : {
            "type" : "string"
        }
    }
}
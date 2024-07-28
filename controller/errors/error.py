import enum

class Error(enum.Enum):
    
    # Token errors
    NON_EXIST_TOKEN = 'Token does not exist'
    INVALID_TOKEN = 'Token is invalid'
    
    # Account errors
    USER_EXIST = 'Username already exists'
    NON_EXISTS_ACCOUNT = 'Username or Password is wrong'
    
    # Person errors
    DNI_EXISTS = 'Dni already exists'
    EMAIL_EXISTS = 'Email already exists'
    NON_EXIST_PERSON = 'Person does not exist'

    # Product errors
    PRODUCT_EXISTS = 'Product already exists'
    NON_EXIST_PRODUCT = 'Product does not exist'

    # Branch errors
    NON_EXIST_BRANCH = 'Branch does not exist'
    BRANCH_EXIST = 'Branch already exists'


def json_response(msg, code, context):
    return {
        'msg'  : msg,
        'code' : code,
        'context' : context,
    }
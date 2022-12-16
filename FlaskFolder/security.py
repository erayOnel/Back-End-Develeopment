import hmac
from user import User
import codecs
codecs.register_error("strict", codecs.ignore_errors)

def authenticate(username,password):
    user=User.find_by_username(username)
    if user and hmac.compare_digest(user.password, password):
        return user
def identity(payload):
    id=payload["identity"]
    return User.find_by_id(id)

















































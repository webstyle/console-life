from .base_rpc import Base_Rpc


class token_validation(Base_Rpc):
    token: ""
    is_valid: False

    def __init__(self, token):
        super().__init__("token_validation")
        self.token = token

    def token_is_valid(self):
        try:
            self.is_valid = self.call(self.token)
        except ValueError:
            print("Please try again")
        finally:
            return self.is_valid

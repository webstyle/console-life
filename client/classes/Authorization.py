from .base_rpc import Base_Rpc


class Authorization(Base_Rpc):
    token: ""
    name: ""

    def __init__(self):
        super().__init__("connection")

    def sign(self):
        self.name = input("Enter your name:   ")
        self.token = self.call(self.name)

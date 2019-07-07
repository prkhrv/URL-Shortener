import random
import string


class shortener:
    tokenSize = 5

    def __init__(self,tokenSize=None):
        self.tokenSize = tokenSize if tokenSize is not None else 5

    def issue_token(self):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(self.tokenSize))    

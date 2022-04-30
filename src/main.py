from mathematics.arithmetric import Arithmetrics
from utils import utils
import fire

class CLI(object):
    """CLI application that demonstrated simple arithmetric operations"""

    def __init__(self):
        self._cli = Arithmetrics()

    def add(self, a: float, b:float):
        """Adds two numbers and returns a float"""

        if utils.is_number(a) and utils.is_number(b):
            return self._cli.sum(a,b)
        
        return "parameters must be number"
        

    def subtract(self, a: float, b:float):
        """Subtracts b from a and returns a float"""

        if utils.is_number(a) and utils.is_number(b):
            return self._cli.subtract(a,b)

        return "parameters must be number"

    def multiply(self, a: float, b:float):
        """Multiplys a with b and returns a float"""

        if utils.is_number(a) and utils.is_number(b):
            return self._cli.multiply(a,b)

        return "parameters must be number"

    def divide(self, a: float, b:float):
        """Divides b by a and returns a float"""
        try:
            if utils.is_number(a) and utils.is_number(b):
                return self._cli.divide(a,b)
            return "parameters must be number"
        except(ZeroDivisionError):
            return "Divisor can not be Zero", 0


if __name__ == '__main__':
    fire.Fire(CLI)

# define Python user-defined exceptions

__author__ = "Paruj Ratanaworabhan"
__credits__ = ["Paruj Ratanaworabhan"]
__version__ = "0.1.0"
__maintainer__ = "Paruj Ratanaworabhan"
__email__ = "paruj.r@ku.th"
__status__ = "Dev"

class Error(Exception):
   """Base class for other exceptions"""
   pass
class InvalidCardRank(Error):
   """Raised when the input card rank is not a valid rank"""
   pass
class InvalidCardSuit(Error):
   """Raised when the input card suit is not a valid suit"""
   pass

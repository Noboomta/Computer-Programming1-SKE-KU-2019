# define Python user-defined exceptions

class Error(Exception):
   """Base class for other exceptions"""
   pass

class AccountNotFound(Error):
   """Raised when the account is invalid"""
   pass

class InsufficientFund(Error):
   """Raised when the amount to be drawn is greater than the balance"""
   pass

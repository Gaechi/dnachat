# -*-coding:utf8-*-
from functools import wraps

from dnachat.dna.exceptions import ProtocolError


def must_be_in_channel(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.user is not None and self.user.channel is None:
            raise ProtocolError
        return func(self, *args, **kwargs)
    return wrapper
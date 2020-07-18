from abc import ABC
from collections import OrderedDict


class Distribution(ABC):
    @staticmethod
    def get_char_distribution():
        pass

    @staticmethod
    def digraph_distribution():
        pass

    @staticmethod
    def trigraph_distribution():
        pass
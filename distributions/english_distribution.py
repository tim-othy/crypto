from collections import OrderedDict
from distributions.distribution import Distribution


class EnglishDistribution(Distribution):

    @staticmethod
    def get_char_distribution():
        return OrderedDict({
            'a': 0.08167,
            'b': 0.01492,
            'c': 0.02782,
            'd': 0.04253,
            'e': 0.12702,
            'f': 0.02228,
            'g': 0.02015,
            'h': 0.06094,
            'i': 0.06966,
            'j': 0.00153,
            'k': 0.00772,
            'l': 0.04025,
            'm': 0.02406,
            'n': 0.06749,
            'o': 0.07507,
            'p': 0.01929,
            'q': 0.00095,
            'r': 0.05987,
            's': 0.06327,
            't': 0.09056,
            'u': 0.02758,
            'v': 0.00978,
            'w': 0.02360,
            'x': 0.00150,
            'y': 0.01974,
            'z': 0.00074
        })

    @staticmethod
    def get_digraph_distribution():
        return OrderedDict({
            "th": 0.0259995,
            "he": 0.0223754,
            "in": 0.0194831,
            "er": 0.017141,
            "an": 0.0155056,
            "re": 0.0135386,
            "es": 0.0126823,
            "on": 0.0126478,
            "st": 0.0120041,
            "nt": 0.0112669,
            "en": 0.010887,
            "at": 0.0107277,
            "ed": 0.0103662,
            "nd": 0.0102654,
            "to": 0.0102478,
            "or": 0.0101612,
            "ea": 0.00962885,
            "ti": 0.00953081,
            "ar": 0.00941184,
            "te": 0.00939907,
            "ng": 0.00857053,
            "al": 0.00849146,
            "it": 0.00843079,
            "as": 0.0083942,
            "is": 0.0083,
            "ha": 0.00799374,
            "et": 0.00730501,
            "se": 0.00700717,
            "ou": 0.00691384,
            "of": 0.00678687

        })

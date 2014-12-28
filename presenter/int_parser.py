__author__ = 'novy'


class IntParser(object):
    def parse(self, string):
        if string is None:
            return None

        try:
            return int(string)
        except ValueError:
            return None
# -*- coding: utf-8 -*-
import os
from ..empty import empty


class BaseReporter(object):

    def __init__(self, ctx, error):
        self.ctx = ctx
        self.error = error

    def cut(self, value, size=40):
        text = str(value)
        return text[0:size] + ' ...' if len(text) > size else text

    def linefy(self, value):
        return str(value).replace(os.linesep, r'\n')

    def indentify(self, value):
        if not isinstance(value, str):
            return value

        lines = value.split(os.linesep)
        return '\n    '.join(lines)

    def normalize(self, value, size=20, use_raw=True):
        if value is None:
            return value

        try:
            value = str(value)
        except:
            value = value

        if not hasattr(value, '__len__'):
            return value

        if use_raw and self.from_operator('raw_mode'):
            return self.indentify(value)
        else:
            return self.linefy(self.cut(value))

    def safe_length(self, value):
        try:
            return len(value)
        except:
            return '"unmeasurable"'

    def from_operator(self, name, defaults=None, operator=None):
        operator = operator or getattr(self.error, 'operator', None)
        if not operator:
            return defaults

        value = getattr(operator, name, defaults)
        return defaults if value is empty else value

    def render_tmpl(self, tmpl, value):
        placeholders = {}

        if '{value}' in tmpl:
            placeholders['value'] = self.normalize(value)

        if '{type}' in tmpl:
            placeholders['type'] = type(value).__name__

        if '{length}' in tmpl:
            placeholders['length'] = self.safe_length(value)

        return tmpl.format(**placeholders)

    def run(self, error):
        raise NotImplementedError('run() method must be implemented')

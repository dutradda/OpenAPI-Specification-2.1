#!/usr/bin/env python

from swagger_spec_validator.validator20 import validate_spec
from os import path
from six import iteritems

import functools
import json
import logging
import os.path
import pathlib
import urllib.parse

logging.basicConfig(level=logging.DEBUG)
ROOT_PATH = path.dirname(path.abspath(__file__))


class Handler(object):

    def __init__(self, base_path=''):
        base_path = pathlib.Path(base_path)

        if base_path.is_absolute():
            root_path = base_path
        else:
            root_path = path.join(ROOT_PATH, base_path)

        self.root_path = root_path

    def __call__(self, ref):
        ref_path = path.join(self.root_path, ref)
        return json.load(open(ref_path))


def apis_defs_getter(object_, deref):
    new_object = {}
    for key, value in iteritems(object_):
        value = deref(value)
        if key == 'allOf':
            for all_of_i in value:
                for key_i, value_i in iteritems(deref(all_of_i)):
                    new_object[key_i] = deref(value_i)
        else:
            new_object[key] = value

    return new_object


class UrlJoin(object):

    def __init__(self):
        self._scheme_cache = {}
        self._isabs_cache = {}

    def __call__(self, old_uri, new_uri):
        if not self._uri_has_scheme(old_uri) and \
                not self._uri_is_isabs(old_uri):
            common_prefix = os.path.commonprefix([old_uri, new_uri])
            new_uri = new_uri.replace(common_prefix, '')

        return urllib.parse.urljoin(old_uri, new_uri)
    
    def _uri_has_scheme(self, old_uri):
        scheme = self._scheme_cache.get(old_uri)

        if scheme is None:
            scheme = urllib.parse.urlsplit(old_uri).scheme
            self._scheme_cache[old_uri] = scheme

        return scheme

    def _uri_is_isabs(self, old_uri):
        isabs = self._isabs_cache.get(old_uri)

        if isabs is None:
            isabs = os.path.isabs(old_uri)
            self._isabs_cache[old_uri] = isabs

        return isabs


schema = json.load(open('schema.json'))
spec = json.load(open(os.path.join(ROOT_PATH, 'swagger.json')))
handlers = {'': Handler('')}
urljoin_cache = functools.lru_cache(1024)(UrlJoin())

validate_spec(spec, schema_dict=schema, custom_handlers=handlers,
              apis_getter=apis_defs_getter,
              definitions_getter=apis_defs_getter,
              urljoin_cache=urljoin_cache)

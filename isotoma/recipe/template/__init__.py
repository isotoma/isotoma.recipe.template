# Copyright 2010 Isotoma Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import os
import zc.buildout
from Cheetah.Template import Template as Tmpl
import simplejson

try:
    from hashlib import sha1
except ImportError:
    import sha 
    def sha1(str):
        return sha.new(str)


class LazyDictTransform(object):

    def __init__(self, dict):
        self.internal = dict

    def has_key(self, key):
        return key in self.internal

    def __getitem__(self, key):
        if not key in self.internal:
            raise KeyError("'%s' not found" % key)
        val = self.internal[key].strip()
        if val.startswith("[") or val.startswith("{"):
            val = simplejson.loads(val)
        return val

    def __iter__(self):
        return self.internal.__iter__()


class Template(object):

    def __init__(self, buildout, name, options):
        self.name = name
        self.options = options
        self.buildout = buildout

        # Record a SHA1 of the template we use, so we can detect changes in subsequent runs
        self.options["__hashes_input"] = sha1(open(self.options["input"]).read()).hexdigest()

    def install(self):
        template = open(self.options['input']).read()
        cfgfilename = self.options['output']

        if not cfgfilename.startswith("/"):
            cfgfilename = os.path.join(self.buildout['buildout']['parts-directory'], cfgfilename)

        dir, file = os.path.split(cfgfilename)
        if not os.path.isdir(dir):
            os.makedirs(dir)

        c = Tmpl(template, searchList=LazyDictTransform(self.options))
        open(cfgfilename, "w").write(str(c))
        return [cfgfilename]

    def update(self):
        pass


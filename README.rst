Template buildout recipe
========================

This recipe provides buildout_ with a generic way to fill in a template from
buildout parameters. Lists and dictionaries are supported using JSON syntax.

.. _buildout: http://pypi.python.org/pypi/zc.buildout


Mandatory Parameters
--------------------

input
    Path to a template (in Cheetah format)
output
    Where to write the template


Example
-------

In your template::

    ${hello_world}
    #for $bar in $foo
    $bar
    #end for

And in your buildout.cfg::

    [buildout]
    parts = template

    [template]
    recipe = isotoma.recipe.template
    input = template.cfg
    output = myfile.cfg
    hello_world = Hello World
    foo = ['foo', 'bar', 'baz']


Repository
----------

This software is available from our `recipe repository`_ on github.

.. _`recipe repository`: http://github.com/isotoma/recipes

License
-------

Copyright 2010 Isotoma Limited

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.



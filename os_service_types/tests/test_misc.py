# -*- coding: utf-8 -*-

# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""
test_misc
---------

Miscellaneous tests
"""

from os_service_types import service_types
from os_service_types.tests import base


class TestMisc(base.TestCase):

    def test_normalize(self):
        self.assertEqual('foo-bar', service_types._normalize_type('foo_bar'))

    def test_normalize_none(self):
        self.assertIsNone(service_types._normalize_type(None))

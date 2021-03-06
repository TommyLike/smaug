#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo_config import cfg

from smaug.context import RequestContext
from smaug.services.protection.clients import swift
from smaug.tests import base


class SwiftClientTest(base.TestCase):
    def setUp(self):
        super(SwiftClientTest, self).setUp()
        service_catalog = [
            {
                'endpoints': [
                    {'publicURL': 'http://127.0.0.1:8080/v1/AUTH_abcd', }
                ],
                'type': 'object-store',
                'name': 'swift',
            },
        ]

        self._context = RequestContext(user_id='admin',
                                       project_id='abcd',
                                       auth_token='efgh',
                                       service_catalog=service_catalog)

        self.conf = cfg.ConfigOpts()
        swift.register_opts(self.conf)

    def test_create_client_by_endpoint(self):
        self.conf.set_default('swift_endpoint',
                              'http://127.0.0.1:8080/v1',
                              'swift_client')

        sc = swift.create(self._context, self.conf)
        self.assertEqual('http://127.0.0.1:8080/v1/AUTH_abcd', sc.url)

    def test_create_client_by_catalog(self):
        sc = swift.create(self._context, cfg.CONF)
        self.assertEqual('http://127.0.0.1:8080/v1/AUTH_abcd', sc.url)

    def test_create_client_by_keystone(self):
        self.conf.set_default('swift_auth_url',
                              'http://127.0.0.1:5000/v2.0',
                              'swift_client')
        self.conf.set_override('swift_user', 'admin', 'swift_client')
        self.conf.set_override('swift_key', 'secrete', 'swift_client')
        self.conf.set_override('swift_tenant_name', 'abcd', 'swift_client')
        sc = swift.create(self._context, self.conf)
        self.assertEqual(sc.authurl, 'http://127.0.0.1:5000/v2.0')
        self.assertEqual(sc.user, 'admin')
        self.assertEqual(sc.key, 'secrete')
        self.assertEqual(sc.os_options['tenant_name'], 'abcd')

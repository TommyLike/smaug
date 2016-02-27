# Copyright 2012, Red Hat, Inc.
#
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

"""
Client side of the protection manager RPC API.
"""

from oslo_config import cfg
import oslo_messaging as messaging

from smaug.objects import base as objects_base
from smaug import rpc


CONF = cfg.CONF


class ProtectionAPI(object):
    """Client side of the protection rpc API.

    API version history:

        1.0 - Initial version.
    """

    RPC_API_VERSION = '1.0'

    def __init__(self):
        super(ProtectionAPI, self).__init__()
        target = messaging.Target(topic=CONF.protection_topic,
                                  version=self.RPC_API_VERSION)
        serializer = objects_base.SmaugObjectSerializer()
        self.client = rpc.get_client(target, version_cap=None,
                                     serializer=serializer)

    def restore(self, ctxt, restore=None):
        cctxt = self.client.prepare(version='1.0')
        return cctxt.call(
            ctxt,
            'restore',
            restore=restore)

    def list_protectable_types(self, ctxt):
        cctxt = self.client.prepare(version='1.0')
        return cctxt.call(
            ctxt,
            'list_protectable_types')

    def show_protectable_type(self, ctxt, protectable_type=None):
        cctxt = self.client.prepare(version='1.0')
        return cctxt.call(
            ctxt,
            'show_protectable_type',
            protectable_type=protectable_type)

    def list_protectable_instances(
            self, ctxt, protectable_type=None,
            marker=None, limit=None, sort_keys=None,
            sort_dirs=None, filters=None):
        cctxt = self.client.prepare(version='1.0')
        return cctxt.call(
            ctxt,
            'list_protectable_instances',
            protectable_type=protectable_type,
            marker=marker,
            limit=limit,
            sort_keys=sort_keys,
            sort_dirs=sort_dirs,
            filters=filters)

    def list_protectable_dependents(self,
                                    ctxt, protectable_id=None,
                                    protectable_type=None):
        cctxt = self.client.prepare(version='1.0')
        return cctxt.call(
            ctxt,
            'list_protectable_dependents',
            protectable_id=protectable_id,
            protectable_type=protectable_type)

    def show_provider(self,
                      ctxt, provider_id=None):
        cctxt = self.client.prepare(version='1.0')
        return cctxt.call(
            ctxt,
            'show_provider',
            provider_id=provider_id)

    def list_providers(self, ctxt, marker=None, limit=None,
                       sort_keys=None,
                       sort_dirs=None, filters=None):
        cctxt = self.client.prepare(version='1.0')
        return cctxt.call(
            ctxt,
            'list_providers',
            marker=marker,
            limit=limit,
            sort_keys=sort_keys,
            sort_dirs=sort_dirs,
            filters=filters)

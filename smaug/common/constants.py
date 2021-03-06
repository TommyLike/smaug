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

#  operation type
OPERATION_TYPES = (
    OPERATION_PROTECT,
    OPERATION_RESTORE,
    OPERATION_DELETE,
    OPERATION_START,
    OPERATION_SUSPEND,
) = (
    'protect',
    'restore',
    'delete',
    'start',
    'suspend',
)


#  plugin type
PLUGIN_BANK = 'bank'

# supported resource types
RESOURCE_TYPES = (PROJECT_RESOURCE_TYPE,
                  SERVER_RESOURCE_TYPE,
                  VOLUME_RESOURCE_TYPE,
                  IMAGE_RESOURCE_TYPE,
                  ) = ('OS::Keystone::Project',
                       'OS::Nova::Server',
                       'OS::Cinder::Volume',
                       'OS::Glance::Image',
                       )

CHECKPOINT_STATUS_ERROR = 'error'
CHECKPOINT_STATUS_PROTECTING = 'protecting'
CHECKPOINT_STATUS_AVAILABLE = 'available'
CHECKPOINT_STATUS_DELETING = 'deleting'
CHECKPOINT_STATUS_DELETED = 'deleted'
CHECKPOINT_STATUS_ERROR_DELETING = 'error-deleting'

# resource status
RESOURCE_STATUS_ERROR = 'error'
RESOURCE_STATUS_PROTECTING = 'protecting'
RESOURCE_STATUS_AVAILABLE = 'available'
RESOURCE_STATUS_DELETING = 'deleting'
RESOURCE_STATUS_DELETED = 'deleted'
RESOURCE_STATUS_UNDEFINED = 'undefined'

# scheduled operation state
OPERATION_STATE_INIT = 'init'
OPERATION_STATE_REGISTERED = 'registered'
OPERATION_STATE_TRIGGERED = 'triggered'
OPERATION_STATE_RUNNING = 'running'
OPERATION_STATE_DELETED = 'deleted'

# scheduled operation run type
OPERATION_RUN_TYPE_EXECUTE = 'execute'
OPERATION_RUN_TYPE_RESUME = 'resume'

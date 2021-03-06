# coding: utf-8
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from testinfra.backend import base


class LocalBackend(base.BaseBackend):
    NAME = "local"

    def __init__(self, *args, **kwargs):
        super(LocalBackend, self).__init__("local", **kwargs)

    def get_pytest_id(self):
        return "local"

    @classmethod
    def get_hosts(cls, host, **kwargs):
        return [host]

    def run(self, command, *args, **kwargs):
        return self.run_local(self.get_command(command, *args))

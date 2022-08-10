# Copyright © 2022 Province of British Columbia
#
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
"""Example JSON segments of Certificate of Good Standing."""
from .common import BUSINESS, REGISTRAR_INFO

COGS = {
    'business': BUSINESS,
    'entityAct': 'Business Corporations Act',
    'entityDescription': 'BC Benefit Company',
    'registrarInfo': REGISTRAR_INFO,
    'reportDateTime': '2022-08-05T16:49:06.231324+00:00',
    'reportType': 'cogs'
}

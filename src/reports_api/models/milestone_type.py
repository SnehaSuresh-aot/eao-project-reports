# Copyright © 2019 Province of British Columbia
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
"""Model to handle all operations related to Milestone Type."""

from sqlalchemy import Column, String, Integer

from .code_table import CodeTable
from .db import db

class MilestoneType(db.Model,CodeTable):
    """Model class for Milestone Type."""
    __tablename__ = 'milestone_types'
    id = Column(Integer, primary_key=True, autoincrement=True)  # TODO check how it can be inherited from parent
    name = Column(String,nullable=False)
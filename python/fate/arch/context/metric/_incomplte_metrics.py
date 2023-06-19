#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
from ._type import InCompleteMetrics


class StepMetrics(InCompleteMetrics):
    complete = False

    def __init__(self, name, namespace, type, data, metadata) -> None:
        self.name = name
        self.namespace = namespace
        self.type = type
        self.data = data
        self.metadata = metadata

    def merge(self, metrics: InCompleteMetrics):
        if not isinstance(metrics, StepMetrics):
            raise ValueError(f"can't merge metrics type `{metrics}` with StepMetrics")
        if metrics.type != self.type:
            raise ValueError(f"can't merge metrics type `{metrics}` with StepMetrics named `{self.name}`")
        if metrics.namespace != self.namespace:
            raise ValueError(
                f"can't merge metrics namespace `{self.namespace}` with `{metrics.namespace}` named `{self.name}`"
            )

        return StepMetrics(
            name=self.name,
            type=self.type,
            namespace=self.namespace,
            data=[*self.data, *metrics.data],
            metadata=self.metadata,
        )

    def dict(self) -> dict:
        return dict(
            name=self.name,
            namespace=self.namespace,
            type=self.type,
            metadata=self.metadata,
            data=self.data,
        )

    @classmethod
    def from_dict(cls, d) -> "StepMetrics":
        return StepMetrics(**d)

    def __str__(self):
        return f"StepMetrics(name={self.name}, type={self.type}, namespace={self.namespace}, data={self.data}, metadata={self.metadata})"

    def __repr__(self):
        return self.__str__()

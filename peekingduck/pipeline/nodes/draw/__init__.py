# Copyright 2022 AI Singapore
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Draws results/outputs to an image.

.. deprecated:: 1.2.0 |br|
    :mod:`draw.image_processor` is deprecated, and replaced by the nodes :mod:`augment.brightness`
    and :mod:`augment.contrast`.
"""

from . import (
    bbox,
    blur_bbox,
    btm_midpoint,
    group_bbox_and_tag,
    heat_map,
    legend,
    mosaic_bbox,
    poses,
    tag,
    zones,
)

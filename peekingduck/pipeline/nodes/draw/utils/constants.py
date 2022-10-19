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
Constants used for drawing
"""

# colors
CHAMPAGNE = (156, 223, 244)
BLIZZARD = (241, 232, 164)
VIOLET_BLUE = (188, 118, 119)
TOMATO = (77, 103, 255)
BROWN = (96, 109, 167)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PRIMARY_PALETTE_LENGTH = 5
PRIMARY_PALETTE = [CHAMPAGNE, BLIZZARD, TOMATO, VIOLET_BLUE, BROWN]

# constants for thickness
THIN = 1
THICK = 2
VERY_THICK = 3

# constant to fill shapes in cv2. To be replace line thickness
FILLED = -1

# constants for font scale
SMALL_FONTSCALE = 0.5
NORMAL_FONTSCALE = 1
BIG_FONTSCALE = 2

# constants used for image manipulation
LOWER_SATURATION = 0.5

# constants for pts
POINT_RADIUS = 5

# constants for masks
SATURATION_STEPS = 8
SATURATION_MINIMUM = 100
ALPHA = 0.5
CONTOUR_COLOR = (0, 0, 0)
DEFAULT_CLASS_COLOR = (204, 204, 204)
# fmt: off
CLASS_COLORS = {
    "person": CHAMPAGNE,

    "bicycle":      BLIZZARD,
    "car":          BLIZZARD,
    "motorcycle":   BLIZZARD,
    "airplane":     BLIZZARD,
    "bus":          BLIZZARD,
    "train":        BLIZZARD,
    "truck":        BLIZZARD,
    "boat":         BLIZZARD,

    "traffic light":    (79,14,136),
    "fire hydrant":     (79,14,136),
    "stop sign":        (79,14,136),
    "parking meter":    (79,14,136),
    "bench":            (79,14,136),

    "bird":     TOMATO,
    "cat":      TOMATO,
    "dog":      TOMATO,
    "horse":    TOMATO,
    "sheep":    TOMATO,
    "cow":      TOMATO,
    "elephant": TOMATO,
    "bear":     TOMATO,
    "zebra":    TOMATO,
    "giraffe":  TOMATO,

    "backpack": (0,51,0),
    "umbrella": (0,51,0),
    "handbag":  (0,51,0),
    'tie':      (0,51,0),
    "suitcase": (0,51,0),

    "frisbee":          (140,20,74),
    "skis":             (140,20,74),
    "snowboard":        (140,20,74),
    "sports ball":      (140,20,74),
    "kite":             (140,20,74),
    "baseball bat":     (140,20,74),
    "baseball glove":   (140,20,74),
    "skateboard":       (140,20,74),
    "surfboard":        (140,20,74),
    "tennis racket":    (140,20,74),

    "bottle":       (0,111,255),
    "wine glass":   (0,111,255),
    "cup":          (0,111,255),
    "fork":         (0,111,255),
    "knife":        (0,111,255),
    "spoon":        (0,111,255),
    "bowl":         (0,111,255),

    "banana":   BROWN,
    "apple":    BROWN,
    "sandwich": BROWN,
    "orange":   BROWN,
    "broccoli": BROWN,
    "carrot":   BROWN,
    "hot dog":  BROWN,
    "pizza":    BROWN,
    "donut":    BROWN,
    "cake":     BROWN,

    "chair":        (155,87,1),
    "couch":        (155,87,1),
    "potted plant": (155,87,1),
    "bed":          (155,87,1),
    "dining table": (155,87,1),
    "toilet":       (155,87,1),

    "tv":           VIOLET_BLUE,
    "laptop":       VIOLET_BLUE,
    "mouse":        VIOLET_BLUE,
    "remote":       VIOLET_BLUE,
    "keyboard":     VIOLET_BLUE,
    "cell phone":   VIOLET_BLUE,

    "microwave":    (12,54,191),
    "oven":         (12,54,191),
    "toaster":      (12,54,191),
    "sink":         (12,54,191),
    "refrigerator": (12,54,191),

    "book":         (35,39,62),
    "clock":        (35,39,62),
    "vase":         (35,39,62),
    "scissors":     (35,39,62),
    "teddy bear":   (35,39,62),
    "hair drier":   (35,39,62),
    "toothbrush":   (35,39,62),
}
# fmt: on

# color map with keys as color name and values as BGR values
# {champagne, blizzard, violet blue, tomato} are colors from PeekingDuck
COLOR_MAP = {
    "champagne": (156, 223, 244),
    "blizzard": (241, 232, 164),
    "violet blue": (188, 118, 119),
    "tomato": (77, 103, 255),
    "aliceblue": (255, 248, 240),
    "antiquewhite": (215, 235, 250),
    "aqua": (255, 255, 0),
    "aquamarine": (212, 255, 127),
    "azure": (255, 255, 240),
    "beige": (220, 245, 245),
    "bisque": (196, 228, 255),
    "black": (0, 0, 0),
    "blanchedalmond": (205, 235, 255),
    "blue": (255, 0, 0),
    "blueviolet": (226, 43, 138),
    "brown": (42, 42, 165),
    "burlywood": (135, 184, 222),
    "cadetblue": (160, 158, 95),
    "chartreuse": (0, 255, 127),
    "chocolate": (30, 105, 210),
    "coral": (80, 127, 255),
    "cornflowerblue": (237, 149, 100),
    "cornsilk": (220, 248, 255),
    "crimson": (60, 20, 220),
    "cyan": (255, 255, 0),
    "darkblue": (139, 0, 0),
    "darkcyan": (139, 139, 0),
    "darkgoldenrod": (11, 134, 184),
    "darkgray": (169, 169, 169),
    "darkgreen": (0, 100, 0),
    "darkgrey": (169, 169, 169),
    "darkkhaki": (107, 183, 189),
    "darkmagenta": (139, 0, 139),
    "darkolivegreen": (47, 107, 85),
    "darkorange": (0, 140, 255),
    "darkorchid": (204, 50, 153),
    "darkred": (0, 0, 139),
    "darksalmon": (122, 150, 233),
    "darkseagreen": (143, 188, 143),
    "darkslateblue": (139, 61, 72),
    "darkslategray": (79, 79, 47),
    "darkslategrey": (79, 79, 47),
    "darkturquoise": (209, 206, 0),
    "darkviolet": (211, 0, 148),
    "deeppink": (147, 20, 255),
    "deepskyblue": (255, 191, 0),
    "dimgray": (105, 105, 105),
    "dimgrey": (105, 105, 105),
    "dodgerblue": (255, 144, 30),
    "firebrick": (34, 34, 178),
    "floralwhite": (240, 250, 255),
    "forestgreen": (34, 139, 34),
    "fuchsia": (255, 0, 255),
    "gainsboro": (220, 220, 220),
    "ghostwhite": (255, 248, 248),
    "gold": (0, 215, 255),
    "goldenrod": (32, 165, 218),
    "gray": (128, 128, 128),
    "green": (0, 128, 0),
    "greenyellow": (47, 255, 173),
    "grey": (128, 128, 128),
    "honeydew": (240, 255, 240),
    "hotpink": (180, 105, 255),
    "indianred": (92, 92, 205),
    "indigo": (130, 0, 75),
    "ivory": (240, 255, 255),
    "khaki": (140, 230, 240),
    "lavender": (250, 230, 230),
    "lavenderblush": (245, 240, 255),
    "lawngreen": (0, 252, 124),
    "lemonchiffon": (205, 250, 255),
    "lightblue": (230, 216, 173),
    "lightcoral": (128, 128, 240),
    "lightcyan": (255, 255, 224),
    "lightgoldenrodyellow": (210, 250, 250),
    "lightgray": (211, 211, 211),
    "lightgreen": (144, 238, 144),
    "lightgrey": (211, 211, 211),
    "lightpink": (193, 182, 255),
    "lightsalmon": (122, 160, 255),
    "lightseagreen": (170, 178, 32),
    "lightskyblue": (250, 206, 135),
    "lightslategray": (153, 136, 119),
    "lightslategrey": (153, 136, 119),
    "lightsteelblue": (222, 196, 176),
    "lightyellow": (224, 255, 255),
    "lime": (0, 255, 0),
    "limegreen": (50, 205, 50),
    "linen": (230, 240, 250),
    "magenta": (255, 0, 255),
    "maroon": (0, 0, 128),
    "mediumaquamarine": (170, 205, 102),
    "mediumblue": (205, 0, 0),
    "mediumorchid": (211, 85, 186),
    "mediumpurple": (219, 112, 147),
    "mediumseagreen": (113, 179, 60),
    "mediumslateblue": (238, 104, 123),
    "mediumspringgreen": (154, 250, 0),
    "mediumturquoise": (204, 209, 72),
    "mediumvioletred": (133, 21, 199),
    "midnightblue": (112, 25, 25),
    "mintcream": (250, 255, 245),
    "mistyrose": (225, 228, 255),
    "moccasin": (181, 228, 255),
    "navajowhite": (173, 222, 255),
    "navy": (128, 0, 0),
    "oldlace": (230, 245, 253),
    "olive": (0, 128, 128),
    "olivedrab": (35, 142, 107),
    "orange": (0, 165, 255),
    "orangered": (0, 69, 255),
    "orchid": (214, 112, 218),
    "palegoldenrod": (170, 232, 238),
    "palegreen": (152, 251, 152),
    "paleturquoise": (238, 238, 175),
    "palevioletred": (147, 112, 219),
    "papayawhip": (213, 239, 255),
    "peachpuff": (185, 218, 255),
    "peru": (63, 133, 205),
    "pink": (203, 192, 255),
    "plum": (221, 160, 221),
    "powderblue": (230, 224, 176),
    "purple": (128, 0, 128),
    "rebeccapurple": (153, 51, 102),
    "red": (0, 0, 255),
    "rosybrown": (143, 143, 188),
    "royalblue": (225, 105, 65),
    "saddlebrown": (19, 69, 139),
    "salmon": (114, 128, 250),
    "sandybrown": (96, 164, 244),
    "seagreen": (87, 139, 46),
    "seashell": (238, 245, 255),
    "sienna": (45, 82, 160),
    "silver": (192, 192, 192),
    "skyblue": (235, 206, 135),
    "slateblue": (205, 90, 106),
    "slategray": (144, 128, 112),
    "slategrey": (144, 128, 112),
    "snow": (250, 250, 255),
    "springgreen": (127, 255, 0),
    "steelblue": (180, 130, 70),
    "tan": (140, 180, 210),
    "teal": (128, 128, 0),
    "thistle": (216, 191, 216),
    # "tomato": (71, 99, 255),
    "turquoise": (208, 224, 64),
    "violet": (238, 130, 238),
    "wheat": (179, 222, 245),
    "white": (255, 255, 255),
    "whitesmoke": (245, 245, 245),
    "yellow": (0, 255, 255),
    "yellowgreen": (50, 205, 154),
}

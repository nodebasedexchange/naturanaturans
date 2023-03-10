# Grabbing the projects
import sys
sys.path.append('/glasbey-main/')
import glasbey
from matplotlib import pyplot as plt
import seaborn as sea

# Extending Natura Naturans for if you want different colors than the Base16 provided.
# Recommended that you keep the parameters mostly the same as it is a "Naturally Matte" Color Theme
# Check out the documentation for parameters that are supported for Extending Natura Naturans
# https://glasbey.readthedocs.io/en/latest/index.html

print(glasbey.extend_palette("#55AABB", palette_size=16, lightness_bounds=(30, 60), chroma_bounds=(3, 40)))
sea.set()
sea.palplot(glasbey.extend_palette("#55AABB", palette_size=16, lightness_bounds=(30, 60), chroma_bounds=(3, 40)))
plt.show()

# Important to remember for changing things:
# CHANGE BOTH THE HEX CODES & THE PARAMETERS for EXTENDING Natura Naturans

# The command to extend the Color Palette:
# python3 generators/extend_color_palette.py

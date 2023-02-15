import glasbey

# This works but only shows the Hex Codes of the colors as explained in the documentation
# print(glasbey.extend_palette("#453B32", palette_size=12, lightness_bounds=(20, 40), chroma_bounds=(40, 50)))

# This one doesn't seem to work even though its directly taken from the documentation...
# print(sns.palplot(glasbey.create_palette(palette_size=12))) 

# This is from the Seaborn Color Palette Documentation which works!
# see here: https://seaborn.pydata.org/tutorial/color_palettes.html

from matplotlib import pyplot as plt
import seaborn as sns

# This is also from there but not necessary bc we're using Glasbey
# current_palette = sns.color_palette()
# sns.palplot(current_palette)
# plt.show()



# Now combine them together to view the hexcode generated WITH the Color itself
print(glasbey.extend_palette("#453B32", palette_size=12, lightness_bounds=(20, 40), chroma_bounds=(40, 50)))

sns.set()
sns.palplot(glasbey.extend_palette("#453B32", palette_size=12, lightness_bounds=(20, 40), chroma_bounds=(40, 50)))
plt.show()

# Important to Remember:
# CHANGE BOTH THE HEX CODES & THE PARAMETERS for EXTENDING/GENERATING COLOR PALETTES

# Check out the documentation for parameters that are supported for both Generating & Extending Color Palettes
# https://glasbey.readthedocs.io/en/latest/index.html
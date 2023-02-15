# Glasbey Color Generator 
The libraries/modules used for Generating/Extending the Natura Naturans' Color palette is [Glasbey](https://github.com/lmcinnes/glasbey) with the Seaborn/matplotlib addon. All of which are included in this repo.

The Glasbey documentation is [here](https://glasbey.readthedocs.io/en/latest/index.html). With the references for Glasbey being the [original repo](https://github.com/taketwo/glasbey) and the Academic Papers:
1) Glasbey, C., van der Heijden, G., Toh, V. F. K. and Gray, A. (2007),
   Colour Displays for Categorical Images <https://onlinelibrary.wiley.com/doi/10.1002/col.20327/abstract>.
   Color Research and Application, 32: 304-309

2) Luo, M. R., Cui, G. and Li, C. (2006), Uniform Colour Spaces Based on CIECAM02 Colour Appearance Model <https://onlinelibrary.wiley.com/doi/10.1002/col.20227/abstract>.
   Color Research and Application, 31: 320–330

> Glasbey is MIT Licensed 

---

## Tutorial for Extending Natura Naturans' Color Palette
This tutorial is for people using VSCode/VSCodium and that have cloned/forked/downloaded this repo for development.

1. Have `python3` installed
2. Have `pip3` configured 
3. Have this repo Downloaded


> Installing the Library user wide:
- `pip install glasbey` 
    - Which will work for most users that have the dependencies already installed.

> Installing the Library dependencies manually inside `/glasbey-main/`:

```bash
pip install setuptools
pip install numpy
pip install numba
pip install colorspacious
pip install matplotlib

# finally:
python setup.py install
```
Be sure to be inside the `/glasbey-main/` directory before running the `python setup.py install` command.

Minimum versions for the packages are:

- numpy>=1.21
- numba>=0.56
- colorspacious>=1.1
- matplotlib>=3.5

---

## Once Installed Correctly:

```bash
cd ../

# or

cd /Natura Naturans/
```
> (simply be inside the `/Natura Naturans/` root directory)

Then you can test the Glasbey Generator by running the following command in the terminal: (or clicking the "run python file" button is VSCode)

```bash
python3 extend_color_palette.py
```
If you installed everything correctly your output should look like this with a popup window showing the colors generated:

(SCREENSHOT HERE)

---

## Editing the Parameters:
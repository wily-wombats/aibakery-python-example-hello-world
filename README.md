# Getting Started

This is a sample package showing how a python model would be setup to run on
aibakery.

## Requirements

### Running locally

All dependencies are listed in the requirements.txt file.

### Packaging

Ensure the `wheel` package is installed

## How to

### Building .whl/tar.gz

To build the package. From the root directory of the project run:

```shell
python3 setup.py sdist bdist_wheel
```

This will generate a .whl and .tar.gz in the `dist` directory.

# chile-rut
Validator and generator of Chile id

[![Build Status](https://travis-ci.org/gmgarciag/chile_rut.svg?branch=master)](https://travis-ci.org/gmgarciag/chile_rut)

# Instalation

```
git clone https://github.com/gmgarciag/chile_rut.git

# In the folder of the package
python setup.py install
```

# Usage

```
import chile_rut

chile_rut.validate_rut("12345678-9")
# return False
chile_rut.validate_rut("6265837-1")
# return True

# It's works with any separator
chile_rut.validate_rut("12.345.678-9")
# return False
chile_rut.validate_rut("6/265/837-1")
# return True
```
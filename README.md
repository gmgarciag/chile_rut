# chile-rut
Validator and generator of Chile id

[![Build Status](https://travis-ci.org/gmgarciag/chile_rut.svg?branch=master)](https://travis-ci.org/gmgarciag/chile_rut)
# Instalation

```
pip install chile_rut
```

or

```
git clone https://github.com/gmgarciag/chile_rut.git
# In the folder of the package
python setup.py install
```

# Usage
## Validate rut
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

## Random rut generator
```
import chile_rut

chile_rut.get_random_rut()
# return "6265837-1"
chile_rut.get_random_ruts(number_of_ruts)
# return ["6265837-1", ""23289335-4", ...]
```

## Format rut
```
import chile_rut

chile_rut.format_rut("12345678-9")
# return "12.345.678-9"
```

## Verification digit
```
import chile_rut

chile_rut.verification_digit("6265837")
# return "1"
chile_rut.verification_digit("14065549")
# return "K"
```
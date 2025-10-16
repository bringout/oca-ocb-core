# Transifex integration


Transifex integration
=====================
This module will add a link to the Transifex project in the translation view.
The purpose of this module is to speed up translations of the main modules.

To work, Odoo uses Transifex configuration files `.tx/config` to detect the
project source. Custom modules will not be translated (as not published on
the main Transifex project).

The language the user tries to translate must be activated on the Transifex
project.
        

## Installation

```bash
pip install odoo-bringout-oca-ocb-transifex
```

## Dependencies

- base
- web

## Source

- Repository: https://github.com/OCA/OCB
- Branch: 16.0
- Path: addons/transifex

## License

This package preserves the original LGPL-3 license.

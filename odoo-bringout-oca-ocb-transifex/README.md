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

This addon depends on:
- base
- web

## Manifest Information

- **Name**: Transifex integration
- **Version**: 1.0
- **Category**: Hidden/Tools
- **License**: LGPL-3
- **Installable**: False

## Source

Based on [OCA/OCB](https://github.com/OCA/OCB) branch 16.0, addon `transifex`.

## License

This package maintains the original LGPL-3 license from the upstream Odoo project.

## Documentation

- Overview: doc/OVERVIEW.md
- Architecture: doc/ARCHITECTURE.md
- Models: doc/MODELS.md
- Controllers: doc/CONTROLLERS.md
- Wizards: doc/WIZARDS.md
- Reports: doc/REPORTS.md
- Security: doc/SECURITY.md
- Install: doc/INSTALL.md
- Usage: doc/USAGE.md
- Configuration: doc/CONFIGURATION.md
- Dependencies: doc/DEPENDENCIES.md
- Troubleshooting: doc/TROUBLESHOOTING.md
- FAQ: doc/FAQ.md

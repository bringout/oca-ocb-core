# Phone Numbers Validation


Phone Numbers Validation
========================

This module adds the feature of validation and formatting phone numbers
according to a destination country.

It also adds phone blacklist management through a specific model storing
blacklisted phone numbers.

It adds mail.thread.phone mixin that handles sanitation and blacklist of
records numbers. 

## Installation

```bash
pip install odoo-bringout-oca-ocb-phone_validation
```

## Dependencies

This addon depends on:
- base
- mail

## Manifest Information

- **Name**: Phone Numbers Validation
- **Version**: 2.1
- **Category**: Hidden
- **License**: LGPL-3
- **Installable**: False

## Source

Based on [OCA/OCB](https://github.com/OCA/OCB) branch 16.0, addon `phone_validation`.

## License

This package maintains the original LGPL-3 license from the upstream Odoo project.

## Documentation

- Overview: doc/OVERVIEW.md
- Architecture: doc/ARCHITECTURE.md
- Models: doc/MODELS.md
- Controllers: doc/CONTROLLERS.md
- Wizards: doc/WIZARDS.md
- Install: doc/INSTALL.md
- Usage: doc/USAGE.md
- Configuration: doc/CONFIGURATION.md
- Dependencies: doc/DEPENDENCIES.md
- Troubleshooting: doc/TROUBLESHOOTING.md
- FAQ: doc/FAQ.md

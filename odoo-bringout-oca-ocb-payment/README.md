# Payment Engine

Odoo addon: payment

## Installation

```bash
pip install odoo-bringout-oca-ocb-payment
```

## Patches Applied

- **Payment Provider Dependencies Removal**: External payment provider dependencies have been removed to prevent installation issues. See [doc/PATCH_REMOVE_PAYMENT_PROVIDERS.md](doc/PATCH_REMOVE_PAYMENT_PROVIDERS.md) for details.

## Dependencies

This addon depends on:
- portal

## Manifest Information

- **Name**: Payment Engine
- **Version**: 2.0
- **Category**: Hidden
- **License**: LGPL-3
- **Installable**: False

## Source

Based on [OCA/OCB](https://github.com/OCA/OCB) branch 16.0, addon `payment`.

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

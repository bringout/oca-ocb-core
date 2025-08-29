# Sparse Fields


        The purpose of this module is to implement "sparse" fields, i.e., fields
        that are mostly null. This implementation circumvents the PostgreSQL
        limitation on the number of columns in a table. The values of all sparse
        fields are stored in a "serialized" field in the form of a JSON mapping.
    

## Installation

```bash
pip install odoo-bringout-oca-ocb-base_sparse_field
```

## Dependencies

This addon depends on:
- base

## Manifest Information

- **Name**: Sparse Fields
- **Version**: 1.0
- **Category**: Hidden
- **License**: LGPL-3
- **Installable**: False

## Source

Based on [OCA/OCB](https://github.com/OCA/OCB) branch 16.0, addon `base_sparse_field`.

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

# Base import


New extensible file import for Odoo
======================================

Re-implement Odoo's file import system:

* Server side, the previous system forces most of the logic into the
  client which duplicates the effort (between clients), makes the
  import system much harder to use without a client (direct RPC or
  other forms of automation) and makes knowledge about the
  import/export system much harder to gather as it is spread over
  3+ different projects.

* In a more extensible manner, so users and partners can build their
  own front-end to import from other file formats (e.g. OpenDocument
  files) which may be simpler to handle in their work flow or from
  their data production sources.

* In a module, so that administrators and users of Odoo who do not
  need or want an online import can avoid it being available to users.


## Installation

```bash
pip install odoo-bringout-oca-ocb-base_import
```

## Dependencies

- web

## Source

- Repository: https://github.com/OCA/OCB
- Branch: 16.0
- Path: addons/base_import

## License

This package preserves the original LGPL-3 license.

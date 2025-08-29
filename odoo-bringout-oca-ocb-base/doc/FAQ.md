# FAQ

- Q: Which Odoo is this?
  - A: OCA/OCB 16.0 core runtime + base addon, Python 3.11–3.12 compatible.
- Q: Can I run only this package?
  - A: Yes, it boots Odoo and base. You’ll add feature addons via packages/.
- Q: Where are web assets handled?
  - A: Through `web` addon (separate package) and QWeb within HTTP layer.
- Q: Where are my configs stored?
  - A: Combination of `odoo.conf` and `ir.config_parameter` in DB.

# Remove Enterprise Proprietary Modules from Apps

This package is customized to remove Odoo Enterprise promotional modules from the Apps list and keep them from coming back on upgrades.

## Summary of Changes

- Stop seeding enterprise promo modules: the Base module no longer loads `data/ir_module_module.xml` that created `ir.module.module` rows with `to_buy=True` (promotional stubs pointing to Enterprise apps).
- Post-init cleanup: upon upgrading `base`, we purge any existing promotional entries with `to_buy=True` and a proprietary license.
- UI filter: the Apps action (`open_module_tree`) now has a domain `[("to_buy", "=", False)]` so any residual `to_buy=True` entries are hidden in the Apps list.

## Files Touched

- `odoo/addons/base/__manifest__.py`
  - Commented out the line that loaded `data/ir_module_module.xml`.
- `odoo/addons/base/__init__.py`
  - Extended `post_init` to delete `ir.module.module` records matching:
    - `to_buy = True`
    - `license in ['OEEL-1', 'OEEL', 'OPL-1', 'Proprietary']`
- `odoo/addons/base/views/ir_module_views.xml`
  - Added a domain on the `open_module_tree` action: `[("to_buy", "=", False)]`.

## Why

In vanilla Odoo, `base/data/ir_module_module.xml` seeds several records flagged with `to_buy=True` (e.g., Studio, Knowledge, Helpdesk, etc.), which show up in the Apps screen with an Upgrade/Install button but link to Enterprise features. This customization removes those marketing entries to keep the Apps list clean and avoid confusion.

## How to Apply

1. Upgrade the `base` module so the manifest change and post-init hook run:
   - UI: Apps → search `Base` → `Upgrade`.
   - CLI: `odoo -u base -d <your_db>` (or via your wrapper script).
2. Refresh the Apps page. The Enterprise proprietary entries should be gone.

## Notes and Caveats

 - App list updates: If you use "Update Apps List" pulling from Odoo Apps server, external data could re-introduce promotional entries. With this change, any `to_buy=True` entries matching proprietary licenses are cleaned up again on the next `base` upgrade, and the Apps action already hides `to_buy=True` entries by domain.
- Safety: The cleanup runs best-effort inside a `try/except` to avoid breaking the base post-init. It only targets obvious proprietary licenses.

## Rollback

To restore the default behavior:

1. Re-enable loading of `data/ir_module_module.xml` in `odoo/addons/base/__manifest__.py`.
2. Remove the promo cleanup block from `odoo/addons/base/__init__.py` `post_init`.
3. Upgrade `base` again: `odoo -u base -d <your_db>`.

## Related Paths

- Removed data file (not loaded anymore): `odoo/addons/base/data/ir_module_module.xml`
- Model implementing Apps logic: `odoo/addons/base/models/ir_module.py`

## Screenshot Reference

- Original issue context: `input/screenshot-2025-08-23_17-38-34.png`

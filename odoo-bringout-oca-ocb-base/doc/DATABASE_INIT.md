# Database Initialization & Fixes

This package includes critical fixes ensuring smooth database initialization on Odoo 16 with Python 3.11+.

## Module Categories Fix

Issue: missing module categories referenced by `ir_module_module.xml` during init.

Fix: add the categories to `base` data (`ir_module_category_data.xml`).

Impact: DB initializes cleanly; no more `External ID not found` errors.

## Python 3.11 Addons Path Fix

Issue: `_NamespacePath` cannot be `+`-concatenated with lists (Python 3.11+), breaking addons path handling.

Fix: cast namespace path to list before concatenation:

```python
# BEFORE
addons_paths = odoo.addons.__path__ + [root_path]
# AFTER
addons_paths = list(odoo.addons.__path__) + [root_path]
```

Impact: runtime stable on Python 3.11–3.12.

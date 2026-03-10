# QwebJSON Circular Reference Bugfix

## Problem

When loading the Odoo 19 web client, the `web.webclient_bootstrap` QWeb template
fails with:

```
ValueError: Circular reference detected
```

at the line:

```xml
<t t-out="json.dumps(session_info)"/>
```

## Root Cause

The `QwebJSON.dumps()` default handler in `odoo/addons/base/models/ir_qweb.py`
returned non-serializable objects unchanged:

```python
# Original (broken)
class QwebJSON(json.JSON):
    def dumps(self, *args, **kwargs):
        prev_default = kwargs.pop('default', lambda obj: obj)
        return super().dumps(*args, **kwargs, default=(
            lambda obj: prev_default(str(obj) if isinstance(obj, QwebContent) else obj)
        ))
```

When the JSON encoder encounters a non-serializable type (e.g. `ReadonlyDict`,
`lazy`, `datetime`, `bytes`, `Domain`), it calls the `default` handler. The handler
returns the object unchanged (since it's not `QwebContent`). The encoder tries to
serialize it again, gets the same object back, and raises "Circular reference detected."

This is a **latent bug in the Odoo 19 core**. In vanilla Odoo it rarely triggers
because `session_info` values are typically JSON-serializable. However, any module
(OCA or custom) that introduces a non-serializable type into `session_info` or any
other QWeb JSON-serialized context will expose this bug.

## Fix

Use `odoo.tools.json.json_default()` as the fallback for non-QwebContent objects:

```python
# Fixed
class QwebJSON(json.JSON):
    def dumps(self, *args, **kwargs):
        prev_default = kwargs.pop('default', lambda obj: obj)
        return super().dumps(*args, **kwargs, default=(
            lambda obj: prev_default(str(obj) if isinstance(obj, QwebContent) else json.json_default(obj))
        ))
```

`json_default()` (from `odoo/tools/json.py`) properly handles:

- `datetime` -> string via `fields.Datetime.to_string()`
- `date` -> string via `fields.Date.to_string()`
- `lazy` -> resolved value
- `ReadonlyDict` -> regular `dict`
- `bytes` -> decoded string
- `Domain` -> list
- anything else -> `str(obj)`

## File Changed

- `odoo-bringout-oca-ocb-base/odoo/addons/base/models/ir_qweb.py` (class `QwebJSON`)

## Date

2026-03-10

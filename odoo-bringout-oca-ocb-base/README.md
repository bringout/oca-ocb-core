# Odoo Bringout OCA OCB Base

This package provides the core Odoo runtime from the OCA (Odoo Community Association) OCB (Odoo Community Backports) project, packaged for pythonic development.

## What's Included

- Core Odoo runtime (`odoo/` directory)
- Base addon with essential functionality
- Essential test addons
- Command line interface (`odoo` command)

## Installation

```bash
pip install odoo-bringout-oca-ocb-base
```

## Usage

After installation, you can start Odoo with:

```bash
odoo --addons-path=/path/to/your/addons --database=your_database
```

## Python 3.11+ Compatibility

⚠️ **IMPORTANT**: This package includes a critical fix for Python 3.11+ compatibility.

### Issue
Odoo 16.0 has a namespace path compatibility issue with Python 3.11+ that causes module loading failures:
```
TypeError: unsupported operand type(s) for +: '_NamespacePath' and 'list'
```

### Fix Applied
**File:** `odoo/tools/misc.py` (line 169)
```python
# BEFORE (broken in Python 3.11+)
addons_paths = odoo.addons.__path__ + [root_path]

# AFTER (fixed)
addons_paths = list(odoo.addons.__path__) + [root_path]
```

### Root Cause
In Python 3.11+, namespace packages return `_NamespacePath` objects instead of regular lists. The `_NamespacePath` type doesn't support the `+` operator for concatenation with lists.

### Impact
Without this fix, Python 3.11+ environments experience:
- ❌ "Couldn't load module base" errors
- ❌ "Couldn't load module web" errors  
- ❌ Complete web server startup failures
- ❌ All Odoo module loading broken

With this fix:
- ✅ Full Python 3.11+ compatibility
- ✅ All modules load correctly
- ✅ Web server works properly
- ✅ Backward compatible with Python 3.10 and earlier

## Database Initialization Fix

⚠️ **IMPORTANT**: This package includes critical fixes for Odoo 16.0 database initialization.

### Issue
Odoo 16.0 has database initialization failures due to missing module categories in the base module. The database initialization would fail with:
```
ValueError: External ID not found in the system: base.module_category_services_timesheets
psycopg2.errors.UndefinedTable: relation "ir_module_module" does not exist
```

### Root Cause
The `ir_module_module.xml` data file referenced 7 module categories that were not defined in the base module's `ir_module_category_data.xml`, creating circular dependency issues during initialization:

- `module_category_services_timesheets`
- `module_category_services_project`
- `module_category_inventory_inventory` 
- `module_category_manufacturing_manufacturing`
- `module_category_sales_sales`
- `module_category_marketing_email_marketing`
- `module_category_website_website`

### Fix Applied
**File:** `odoo/addons/base/data/ir_module_category_data.xml`

Added all 7 missing module categories with proper hierarchical structure:
```xml
<!-- Services subcategories -->
<record model="ir.module.category" id="module_category_services_project">
    <field name="name">Project</field>
    <field name="parent_id" ref="module_category_services"/>
    <field name="sequence">15</field>
</record>

<record model="ir.module.category" id="module_category_services_timesheets">
    <field name="name">Timesheets</field>
    <field name="parent_id" ref="module_category_services"/>
    <field name="description">Helps you manage the timesheets.</field>
    <field name="sequence">13</field>
</record>

<!-- Similar additions for inventory, manufacturing, sales, marketing, and website categories -->
```

### Impact
Without these fixes, database initialization would:
- ❌ Fail with "External ID not found" errors
- ❌ Leave database in corrupted state
- ❌ Prevent web server from functioning
- ❌ Block all Odoo functionality

With these fixes:
- ✅ Database initializes successfully in ~2.5s
- ✅ All module categories properly defined
- ✅ Web server starts and functions correctly  
- ✅ Cron jobs and background tasks work
- ✅ Complete Odoo functionality available

## Documentation

- Overview: doc/OVERVIEW.md
- Architecture: doc/ARCHITECTURE.md
- Startup: doc/STARTUP.md
- ORM: doc/ORM.md
- HTTP: doc/HTTP.md
- Modules: doc/MODULES.md
- Base Addon: doc/BASE_ADDON.md
- Security: doc/SECURITY.md
- Configuration: doc/CONFIG.md
- CLI: doc/CLI.md
- DB Init & Fixes: doc/DATABASE_INIT.md
- Troubleshooting: doc/TROUBLESHOOTING.md
- FAQ: doc/FAQ.md

## Package Dependencies

This package follows pythonic dependency management and can be used with standard Python tools like:

- `uv` for fast dependency resolution
- `pip` for package installation  
- `pyproject.toml` for configuration

## Source

Based on [OCA/OCB](https://github.com/OCA/OCB) branch 16.0 with Python 3.11+ compatibility fixes applied.

## Enterprise Promotional Modules Removal

This package hides and removes Odoo Enterprise promotional modules (to_buy=True) from the Apps list.

- Summary and rationale: `doc/ENTERPRISE_REMOVE.md`
- Changes include:
  - Stopping load of `data/ir_module_module.xml` (promo seed)
  - Post-init cleanup of existing promo entries
  - UI domain on Apps action to hide `to_buy=True`

## License

This package maintains the original LGPL-3 license from the upstream Odoo project.

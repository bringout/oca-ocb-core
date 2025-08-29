# Troubleshooting

## Addons Path Issues
- Ensure `addons_path` includes both this package and your custom addons.
- On Python 3.11+, verify the namespace path fix is applied (included here).

## Database Init Errors
- Missing categories: fixed by this package; if seen, re-install base.
- `relation "ir_module_module" does not exist`: ensure DB user has privileges; retry init.

## Web Startup
- Port 8069 conflicts: change with `--http-port`.
- `public`/`portal` access issues: check group and record rules in base.

## Filestore Permissions
- Ensure `data_dir` is writable by the Odoo process.

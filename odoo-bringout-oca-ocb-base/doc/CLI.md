# CLI

Entrypoints to manage Odoo from the command line.

## `odoo-bin`
- Start the server: `odoo-bin -c odoo.conf`
- Initialize DB: `-d dbname -i base`
- Update modules: `-u module1,module2`

## Common Flags
- `--addons-path=/path1,/path2`
- `--db_host`, `--db_port`, `--db_user`, `--db_password`
- `--http-port=8069`, `--longpolling-port=8072`
- `--workers=0` (single process) or `>0` (multi workers)

## Logs
- `--log-level=info` (or debug_sql, debug_rpc)
- Logs go to stdout or file via `--logfile`

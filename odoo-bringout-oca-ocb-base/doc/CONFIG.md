# Configuration

## Sources
- `odoo.conf` INI file (path via `-c` flag or defaults)
- CLI flags (e.g., `--db_host`, `--addons-path`)
- `ir.config_parameter` (DB-scoped runtime key/values)
- Environment variables (rarely used, mainly for testing)

## Important Options
- Database: `db_host`, `db_port`, `db_user`, `db_password`
- HTTP: `xmlrpc_port`/`http_port`, `longpolling_port`
- Workers: `workers`, `limit_time_cpu`, `limit_memory_hard`
- Paths: `addons_path`, `data_dir` (filestore)

## Addons Path
- Multiple paths comma-separated
- Python 3.11 namespace path fix applied in this package

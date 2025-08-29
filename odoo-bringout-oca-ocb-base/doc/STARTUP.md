# Startup Flow

```mermaid
sequenceDiagram
    participant U as User
    participant OBIN as odoo-bin
    participant CLI as odoo.cli
    participant SRV as odoo.service.server
    participant MOD as odoo.modules
    participant REG as Registry
    participant HTTP as HTTP Server
    participant PG as Postgres

    U->>OBIN: invoke with args
    OBIN->>CLI: parse config/args
    CLI->>SRV: start() with conf
    SRV->>PG: connect(db)
    SRV->>MOD: load_modules(graph)
    MOD->>REG: build registry (models, fields)
    REG-->>MOD: ready
    SRV->>HTTP: start WSGI workers
    HTTP-->>U: listen on :8069
```

Phases
- Configuration: `odoo.conf`, CLI flags, env vars.
- Database: check, create (if init), connect.
- Modules graph: resolve dependencies, install/upgrade as needed.
- Registry build: import Python files, register models, fields, methods.
- HTTP server: start in single-process or multi-worker mode.
- Services: cron, longpolling bus, reports, i18n.

Workers Modes
- Single worker (dev): everything in one process (default here).
- Multi worker: master + workers via `--workers N`.

```mermaid
flowchart LR
  CONF[odoo.conf] --> CLI[CLI Parser]
  CLI --> SVC[Service]
  SVC --> DB[(PostgreSQL)]
  SVC --> MOD[Module Loader]
  MOD --> REG[Registry]
  REG --> ORM[ORM]
  SVC --> HTTP[HTTP/WSGI]
```

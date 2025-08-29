# Architecture

This package provides the Odoo core runtime and the `base` addon. It sits at the center of every other addon.

```mermaid
flowchart LR
    subgraph CLI
      OBIN[`odoo-bin`]
      CLI[CLI Entrypoints]
    end
    subgraph Core
      CONF[Config Loader]
      SRV[Server Service]
      REG[Registry]
      ORM[Models and ORM]
      MOD[Modules Loader]
      HTTP[HTTP Layer]
      QWEB[QWeb Templates]
      TOOLS[Tools misc ustr date]
    end
    subgraph Services
      PG[(PostgreSQL)]
      CRON[Cron]
      BUS[Bus]
      I18N[I18n]
      REPORT[Reports]
      FS[(Filestore)]
    end
    subgraph Base Addon
      IRM[ir.model and ir.model.fields]
      IRUI[ir.ui.menu and ir.actions]
      IRSEC[ir.model.access ir.rule res.groups]
      RES[res.users res.partner res.company res.currency]
      IRATT[ir.attachment]
      IRCONF[ir.config_parameter]
    end

    OBIN --> CLI --> CONF --> SRV --> REG
    SRV --> HTTP -->|routes| BaseControllers
    SRV --> CRON
    REG --> ORM --> PG
    MOD --> REG
    QWEB --> HTTP
    ORM --> FS
    ORM --> REPORT
    ORM --> TOOLS

    BaseControllers -.import.-> HTTP
    IRM --> ORM
    IRUI --> HTTP
    IRSEC -. enforces .-> ORM
    RES --> ORM
    IRATT --> ORM
    IRCONF --> ORM

    BUS <--> HTTP
```

Key Points
- Registry: process-wide metadata for all models, caches, and methods.
- ORM: `models.Model`, fields, environment, and caching. All addons extend here.
- HTTP: WSGI app; controllers decorated with `@http.route` handle requests.
- Modules Loader: resolves addons path, reads manifests, installs/updates.
- Base Addon: provides the essential models that enable everything else.
- Services: PostgreSQL connections, cron workers, bus long-polling, i18n.

# ORM

Core concepts that power Odoo’s data layer.

## Models and Registry
- `models.Model`: base class for all business models.
- Registry: per-database object storing model classes, metadata, caches.
- Environment: `(cr, uid, context)` wrapped as `env`, provides cursors and context.

## Fields
- Basic: `Char`, `Text`, `Boolean`, `Integer`, `Float`, `Date`, `Datetime`.
- Monetary & Currency: `Monetary` with `currency_field`.
- Relational: `Many2one`, `One2many`, `Many2many`.
- Computed, inverse, depends; stored vs. non-stored.

## APIs
- New API (`@api.model`, `@api.depends`, `@api.constrains`, `@api.onchange`).
- Environment access: `self.env.cr`, `self.env.user`, `self.env.ref()`.
- Access rights: `check_access_rights`, `sudo()`, record rules.

## Cache & Prefetch
- Prefetch groups reads to reduce queries.
- Cache invalidates on write/create/unlink.

## Base Addon Foundation
- `ir.model`, `ir.model.fields`: model metadata registry.
- `res.users`, `res.partner`, `res.company`: identity and company models.
- `ir.attachment`: binary storage via filestore.
- `ir.config_parameter`: runtime config key/value store.

```mermaid
flowchart LR
  REG[Registry] --> ENV[Environment]
  ENV --> ORM[models.Model]
  ORM --> SQL[SQL (psycopg2)]
  ORM --> CACHE[Cache/Prefetch]
  ORM --> SEC[Access + Rules]
```

# Security Model

## Access Rights
- `ir.model.access`: per-model CRUD access per group.
- Default entries for base models, extended by modules.

## Record Rules
- Domain-based filtering of accessible records.
- Multi-company isolation rules in base.

## Groups
- `res.groups` organized by application category.
- Inheritance via `implied_ids`.

## Sudo & Superuser
- `sudo()` to bypass rules for system operations.
- User ID `1` is superuser.

## Portal / Public
- `public` user for anonymous access.
- `portal` group for shared documents and portal pages.

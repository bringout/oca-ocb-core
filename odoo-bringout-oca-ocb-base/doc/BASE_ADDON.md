# Base Addon Deep Dive

The `base` addon provides the foundation for all Odoo applications.

## Key Models
- `ir.model`, `ir.model.fields`: model metadata and fields registry.
- `ir.ui.menu`, `ir.actions.*`: client actions and menu hierarchy.
- `ir.config_parameter`: runtime configuration key/value store.
- `ir.attachment`: binary attachments with filestore storage.
- `res.users`, `res.groups`, `res.company`, `res.partner`, `res.currency`.

```mermaid
classDiagram
  class ir_model
  class ir_model_fields
  class ir_ui_menu
  class ir_actions
  class ir_config_parameter
  class ir_attachment
  class res_users
  class res_groups
  class res_company
  class res_partner
  class res_currency

  ir_model <.. ir_model_fields
  res_users --> res_groups
  res_users --> res_company
  res_partner --> res_company
  ir_ui_menu --> ir_actions
  ir_attachment --> res_users
```

## Controllers
- Minimal endpoints for attachments and common actions.

## Security
- Group definitions and default access rights via `ir.model.access.csv`.
- Record rules for multi-company and user-specific data.

## Data
- Seed actions, menus, parameters, currencies, companies, languages.

## Notes
- Many application modules only extend these models via `_inherit`.

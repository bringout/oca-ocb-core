# Security

Access control and security definitions in uom.

## Access Control Lists (ACLs)

Model access permissions defined in:
- **[ir.model.access.csv](../uom/security/ir.model.access.csv)**
  - 4 model access rules

## Record Rules

Row-level security rules defined in:

## Security Groups & Configuration

Security groups and permissions defined in:
- **[uom_security.xml](../uom/security/uom_security.xml)**
  - 1 security groups defined

```mermaid
graph TB
    subgraph "Security Layers"
        A[Users] --> B[Groups]
        B --> C[Access Control Lists]
        C --> D[Models]
        B --> E[Record Rules]
        E --> F[Individual Records]
    end
```

Security files overview:
- **[ir.model.access.csv](../uom/security/ir.model.access.csv)**
  - Model access permissions (CRUD rights)
- **[uom_security.xml](../uom/security/uom_security.xml)**
  - Security groups, categories, and XML-based rules

Notes
- Access Control Lists define which groups can access which models
- Record Rules provide row-level security (filter records by user/group)
- Security groups organize users and define permission sets
- All security is enforced at the ORM level by Odoo

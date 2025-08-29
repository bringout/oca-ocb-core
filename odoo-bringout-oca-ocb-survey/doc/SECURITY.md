# Security

Access control and security definitions in survey.

## Access Control Lists (ACLs)

Model access permissions defined in:
- **[ir.model.access.csv](../survey/security/ir.model.access.csv)**
  - 22 model access rules

## Record Rules

Row-level security rules defined in:

## Security Groups & Configuration

Security groups and permissions defined in:
- **[survey_security.xml](../survey/security/survey_security.xml)**
  - 2 security groups defined

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
- **[ir.model.access.csv](../survey/security/ir.model.access.csv)**
  - Model access permissions (CRUD rights)
- **[survey_security.xml](../survey/security/survey_security.xml)**
  - Security groups, categories, and XML-based rules

Notes
- Access Control Lists define which groups can access which models
- Record Rules provide row-level security (filter records by user/group)
- Security groups organize users and define permission sets
- All security is enforced at the ORM level by Odoo

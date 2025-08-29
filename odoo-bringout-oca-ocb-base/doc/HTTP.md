# HTTP Layer

Request handling and routing.

## Controllers
- Defined with `@http.route` in Python files.
- Support auth: `public`, `user`, `none`.
- Return types: HTML (QWeb), JSON, files.

## Request Lifecycle
```mermaid
sequenceDiagram
    participant C as Client
    participant W as WSGI
    participant R as Router
    participant CTR as Controller
    participant T as QWeb

    C->>W: HTTP Request
    W->>R: match route
    R->>CTR: call method
    CTR->>T: render template (optional)
    T-->>C: HTML/JSON/Stream
```

## Sessions & Security
- CSRF tokens for forms.
- `request.env` and `request.uid` for user context.
- Access rules enforced by ORM.

## Base Addon
- Provides base controllers for menus, actions, attachments APIs.

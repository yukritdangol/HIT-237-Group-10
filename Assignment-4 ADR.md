# Architectural Decision Record (ADR)

# Remote Housing Crisis Management System

---

# ADR 001 — Authentication and Role-Based Access

## Status

Accepted

## Context

The application required authenticated workflows to separate standard users, housing managers, and administrators. Different user types required different permissions and dashboard functionality.

## Alternatives Considered

1. Single user model without roles
2. Custom Django user model
3. Django authentication with separate profile model

## Decision

The team selected Django’s built-in authentication system combined with a separate `UserProfile` model for role management.

Roles implemented:

* USER
* MANAGER
* ADMIN

This allowed separation of authentication concerns from domain-specific user information.

## Code Reference

* `accounts/models.py`
* `accounts/views.py`
* `dashboard.html`

## Consequences

### Positive

* Simplified authentication implementation
* Reused Django security features
* Easier role expansion
* Clear permission boundaries

### Negative

* Additional database join between User and UserProfile
* Slightly more complex dashboard logic

---

# ADR 002 — Service Layer Architecture

## Status

Accepted

## Context

Business logic was initially embedded directly inside Django views. As functionality increased, the application required better separation of concerns.

## Alternatives Considered

1. Keep logic inside views
2. Use Django forms only
3. Introduce dedicated service layer

## Decision

A dedicated service layer (`HousingService`) was implemented to encapsulate housing-related business logic.

The service layer handles:

* housing creation
* validation
* filtering
* availability management

## Code Reference

* `housing/services/housing_service.py`
* `housing/views.py`

## Consequences

### Positive

* Cleaner views
* Improved maintainability
* Easier testing
* Better scalability

### Negative

* Additional abstraction layer
* Slightly increased project complexity

---

# ADR 003 — Middleware Exception Handling

## Status

Accepted

## Context

The application required centralized exception handling to avoid repetitive try-except blocks inside views and to improve user experience.

## Alternatives Considered

1. Handle exceptions inside each view
2. Use default Django error pages
3. Implement custom middleware

## Decision

Custom middleware (`GlobalExceptionMiddleware`) was implemented to intercept domain-specific exceptions and render structured error pages.

Exceptions handled:

* InvalidHousingPriceError
* HousingNotAvailableError
* UnauthorizedActionError

## Code Reference

* `housing/middleware.py`
* `housing/exceptions.py`
* `templates/errors/`

## Consequences

### Positive

* Centralized error management
* Cleaner views
* Improved UX
* Reusable architecture

### Negative

* Additional middleware complexity
* Requires template maintenance

---

# ADR 004 — Testing Strategy

## Status

Accepted

## Context

The project required meaningful testing beyond trivial assertions. The team needed a maintainable testing structure that covered core functionality and permission boundaries.

## Alternatives Considered

1. Minimal smoke tests
2. Single tests.py file
3. Structured modular test suite

## Decision

A modular testing structure was implemented using:

* model tests
* service tests
* view tests
* permission tests

Testing focused on:

* business behaviour
* role restrictions
* exception handling
* authenticated workflows

## Code Reference

* `housing/tests/test_models.py`
* `housing/tests/test_services.py`
* `housing/tests/test_views.py`

## Consequences

### Positive

* Better reliability
* Easier regression prevention
* Clearer testing responsibilities
* Improved maintainability

### Negative

* Increased development time
* Additional maintenance overhead

---

# ADR 005 — Template Inheritance and Shared UI

## Status

Accepted

## Context

The application initially used duplicated HTML structures across templates, resulting in inconsistent navigation and styling.

## Alternatives Considered

1. Independent templates
2. Copy-pasted layouts
3. Shared base template

## Decision

A shared `base.html` template was implemented using Django template inheritance.

Shared components:

* navbar
* global styling
* success messages
* responsive layout

## Code Reference

* `templates/base.html`
* `dashboard.html`
* `housing_list.html`
* `login.html`
* `signup.html`

## Consequences

### Positive

* Consistent UI
* Easier maintenance
* Cleaner architecture
* Improved UX

### Negative

* Template dependency chain
* More initial setup work

---

# ADR 006 — Feature Evolution from Assessment 2

## Status

Accepted

## Context

Assessment 4 required significant feature growth from Assessment 2 while continuing development within the same repository and architecture.

## Decision

The application evolved from a basic housing listing system into a role-based housing management platform with:

* authentication
* dashboards
* service layer architecture
* middleware exception handling
* modular testing
* improved UX

## Consequences

### Positive

* Greater architectural maturity
* Improved feature completeness
* More realistic workflows
* Better maintainability

### Negative

* Increased application complexity
* Additional documentation requirements

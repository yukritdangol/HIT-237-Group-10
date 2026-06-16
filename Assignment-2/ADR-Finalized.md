
# Architectural Decision Records

This document presents the significant decisions made concerning the development of the design for the Remote Housing Crisis Application.

# ADR 1: Use of Django Framework
## Status
Accepted

## Context
The development of a framework is a requirement for the management of remote housing crisis associated data.

## Options Considered
- Flask (less structure, lightweight)
- Node.js (different stack)

## Decision
Integration of an Object Relational Mapper (ORM) along with an admin interface in Django allows for structured architectural and high-performance web app development.

## Code Reference
housing_project/settings.py

## Consequences
- Quicker development implementation time
- Less flexible than lightweight web frameworks

# ADR 2: Use of the Django ORM for Managing Databases
## Status
Accepted

## Context
Management and storage of housing data must occur effectively.

## Options Considered
- Execute queries directly on the database using raw SQL
- Use of a NoSQL database

## Decision
The Django ORM was chosen as the preferred option due to its ability to provide streamlined interactions with the database while maintaining clean code.

## Code Reference
housing/models.py

## Consequences
- Enhanced data storage and management
- Decreased ability to optimize query performance

# ADR 3: Use a Foreign Key Relationship between Housing and Location

## Status
Accepted

## Context
Housing data must be associated with specific locations to reflect real-world relationships and avoid duplication.

## Options Considered
- Using a CharField for location (simple but no relationship)
- Creating unrelated models without links

## Decision
A ForeignKey relationship was implemented between Housing and Location models to maintain relational integrity.

## Code Reference
housing/models.py: (ForeignKey field in Housing model)

## Consequences
- Structured relational data
- Prevents duplication
- Requires joins when querying

# ADR 4: Use Class-Based Views

## Status
Accepted

## Context
The application requires a structured way to display housing data.

## Options Considered
- Function-based views
- Static HTML pages

## Decision
Class-based views were used to improve reusability and maintainability.

## Code Reference
housing/views.py:1–20

## Consequences
- Better code structure
- Reusable components
- Slight learning curve

# ADR 5: Use QuerySet Filtering

## Status
Accepted

## Context
Only relevant housing (available properties) should be displayed.

## Options Considered
- Display all housing
- Filter manually in templates

## Decision
QuerySet filtering was used to show only available housing.

## Code Reference
housing/views.py:10–25

## Consequences
- Efficient data retrieval
- Improved user experience
- Requires understanding of ORM

# ADR 6: Follow Django Design Philosophy (DRY & MTV)

## Status
Accepted

## Context
The project requires clean, maintainable, and scalable code.

## Options Considered
- Repeating logic in multiple files
- Mixing logic and UI

## Decision
The project follows:
- DRY (Don't Repeat Yourself)
- MTV (Model-Template-View)

## Code Reference
housing/models.py, views.py, templates/

## Consequences
- Cleaner codebase
- Easier maintenance
- Requires structured planning
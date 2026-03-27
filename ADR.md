
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
Housing data must be related to location in order to demonstrate the connection between the two.

## Options Considered
- Creating housing location using text field, and make various other feilds corresponding to the topic
- Creating separate models without any relationship, which will help create a better feild of vision and better data from all sources.

### Decision
The Django admin panel is used for efficient management and testing. 

### Code Reference
housing/admin.py

### Consequences
- Faster development and testing
- Limited customization
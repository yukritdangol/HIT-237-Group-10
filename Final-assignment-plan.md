# Assessment 4 – Final Plan of work

## Group Project Progress Update

This checkpoint outlines the architectural restructuring, planning, and project reorganization completed for Assessment 4. At this stage, the group has not yet implemented major functionality or written the final business logic code. However, significant progress has been made in preparing the project structure to align with the updated assessment requirements, lecturer feedback, and marking rubric expectations.

The team focused primarily on restructuring the existing Django application, redefining responsibilities, improving system architecture planning, and preparing the repository for scalable development.

---

# Project Restructuring and Architectural Changes

## Transition to a Multi-App Django Architecture

One of the major changes completed during this checkpoint was restructuring the project into a modular multi-app Django architecture.

The original implementation used a simpler structure with limited separation between responsibilities. Based on lecturer feedback and Assessment 4 requirements, the project was redesigned into multiple Django apps to improve scalability, maintainability, and separation of concerns.

The planned architecture now includes:

- `accounts` app
- `housing` app
- optional `services/core` layer for business logic orchestration

This restructuring prepares the system for clearer module ownership and cleaner code organization.

### Purpose of the Change

The multi-app approach was introduced to:

- separate authentication logic from housing management logic
- improve maintainability
- support modular testing
- enable role-based workflows
- allow better scalability for future features
- align with industry-standard Django practices

The new structure also supports better implementation of service layers and permission boundaries.

---

# Authentication and User Management Planning

## Accounts Application Preparation

The `accounts` app structure has been added and prepared for implementing:

- user registration
- login/logout functionality
- role-based access control
- protected routes/pages
- dashboard permissions

Although full authentication logic has not yet been implemented, required files, routing structure, and placeholders have been prepared to support future integration.

The team also planned role-specific workflows for:

- administrators
- housing managers
- standard users/students

This redesign ensures future implementation can properly separate user permissions and responsibilities.

---

# Service Layer Architecture Preparation

## Business Logic Separation

Another major improvement completed during this checkpoint was planning and preparing a service layer architecture.

The group identified that much of the previous logic was tightly coupled inside views. To improve separation of concerns, the project structure is being reorganized so that:

- views remain lightweight
- business logic moves into `services.py`
- database operations become easier to manage
- workflows become reusable
- testing becomes more maintainable

The service layer preparation includes planning for:

- housing allocation workflows
- request processing
- transaction management
- reusable business operations
- future scalability

This structure aligns with concepts covered during weekly tutorials and lecturer recommendations.

---

# Exception Handling Improvements

## Structured Exception Handling Design

The project structure has also been updated to support structured exception handling.

The team prepared the project for:

- custom exception classes
- centralized error handling
- middleware-based exception responses
- domain-specific validation handling

This change was introduced to improve:

- debugging
- code readability
- application stability
- maintainability

The exception-handling strategy will later be integrated into the service layer implementation.

---

# Testing Strategy Preparation

## Modular Testing Planning

The team also planned a more advanced testing structure compared to previous assessments.

The testing strategy now includes:

- app-level test organization
- service-layer testing
- authentication testing
- permission boundary testing
- integration testing
- edge case validation

The planned structure includes files such as:

```text
accounts/tests.py
housing/tests.py

# ADR and Documentation Improvements

## Architectural Decision Record (ADR) Evolution

The documentation structure has also been updated significantly.

The team prepared an improved ADR structure to document:

- architectural changes
- superseded decisions
- iterative development improvements
- rationale behind redesign choices

This helps demonstrate the evolution of the project from earlier assessments into a more scalable and production-oriented architecture.

The documentation now aims to clearly show:

- why changes were made
- what limitations existed previously
- how the new design improves the system

---

# System Design and Diagram Planning

## Updated Design Documentation

Preparation has begun for updating:

- ER diagrams
- class diagrams
- sequence diagrams
- architecture diagrams

These diagrams will later reflect:

- multi-app architecture
- authentication flows
- service-layer communication
- housing request workflows
- allocation processing

This planning ensures consistency between implementation and documentation.

---

# Repository and File Organization

## Codebase Cleanup and Reorganization

During this checkpoint, the repository was reorganized to improve maintainability and readability.

This included:

- restructuring folders
- preparing app-level separation
- organizing templates
- reorganizing routes
- preparing modular settings/configuration
- updating placeholder files for future implementation

Although functionality is not yet complete, the repository now reflects the intended architecture required for Assessment 4.

---

# Team Contribution Overview

## Yukrit

Focused on:

- authentication architecture preparation
- role-based workflow planning
- project integration structure
- repository restructuring
- protected route planning

---

## Aarjit

Focused on:

- service layer architecture planning
- separation of concerns
- exception handling structure
- business logic organization
- workflow restructuring

---

## Aanchal

Focused on:

- ADR evolution documentation
- architecture documentation updates
- planning updated diagrams
- documenting design changes

---

## Merina

Focused on:

- testing strategy planning
- permission boundary testing preparation
- integration testing structure
- modular test organization

---

# Current Project Status

At the current checkpoint stage:

## Completed

- Project restructuring
- Multi-app architecture setup
- Authentication planning
- Service layer planning
- Exception handling preparation
- Testing strategy preparation
- ADR restructuring
- Repository cleanup and organization
- Design documentation planning

---

## In Progress

- Actual implementation of authentication
- Business logic coding
- Service layer implementation
- Database workflow integration
- Full frontend/backend connectivity
- Automated testing implementation
- Final diagram updates

---

# Conclusion

This checkpoint primarily focused on architectural redesign, restructuring, and preparation work required to align the project with the updated Assessment 4 expectations and lecturer feedback.

Although major functionality has not yet been implemented, the group has completed substantial groundwork that prepares the system for scalable development, modular testing, role-based workflows, and cleaner software architecture.

The project is now positioned for the next development phase, where planned structures and workflows will be fully implemented into the application.
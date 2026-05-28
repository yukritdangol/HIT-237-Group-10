# Updated Project Plan — Assessment 4

# Remote Housing Crisis Management System

---

# Project Overview

The Remote Housing Crisis Management System is a Django-based web application designed to support housing accessibility and management within remote Northern Territory communities. The project evolved from Assessment 2 by introducing authentication, role-based access control, service layer architecture, middleware-based exception handling, and a structured testing suite.

The application now supports multiple user roles including community users, housing managers, and administrators.

---

# Project Objectives

* Implement secure user authentication
* Introduce role-based dashboards and permissions
* Encapsulate business logic using a service layer
* Implement centralized exception handling
* Create meaningful automated tests
* Improve overall feature maturity and UX consistency
* Maintain scalable and modular architecture

---

# Updated Features Implemented

## Authentication and Authorization

* User registration
* User login/logout
* Role-based access control
* UserProfile model

## Housing Management

* Housing listings
* Housing creation
* Availability management
* Location filtering

## Service Layer

* HousingService abstraction
* Business validation
* Reusable housing workflows

## Middleware Exception Handling

* Global exception middleware
* Custom error pages
* Structured error responses

## Testing

* Model tests
* Service tests
* Permission tests
* View tests

## UI Improvements

* Shared base template
* Responsive navbar
* Dashboard improvements
* Consistent styling

---

# Team Responsibilities

| Team Member | Responsibilities                                  |
| ----------- | ------------------------------------------------- |
| Yukrit      | Authentication, dashboards, UI integration        |
| Aarjit      | Service layer, housing workflows, permissions     |
| Aanchal     | Middleware, exceptions, structured error handling |
| Merina      | Testing suite, validation, documentation support  |

---

# Development Timeline

| Phase   | Tasks                                          | Status    |
| ------- | ---------------------------------------------- | --------- |
| Phase 1 | Assessment 2 continuation and repository setup | Completed |
| Phase 2 | Authentication and dashboards                  | Completed |
| Phase 3 | Service layer implementation                   | Completed |
| Phase 4 | Middleware and exception handling              | Completed |
| Phase 5 | Testing implementation                         | Completed |
| Phase 6 | UI polishing and navigation consistency        | Completed |
| Phase 7 | Documentation and supplementary materials      | Completed |

---

# Tools and Technologies

* Python 3
* Django 4.2
* SQLite3
* HTML/CSS
* GitHub
* Visual Studio Code

---

# Risks Encountered

* Migration conflicts during authentication integration
* Template inheritance path issues
* Role permission debugging
* Middleware template resolution errors

---

# Risk Mitigation Strategies

* Regular GitHub commits
* Shared debugging sessions
* Modular application structure
* Layered testing strategy

---

# Final Outcome

The final application evolved significantly from Assessment 2 into a more mature multi-role housing management platform demonstrating authentication, layered architecture, exception handling, modular testing, and improved user experience.

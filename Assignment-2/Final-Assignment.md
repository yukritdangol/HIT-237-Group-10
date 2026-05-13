# Remote Housing Crisis Application

## Project Overview
This project is a Django-based web application developed to address challenges related to housing availability in remote communities. The system allows users to view housing listings, manage data through an admin panel, and ensures only relevant (available) housing is displayed.

The application demonstrates strong architectural design, object-oriented principles, and proper use of Django frameworks and tools.

---

## Features
- Display housing listings dynamically
- Filter only available housing using QuerySets
- Relational database using ForeignKey (Housing ↔ Location)
- Admin panel for managing data
- Class-based views for structured backend logic
- Clean UI using Django templates

---

## Technologies Used
- Python
- Django
- SQLite (default Django database)
- HTML (Django Templates)
- Git & GitHub

---

## Architecture & Design
The application follows Django’s **Model-Template-View (MTV)** architecture and key design philosophies:

- **DRY (Don't Repeat Yourself)** – avoids redundant code
- **Separation of Concerns** – models, views, and templates are separated
- **ORM Usage** – database handled via Django ORM

All major architectural decisions are documented in the `ADR.md` file.

---

Team Contributions
- Yukrit
Developed frontend interface using Django templates
Implemented class-based views and routing
Integrated models with UI
- Aarjit
Implemented QuerySet filtering (available housing only)
Designed models and relationships (ForeignKey)
Improved backend data handling
- Aanchal
Created and maintained the ADR (Architectural Decision Records)
Documented design decisions, alternatives, and code references
Ensured alignment with Django design philosophies
- Merina
Conducted system testing (models, views, filtering)
Documented testing process
Collected and organised screenshots as evidence
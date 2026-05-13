# Testing Documentation

## 1. Server Test
- Ran Django development server using:
  python manage.py runserver
- Result: Server started successfully without errors

---

## 2. Admin Panel Test
- Accessed admin panel at /admin
- Logged in using superuser credentials
- Result: Admin panel accessible and functional

---

## 3. Model Testing

### Location Model
- Added multiple location entries (e.g., Wurrumiyanga, Maningrida)
- Result: Locations saved and displayed correctly

### Housing Model
- Added housing entries with:
  - Title
  - Location (ForeignKey)
  - Price
  - Description
  - Availability
- Result: Data stored correctly and linked to locations

---

## 4. Relationship Testing
- Verified that each housing entry is linked to a location
- Result: ForeignKey relationship working correctly

---

## 5. View Testing
- Accessed homepage (/)
- Verified that housing listings are displayed
- Result: Data rendered successfully using class-based view

---

## 6. QuerySet Testing
- Marked some housing as unavailable in admin
- Refreshed homepage
- Result: Only available housing displayed (filter working correctly)

---

## 7. UI Testing
- Verified layout and readability of housing listings page
- Result: Clean and structured UI displayed correctly

---

## Conclusion
All core functionalities of the application have been tested successfully, including models, relationships, views, and filtering logic.
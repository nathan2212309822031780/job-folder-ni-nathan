# Job Applicant Dashboard

A Django web application to manage and view Junior Developer applicants and their portfolios.

## Features
- Admin panel to create applicants and portfolios
- List view of all applicants with Bootstrap-styled table
- Detail view of applicant's portfolio
- Deletion of applicants
- Bootstrap hosted locally (no CDN)

## Tech Stack
- Django
- Bootstrap (local static files)
- SQLite (default DB)

## Installation

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

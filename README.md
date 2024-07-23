# Research Academic Blog

Welcome to the Academic Blog repository! This project is dedicated to research and development in areas like NLP applications, AI, machine learning.

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Wagtail Integration](#wagtail-integration)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This repository contains the research content and the academic blog for sharing insights and developments in relevant fields. It is designed to provide information and updates on various research topics and projects.

## Project Structure

- `mysite/` - Contains the Wagtail blog application code and configuration.
- `blog/` - blog article contains.
- `research/` - Contains research papers, articles, and other academic content.
- `menu/` - menu of our blog.
- `publication/` - Contains  our prevous paper.
- `requirements.txt` - Python  and wagtail dependencies for the project.
- `manage.py` - Django management script for running and managing the Wagtail application.
- `README.md` - This file, providing an overview of the project.

## Setup Instructions

To set up this project locally, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/Research-Academic-Blog.git
   cd Research-Academic-Blog

2. **Create and Activate a Virtual Environment::**
   ```python
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Dependencies:**
   ```python
   pip install -r requirements.txt
4. **Apply Migrations:**
   ```python
  python manage.py migrate

5. **Create a Superuser:**
   ```python
   python manage.py createsuperuser
6. **Run the Development Server:**
   ```pyhton
   python manage.py runserver

## Wagtail Integration
This project uses Wagtail CMS for managing the blog content. The Wagtail configuration files are located in the blog/ directory.

blog/models.py - Contains the Wagtail page models for the blog.
blog/wagtail_hooks.py - Contains custom hooks and configurations for the Wagtail admin interface.
blog/templates/ - Contains templates used by Wagtail for rendering pages.
For detailed information on configuring and using Wagtail, refer to the Wagtail documentation https://docs.wagtail.org/en/stable/.

## Contributing

We welcome contributions from the community. Please follow our contributing guidelines for more details on how to contribute to this project.


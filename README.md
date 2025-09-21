# Professional Portfolio Website

A modern, responsive portfolio website built with Django and Bootstrap. Features a clean design with sections for showcasing projects, skills, certificates, and contact information.

## Features

- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Modern UI**: Clean, professional design with smooth animations
- **Project Showcase**: Display your projects with images, descriptions, and technology tags
- **Skills Section**: Visual representation of your technical skills with proficiency levels
- **Contact Form**: Functional contact form with email integration
- **Admin Interface**: Easy content management through Django admin
- **SEO Friendly**: Optimized for search engines
- **Fast Loading**: Optimized assets and efficient database queries
- **Interactive Features**: JavaScript enhancements for better user experience

## Technology Stack

- **Backend**: Django 4.2.7
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Database**: SQLite (development), PostgreSQL (production ready)
- **Image Processing**: Pillow
- **Configuration**: python-decouple for environment variables

## Models

### Portfolio
Main portfolio information including name, title, bio, contact details, and profile image.

### Project
Project showcase with title, description, images, live/source URLs, and technology tags.

### Skill
Technical skills with proficiency levels and categories (Programming, Frameworks, Tools, etc.).

### Technology
Technology tags for projects with customizable colors.

### Certificate
Professional certificates with issuing organization and dates.

### Recommendation
Letters of recommendation from colleagues and supervisors.

### ContactMessage
Messages received through the contact form.

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd professional-portfolio
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv portfolio_env
   
   # On Windows
   portfolio_env\Scripts\activate
   
   # On macOS/Linux
   source portfolio_env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env file with your settings
   ```

5. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Populate with sample data (optional)**
   ```bash
   python manage.py populate_portfolio
   ```

8. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

9. **Run the development server**
   ```bash
   python manage.py runserver
   ```

10. **Access the website**
    - Main site: http://127.0.0.1:8000/
    - Admin interface: http://127.0.0.1:8000/admin/

## Customization

### Adding Content
1. Access the Django admin interface at `/admin/`
2. Add your portfolio information, projects, skills, and certificates
3. Upload images for projects and profile picture

1. **Portfolio Information**: Update your basic information in the Portfolio section
2. **Skills**: Add your technical skills with proficiency levels
3. **Projects**: Showcase your work with images, descriptions, and links
4. **Certificates**: Upload and display your professional certifications
5. **Recommendations**: Add letters of recommendation from colleagues

### Managing Projects

- Use the "Featured" checkbox to highlight projects on the homepage
- Use the "Order" field to control the display order
- Add technology tags to enable filtering
- Upload high-quality images for better presentation

### Contact Form

- Contact messages are saved to the database
- Email notifications are sent to the admin email
- Messages can be managed through the admin panel

## Deployment

### Production Settings

1. **Security**:
   - Change `SECRET_KEY` in settings.py
   - Set `DEBUG = False`
   - Configure `ALLOWED_HOSTS`

2. **Static Files**:
   - Run `python manage.py collectstatic`
   - Configure static file serving

3. **Database**:
   - Use PostgreSQL or MySQL for production
   - Update database settings accordingly

4. **Email**:
   - Configure proper SMTP settings
   - Use a reliable email service provider

### Recommended Hosting Platforms

- **Heroku**: Easy deployment with PostgreSQL
- **DigitalOcean**: VPS with full control
- **AWS**: Scalable cloud hosting
- **PythonAnywhere**: Simple Python hosting

## Customization Tips

1. **Branding**: Update colors, fonts, and logo in the CSS file
2. **Content**: Use the admin panel to easily manage all content
3. **Layout**: Modify HTML templates for different layouts
4. **Features**: Add new models and views for additional functionality

## Support

For issues or questions:
1. Check the Django documentation
2. Review the code comments
3. Ensure all dependencies are installed correctly
4. Check the Django admin panel for proper configuration

## License

This project is open source and available under the MIT License.

---

**Happy coding!** 🚀

// Portfolio Website JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Smooth scrolling for navigation links
    const navLinks = document.querySelectorAll('a[href^="#"]');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Add loading animation for forms
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function() {
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';
                submitBtn.disabled = true;
            }
        });
    });

    // Project filtering functionality
    const filterButtons = document.querySelectorAll('.filter-btn');
    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            const tech = this.dataset.tech;
            filterProjects(tech);
            
            // Update active button
            filterButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
        });
    });

    // Skills progress animation
    const skillBars = document.querySelectorAll('.skill-progress');
    const observerOptions = {
        threshold: 0.5,
        rootMargin: '0px 0px -50px 0px'
    };

    const skillObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const progressBar = entry.target;
                const percentage = progressBar.dataset.percentage;
                progressBar.style.width = percentage + '%';
            }
        });
    }, observerOptions);

    skillBars.forEach(bar => {
        skillObserver.observe(bar);
    });
});

// Project filtering function
function filterProjects(tech) {
    const url = tech ? `/api/filter-projects/?tech=${encodeURIComponent(tech)}` : '/api/filter-projects/';
    
    fetch(url)
        .then(response => response.json())
        .then(data => {
            const projectsContainer = document.getElementById('projects-container');
            if (projectsContainer) {
                updateProjectsDisplay(data.projects);
            }
        })
        .catch(error => {
            console.error('Error filtering projects:', error);
        });
}

// Update projects display
function updateProjectsDisplay(projects) {
    const container = document.getElementById('projects-container');
    if (!container) return;

    container.innerHTML = '';
    
    projects.forEach(project => {
        const projectCard = createProjectCard(project);
        container.appendChild(projectCard);
    });
}

// Create project card element
function createProjectCard(project) {
    const card = document.createElement('div');
    card.className = 'col-md-6 col-lg-4 mb-4';
    
    const techTags = project.technologies.map(tech => 
        `<span class="badge" style="background-color: ${tech.color}">${tech.name}</span>`
    ).join(' ');
    
    card.innerHTML = `
        <div class="card h-100 project-card">
            <img src="${project.image_url}" class="card-img-top" alt="${project.title}">
            <div class="card-body">
                <h5 class="card-title">${project.title}</h5>
                <p class="card-text">${project.short_description}</p>
                <div class="mb-3">${techTags}</div>
                <div class="d-flex gap-2">
                    ${project.live_url ? `<a href="${project.live_url}" class="btn btn-primary btn-sm" target="_blank">Live Demo</a>` : ''}
                    ${project.source_url ? `<a href="${project.source_url}" class="btn btn-outline-primary btn-sm" target="_blank">Source Code</a>` : ''}
                </div>
            </div>
        </div>
    `;
    
    return card;
}

// Contact form enhancement
function enhanceContactForm() {
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            const submitBtn = this.querySelector('button[type="submit"]');
            
            // Show loading state
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';
            submitBtn.disabled = true;
            
            // Submit form (you can enhance this with AJAX if needed)
            setTimeout(() => {
                this.submit();
            }, 500);
        });
    }
}

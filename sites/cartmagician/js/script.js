// Smooth scroll for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
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

// Add scroll reveal animation
document.addEventListener('DOMContentLoaded', function() {
    const sections = document.querySelectorAll('section');
    
    const observerOptions = {
        root: null,
        threshold: 0.1,
        rootMargin: '0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
            }
        });
    }, observerOptions);

    sections.forEach(section => {
        section.style.opacity = '0';
        observer.observe(section);
    });
});

// Form submission handling for contact buttons
document.querySelectorAll('.btn').forEach(button => {
    button.addEventListener('click', function(e) {
        const action = this.textContent.trim();
        if (action === 'Start Free Trial' || action === 'Schedule a Demo' || action === 'Contact Sales') {
            e.preventDefault();
            // In a real implementation, this would open a modal or redirect to a form
            alert(`Thank you for your interest in ${action}! This feature will be implemented soon.`);
        }
    });
}); 
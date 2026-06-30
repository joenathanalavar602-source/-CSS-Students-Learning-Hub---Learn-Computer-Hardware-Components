// General utility functions for the CSS Learning Hub

// Console log for debugging
console.log('CSS Learning Hub loaded');

// Mobile menu toggle (if needed)
function toggleMobileMenu() {
    const navMenu = document.querySelector('.nav-menu');
    if (navMenu) {
        navMenu.classList.toggle('active');
    }
}

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});

// Add loading state to buttons
document.querySelectorAll('button, input[type="submit"]').forEach(button => {
    button.addEventListener('click', function() {
        if (this.id !== 'flip-btn' && this.id !== 'next-btn') {
            this.disabled = true;
            this.style.opacity = '0.6';
            setTimeout(() => {
                this.disabled = false;
                this.style.opacity = '1';
            }, 1000);
        }
    });
});

// Initialize any tooltips or help text
function initializeHelp() {
    const helpElements = document.querySelectorAll('[data-help]');
    helpElements.forEach(element => {
        element.title = element.getAttribute('data-help');
    });
}

// Check for empty form fields
function validateForm(form) {
    const inputs = form.querySelectorAll('input[required], textarea[required], select[required]');
    let isValid = true;
    
    inputs.forEach(input => {
        if (!input.value.trim()) {
            isValid = false;
            input.style.borderColor = 'red';
        } else {
            input.style.borderColor = '';
        }
    });
    
    return isValid;
}

// Local storage for user preferences
function savePreference(key, value) {
    localStorage.setItem(key, JSON.stringify(value));
}

function getPreference(key) {
    const value = localStorage.getItem(key);
    return value ? JSON.parse(value) : null;
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    initializeHelp();
    
    // Add any other initialization code here
    console.log('Page fully loaded and initialized');
});

// Add keyboard shortcuts (optional)
document.addEventListener('keydown', function(event) {
    // Press 'H' to go home
    if (event.key === 'h' || event.key === 'H') {
        window.location.href = '/';
    }
    
    // Press '?' to show help
    if (event.key === '?') {
        console.log('Help requested - show help modal');
    }
});
// Main JavaScript file for AI Interview Coach

document.addEventListener('DOMContentLoaded', function() {
    // Initialize message dismissal
    initializeMessages();
    
    // Initialize dropdown menus
    initializeDropdowns();
    
    // Initialize smooth scrolling for anchor links
    initializeSmoothScrolling();
    
    // Initialize form validation
    initializeFormValidation();
});

// Message dismissal functionality
function initializeMessages() {
    const messageCloseButtons = document.querySelectorAll('.message-close');
    
    messageCloseButtons.forEach(button => {
        button.addEventListener('click', function() {
            const message = this.closest('.message');
            if (message) {
                message.style.opacity = '0';
                setTimeout(() => {
                    message.remove();
                }, 300);
            }
        });
    });
    
    // Auto-hide success messages after 5 seconds
    const successMessages = document.querySelectorAll('.message-success');
    successMessages.forEach(message => {
        setTimeout(() => {
            if (message.parentNode) {
                message.style.opacity = '0';
                setTimeout(() => {
                    if (message.parentNode) {
                        message.remove();
                    }
                }, 300);
            }
        }, 5000);
    });
}

// Dropdown menu functionality
function initializeDropdowns() {
    const userMenus = document.querySelectorAll('.user-menu');
    
    userMenus.forEach(menu => {
        const dropdown = menu.querySelector('.dropdown-menu');
        if (dropdown) {
            // Close dropdown when clicking outside
            document.addEventListener('click', function(event) {
                if (!menu.contains(event.target)) {
                    dropdown.style.opacity = '0';
                    dropdown.style.visibility = 'hidden';
                    dropdown.style.transform = 'translateY(-10px)';
                }
            });
            
            // Toggle dropdown on click
            menu.addEventListener('click', function(event) {
                event.stopPropagation();
                const isVisible = dropdown.style.opacity === '1';
                
                if (isVisible) {
                    dropdown.style.opacity = '0';
                    dropdown.style.visibility = 'hidden';
                    dropdown.style.transform = 'translateY(-10px)';
                } else {
                    dropdown.style.opacity = '1';
                    dropdown.style.visibility = 'visible';
                    dropdown.style.transform = 'translateY(0)';
                }
            });
        }
    });
}

// Smooth scrolling for anchor links
function initializeSmoothScrolling() {
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    
    anchorLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Form validation
function initializeFormValidation() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.classList.add('error');
                    
                    // Remove error class after user starts typing
                    field.addEventListener('input', function() {
                        this.classList.remove('error');
                    });
                }
            });
            
            if (!isValid) {
                event.preventDefault();
                showFormError('Please fill in all required fields.');
            }
        });
    });
}

// Show form error message
function showFormError(message) {
    const existingError = document.querySelector('.form-error-message');
    if (existingError) {
        existingError.remove();
    }
    
    const errorDiv = document.createElement('div');
    errorDiv.className = 'form-error-message error-message';
    errorDiv.textContent = message;
    
    const form = document.querySelector('form');
    if (form) {
        form.insertBefore(errorDiv, form.firstChild);
    }
}

// Progress bar animation
function animateProgressBars() {
    const progressBars = document.querySelectorAll('.progress-fill');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const progressBar = entry.target;
                const width = progressBar.style.width;
                progressBar.style.width = '0%';
                
                setTimeout(() => {
                    progressBar.style.width = width;
                }, 100);
            }
        });
    });
    
    progressBars.forEach(bar => observer.observe(bar));
}

// Initialize progress bar animations when dashboard is loaded
if (document.querySelector('.progress-fill')) {
    animateProgressBars();
}

// Add loading states to buttons
function initializeButtonLoading() {
    const submitButtons = document.querySelectorAll('button[type="submit"]');
    
    submitButtons.forEach(button => {
        button.addEventListener('click', function() {
            if (this.form && this.form.checkValidity()) {
                this.disabled = true;
                this.innerHTML = '<span class="loading-spinner"></span> Processing...';
                
                // Re-enable button after form submission (in case of errors)
                setTimeout(() => {
                    this.disabled = false;
                    this.innerHTML = this.getAttribute('data-original-text') || 'Submit';
                }, 5000);
            }
        });
    });
}

// Initialize button loading states
initializeButtonLoading();

// Add CSS for loading spinner
const style = document.createElement('style');
style.textContent = `
    .loading-spinner {
        display: inline-block;
        width: 16px;
        height: 16px;
        border: 2px solid #ffffff;
        border-radius: 50%;
        border-top-color: transparent;
        animation: spin 1s ease-in-out infinite;
        margin-right: 8px;
    }
    
    @keyframes spin {
        to { transform: rotate(360deg); }
    }
    
    .form-error-message {
        margin-bottom: 1rem;
    }
    
    .error {
        border-color: #dc2626 !important;
        box-shadow: 0 0 0 3px rgba(220, 38, 38, 0.1) !important;
    }
`;
document.head.appendChild(style);

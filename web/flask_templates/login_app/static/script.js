// Wait for DOM to load
document.addEventListener('DOMContentLoaded', function() {
    // Auto-dismiss flash messages after 5 seconds
    const flashes = document.querySelectorAll('.flash');
    if (flashes.length > 0) {
        setTimeout(function() {
            flashes.forEach(flash => {
                flash.style.opacity = '0';
                setTimeout(() => {
                    flash.style.display = 'none';
                }, 500);
            });
        }, 5000);
    }
    
    // Password strength indicator for registration
    const passwordInput = document.querySelector('input[type="password"]');
    if (passwordInput && window.location.pathname.includes('register')) {
        passwordInput.addEventListener('input', function() {
            const value = this.value;
            let strength = 0;
            
            if (value.length >= 8) strength++;
            if (/[A-Z]/.test(value)) strength++;
            if (/[0-9]/.test(value)) strength++;
            if (/[^A-Za-z0-9]/.test(value)) strength++;
            
            const strengthText = ['Weak', 'Fair', 'Good', 'Strong'][strength];
            
            // Create or update strength indicator
            let indicator = document.querySelector('.password-strength');
            if (!indicator) {
                indicator = document.createElement('div');
                indicator.className = 'password-strength';
                this.parentNode.appendChild(indicator);
            }
            
            indicator.textContent = `Password strength: ${strengthText}`;
            indicator.className = `password-strength strength-${strength}`;
        });
    }
});
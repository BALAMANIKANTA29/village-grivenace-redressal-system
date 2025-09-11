// Custom JavaScript for VGRS

// Confirm complaint submission
document.addEventListener('DOMContentLoaded', function() {
    const complaintForm = document.querySelector('form[action*="submit_complaint"]');
    if (complaintForm) {
        complaintForm.addEventListener('submit', function(e) {
            const confirmed = confirm('Are you sure you want to submit this complaint?');
            if (!confirmed) {
                e.preventDefault();
            }
        });
    }

    // Auto-resize textarea
    const textareas = document.querySelectorAll('textarea');
    textareas.forEach(textarea => {
        textarea.addEventListener('input', function() {
            this.style.height = 'auto';
            this.style.height = this.scrollHeight + 'px';
        });
    });

    // Status badge animations
    const statusBadges = document.querySelectorAll('.badge');
    statusBadges.forEach(badge => {
        if (badge.textContent.trim() === 'Resolved') {
            badge.classList.add('animate__animated', 'animate__bounceIn');
        }
    });
});

// Function to show loading spinner
function showLoading(button) {
    button.disabled = true;
    button.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Loading...';
}

// Function to hide loading spinner
function hideLoading(button, originalText) {
    button.disabled = false;
    button.innerHTML = originalText;
}

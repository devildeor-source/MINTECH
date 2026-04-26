<script>
    // 1. Load data when page opens
    window.onload = function() {
        renderDoctors();
    };

    // 2. The Plus button triggers a prompt
    document.getElementById('add-btn-trigger').addEventListener('click', function() {
        const name = prompt("Enter Doctor's Name:");
        const degree = prompt("Enter Degree (e.g., MS):");
        
        if (name && degree) {
            // Save to browser's Local Storage
            const doctor = { name, degree };
            let doctors = JSON.parse(localStorage.getItem('myDoctors') || '[]');
            doctors.push(doctor);
            localStorage.setItem('myDoctors', JSON.stringify(doctors));
            renderDoctors();
        }
    });

    // 3. Display the doctors
    function renderDoctors() {
        const list = document.getElementById('doctor-list');
        list.innerHTML = '';
        const doctors = JSON.parse(localStorage.getItem('myDoctors') || '[]');
        
        doctors.forEach(doc => {
            list.innerHTML += `
                <div class="doctor-card">
                    <div class="profile-img-container">👤</div>
                    <div class="doctor-details">
                        <h3>${doc.name}</h3>
                        <p>${doc.degree}</p>
                    </div>
                </div>
            `;
        });
    }
</script>

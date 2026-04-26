<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mintech Pharma</title>
    <style>
        body { background-color: #121212; color: white; font-family: sans-serif; padding: 20px; }
        header { border-bottom: 1px solid #333; padding-bottom: 10px; margin-bottom: 20px; }
        .brand { font-size: 24px; font-weight: bold; color: #007bff; display: flex; align-items: center; }
        .plus-red { color: #ff4444; margin-right: 10px; font-weight: 900; }
        .section-title { color: #888; font-size: 14px; margin: 15px 0; }
        .doctor-card { background: #1e1e1e; padding: 15px; border-radius: 10px; display: flex; align-items: center; margin-bottom: 10px; }
        .avatar { width: 50px; height: 50px; background: #333; border-radius: 50%; margin-right: 15px; display: flex; align-items: center; justify-content: center; }
        .fab { position: fixed; bottom: 30px; right: 30px; width: 60px; height: 60px; background: #007bff; border-radius: 50%; font-size: 30px; display: flex; align-items: center; justify-content: center; color: white; border: none; cursor: pointer; }
    </style>
</head>
<body>
    <header>
        <div class="brand">
            <span class="plus-red">+</span> MINTECH PHARMA
        </div>
    </header>
    <div class="section-title">DOCTORS</div>
    <div id="doctor-list"></div>
    <button class="fab" onclick="addDoctor()">+</button>
    <script>
        // Load doctors when page loads
        document.addEventListener('DOMContentLoaded', renderDoctors);
        function addDoctor() {
            const name = prompt("Enter Doctor's Name:");
            const degree = prompt("Enter Degree (e.g., MS, MBBS):");    
            if (name && degree) {
                const doctor = { name, degree };
                let doctors = JSON.parse(localStorage.getItem('mintech_doctors') || '[]');
                doctors.push(doctor);
                localStorage.setItem('mintech_doctors', JSON.stringify(doctors));
                renderDoctors();
            }
        }
        function renderDoctors() {
            const list = document.getElementById('doctor-list');
            const doctors = JSON.parse(localStorage.getItem('mintech_doctors') || '[]');
            list.innerHTML = doctors.map(d => `
                <div class="doctor-card">
                    <div class="avatar">👤</div>
                    <div>
                        <div style="font-weight:bold">${d.name}</div>
                        <div style="color:#aaa; font-size:12px">${d.degree}</div>
                    </div>
                </div>
            `).join('');
        }
    </script>
</body>
</html>

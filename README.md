<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MINTECH PHARMA</title>
    <style>
        body { background-color: #121212; color: #fff; font-family: sans-serif; padding: 20px; }
        header { display: flex; align-items: center; border-bottom: 1px solid #333; padding-bottom: 15px; margin-bottom: 20px; }
        .logo { font-size: 22px; font-weight: bold; color: #007bff; display: flex; align-items: center; }
        .plus-red { color: #ff4444; font-size: 30px; margin-right: 10px; font-weight: 900; }
        .section-header { color: #888; font-size: 14px; text-transform: uppercase; margin-bottom: 15px; }
        .doctor-card { background: #1e1e1e; padding: 15px; border-radius: 12px; display: flex; align-items: center; margin-bottom: 12px; border: 1px solid #333; }
        .img-placeholder { width: 60px; height: 60px; background: #333; border-radius: 50%; margin-right: 15px; }
        .fab { position: fixed; bottom: 30px; right: 30px; width: 65px; height: 65px; background: #007bff; border-radius: 50%; color: white; font-size: 35px; border: none; box-shadow: 0 4px 10px rgba(0,0,0,0.5); }
    </style>
</head>
<body>
    <header>
        <div class="logo"><span class="plus-red">+</span> MINTECH PHARMA</div>
    </header>
    <div class="section-header">DOCTORS</div>
    <div id="doctor-list"></div>
    <button class="fab" onclick="addNewDoctor()">+</button>
    <script>
        // Load data from phone memory when page opens
        window.onload = loadDoctors;
        function addNewDoctor() {
            // Get user input directly
            const name = prompt("Enter Doctor's Name:");
            const degree = prompt("Enter Degree:");
            if (name && degree) {
                const doctor = { name, degree, id: Date.now() };
                let doctors = JSON.parse(localStorage.getItem('my_doctors') || '[]');
                doctors.push(doctor);
                localStorage.setItem('my_doctors', JSON.stringify(doctors));
                loadDoctors();
            }
        }
        function loadDoctors() {
            const container = document.getElementById('doctor-list');
            const doctors = JSON.parse(localStorage.getItem('my_doctors') || '[]');
            container.innerHTML = doctors.map(d => `
                <div class="doctor-card">
                    <div class="img-placeholder"></div>
                    <div>
                        <div style="font-weight:bold; font-size:18px">${d.name}</div>
                        <div style="color:#aaa">${d.degree}</div>
                    </div>
                </div>
            `).join('');
        }
    </script>
</body>
</html>

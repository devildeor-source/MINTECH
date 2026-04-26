<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MINTECH PHARMA</title>
    <script src="https://upload-widget.cloudinary.com/global/all.js" type="text/javascript"></script>
    <style>
        body { background-color: #121212; color: #fff; font-family: sans-serif; padding: 20px; }
        header { display: flex; align-items: center; border-bottom: 1px solid #333; padding-bottom: 15px; margin-bottom: 20px; }
        .logo { font-size: 22px; font-weight: bold; color: #007bff; display: flex; align-items: center; }
        .plus-red { color: #ff4444; font-size: 30px; margin-right: 10px; font-weight: 900; }
        .section-header { color: #888; font-size: 14px; text-transform: uppercase; margin-bottom: 15px; }
        .doctor-card { background: #1e1e1e; padding: 15px; border-radius: 12px; display: flex; align-items: center; margin-bottom: 12px; border: 1px solid #333; }
        /* 2. Styling for the Profile Image */
        .doctor-img { width: 70px; height: 70px; border-radius: 50%; object-fit: cover; margin-right: 20px; border: 2px solid #333; }
        .placeholder-avatar { width: 70px; height: 70px; background: #333; border-radius: 50%; margin-right: 20px; display: flex; justify-content: center; align-items: center; font-size: 24px; color: #666; }
        .fab { position: fixed; bottom: 30px; right: 30px; width: 65px; height: 65px; background: #007bff; border-radius: 50%; color: white; font-size: 35px; border: none; box-shadow: 0 4px 10px rgba(0,0,0,0.5); cursor: pointer; }
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
        // 3. Load data on page open
        window.onload = loadDoctors;
        // 4. Initialize the Cloudinary Widget (Handles the gallery upload)
        var myWidget = cloudinary.createUploadWidget({
            cloudName: 'demo', // REPLACE THIS with your Cloud Name
            uploadPreset: 'default' // REPLACE THIS with your unsigned preset
        }, (error, result) => { 
            if (!error && result && result.event === "success") { 
                // Image successfully uploaded to the cloud!
                const imageUrl = result.info.secure_url;
                saveDoctor(imageUrl);
            }
        });
        // Current temporary data holder
        let tempDoctor = { name: '', degree: '' };
        function addNewDoctor() {
            const name = prompt("Enter Doctor's Name:");
            const degree = prompt("Enter Degree (e.g., MBBS, MS):"); 
            if (name && degree) {
                tempDoctor.name = name;
                tempDoctor.degree = degree;
                // NOW open the widget so they can pick the picture.
                myWidget.open();
            }
        }
        function saveDoctor(imageUrl) {
            // Take the temp info + the newly created image URL
            const finalDoctor = { 
                name: tempDoctor.name, 
                degree: tempDoctor.degree, 
                photo: imageUrl,
                id: Date.now() 
            };
            // Save the complete entry to the phone's memory
            let doctors = JSON.parse(localStorage.getItem('my_doctors_complete') || '[]');
            doctors.push(finalDoctor);
            localStorage.setItem('my_doctors_complete', JSON.stringify(doctors));
            // Clear temp holder and refresh the list
            tempDoctor = { name: '', degree: '' };
            loadDoctors();
        }
        function loadDoctors() {
            const container = document.getElementById('doctor-list');
            const doctors = JSON.parse(localStorage.getItem('my_doctors_complete') || '[]');   
            if (doctors.length === 0) {
                container.innerHTML = `<p style="color:#666; font-style:italic">No doctors listed yet.</p>`;
                return;
            }
            container.innerHTML = doctors.map(d => `
                <div class="doctor-card">
                    ${d.photo ? `<img src="${d.photo}" class="doctor-img" alt="${d.name}">` : `<div class="placeholder-avatar">👤</div>`}
                    <div>
                        <div style="font-weight:bold; font-size:18px">${d.name}</div>
                        <div style="color:#aaa; font-size:14px">${d.degree}</div>
                    </div>
                </div>
            `).join('');
        }
    </script>
</body>
</html>

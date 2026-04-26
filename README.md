<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mintech Pharma - Dispensary</title>
    <style>
        /* Modern Matte Black Theme (Simplified) */
        body { background-color: #121212; color: #ffffff; font-family: 'Segoe UI', sans-serif; margin: 0; padding: 20px; }
        h1, h2, h3 { color: #ffffff; }
        /* HEADER & BRANDING */
        header { 
            display: flex; 
            align-items: center; 
            justify-content: space-between; 
            padding: 20px; 
            border-bottom: 1px solid rgba(255, 255, 255, 0.2); 
            margin-bottom: 25px; 
        }
        .brand-logo { 
            font-size: 24px; 
            font-weight: bold; 
            display: flex; 
            align-items: center; 
            color: #007bff; /* Keeps the blue 'Mintech' feel */
        } 
        /* The Red Medical Plus */
        .medical-cross { 
            font-size: 30px; 
            color: #ee4444; /* Medical Red */
            margin-right: 12px; 
            font-weight: 900;
        }
        /* Section Headings */
        .section-header { 
            font-size: 18px; 
            text-transform: uppercase; 
            color: rgba(255, 255, 255, 0.7); 
            letter-spacing: 1.5px; 
            margin: 20px 0 15px 5px; 
        }
        /* Doctor Card Styling */
        #doctor-list { margin-top: 15px; }
        .doctor-card { 
            background: rgba(30, 30, 30, 0.8); 
            border-radius: 20px; 
            display: flex; 
            align-items: center; 
            padding: 15px; 
            margin-bottom: 15px; 
            border: 1px solid rgba(255, 255, 255, 0.1); 
        }   
        .profile-img-container { 
            width: 70px; height: 70px; 
            border-radius: 50%; 
            background: #333; 
            overflow: hidden; 
            margin-right: 20px; 
            flex-shrink: 0;
            display: flex; justify-content: center; align-items: center;
        }      
        .profile-img-container img { width: 100%; height: 100%; object-fit: cover; }   
        .doctor-details { flex-grow: 1; }
        .doctor-details h3 { margin: 0 0 5px 0; font-size: 18px; }
        .doctor-details p { margin: 0; color: #aaa; font-size: 14px; }
        /* The blue floating action button */
        .add-btn { 
            position: fixed; bottom: 30px; right: 30px; 
            width: 60px; height: 60px; 
            background: #007bff; border-radius: 50%; 
            display: flex; align-items: center; justify-content: center; 
            font-size: 30px; color: white; 
            box-shadow: 0 4px 15px rgba(0, 123, 255, 0.4); 
            cursor: pointer;
            z-index: 100;
        }
        /* This is crucial: an invisible file input */
        #real-file-input { display: none; }
    </style>
</head>
<body>
    <header>
        <div class="brand-logo">
            <span class="medical-cross">+</span>
            MINTECH PHARMA
        </div>
    </header>
    <div class="section-header">DOCTORS</div>
    <div id="doctor-list">
        {% for doctor in doctors %}
        <div class="doctor-card">
            <div class="profile-img-container">
                <img src="{{ doctor.photo }}" alt="Doctor Profile">
            </div>
            <div class="doctor-details">
                <h3>{{ doctor.name }}</h3>
                <p>{{ doctor.degree }}</p>
            </div>
        </div>
        {% else %}
        <p style="text-align: center; color: #666; font-style: italic;">No doctors listed yet. Tap + to add one.</p>
        {% endfor %}
    </div>
    <div class="add-btn" id="add-btn-trigger">+</div>
    <form action="/add_doctor" method="POST" enctype="multipart/form-data" id="upload-form">
        <input type="file" name="doctorPhoto" id="real-file-input" accept="image/*" required>
        </form>
    <script>
        const fab = document.getElementById('add-btn-trigger');
        const fileInput = document.getElementById('real-file-input');
        const form = document.getElementById('upload-form');
        // When the blue + is tapped, automatically open the native gallery
        fab.addEventListener('click', function() {
            fileInput.click(); // Standard HTML trick to open mobile gallery
        });
        // Optional: When the user successfully picks an image, you can submit immediately
        fileInput.addEventListener('change', function() {
            if (fileInput.value) {
                // Here, in a real application, you would now prompt 
                // for the Name/Degree using a simple Javascript prompt 
                // BEFORE submitting. We will keep it simple for now.
                form.submit();
            }
        });
    </script>
</body>
</html>

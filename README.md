<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mintech Pharma Portal</title>
    <style>
        /* Modern Matte Black Theme */
        body {
            background-color: #121212;
            color: #ffffff;
            font-family: 'Segoe UI', sans-serif;
            margin: 0;
            padding: 20px;
        }
        /* Glassmorphism Header */
        header {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            border: 1px solid rgba(255, 255, 255, 0.1);
            margin-bottom: 20px;
        }
        /* Doctor Card Styling */
        .doctor-card {
            background: rgba(30, 30, 30, 0.6);
            backdrop-filter: blur(5px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 15px;
            border-radius: 20px;
            display: flex;
            align-items: center;
            margin-bottom: 15px;
            transition: transform 0.3s ease;
        }
        .doctor-card:hover { transform: scale(1.02); }
        .profile-img {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background: #333;
            margin-right: 15px;
        }
        /* Bottom Floating Action Button */
        .add-btn {
            position: fixed;
            bottom: 30px;
            right: 30px;
            width: 60px;
            height: 60px;
            background: #007bff;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 30px;
            color: white;
            box-shadow: 0 4px 15px rgba(0, 123, 255, 0.4);
        }
    </style>
</head>
<body>
    <header>
        <h1>MINTECH PHARMA</h1>
    </header>
    <div id="doctor-list">
        <div class="doctor-card">
            <div class="profile-img"></div>
            <div>
                <h3>Dr. Example, MS</h3>
                <p>Cardiologist</p>
            </div>
        </div>
    </div>
    <div class="add-btn">+</div>
</body>
</html>


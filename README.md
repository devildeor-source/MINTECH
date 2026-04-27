<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MINTECH PHARMA</title>
    <style>
        /* Deep green background with light aura */
        body { 
            background-color: #051a05; 
            background-image: 
                radial-gradient(at 10% 10%, rgba(0, 255, 127, 0.2) 0px, transparent 50%),
                radial-gradient(at 90% 20%, rgba(34, 139, 34, 0.15) 0px, transparent 40%),
                radial-gradient(at 50% 90%, rgba(0, 250, 154, 0.1) 0px, transparent 35%);
            color: #fff; 
            font-family: sans-serif; 
            padding: 20px; 
            margin: 0; 
            min-height: 100vh;
        }
        header { display: flex; align-items: center; border-bottom: 1px solid #333; padding-bottom: 15px; margin-bottom: 20px; }
        .logo { font-size: 32px; font-weight: 900; color: #ffffff; display: flex; align-items: center; }
        .plus-red { color: #ff4444; font-size: 30px; margin-right: 10px; font-weight: 900;   
        .doctor-card { background: #1e1e1e; padding: 15px; border-radius: 12px; margin-bottom: 12px; border: 1px solid #333; display: flex; justify-content: space-between; align-items: center; cursor: pointer; }
        .img-preview { width: 50px; height: 50px; border-radius: 50%; object-fit: cover; margin-right: 15px; }
        .fab { position: fixed; bottom: 30px; right: 30px; width: 65px; height: 65px; background: #007bff; border-radius: 50%; color: white; font-size: 30px; border: none; box-shadow: 0 4px 10px rgba(0,0,0,0.5); cursor: pointer; }
        .modal { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.95); padding: 20px; box-sizing: border-box; }
        .modal-content { background: #222; padding: 20px; border-radius: 12px; margin-top: 50px; }
        input { width: 100%; padding: 12px; margin: 8px 0; border-radius: 8px; border: none; box-sizing: border-box; }
        .btn { padding: 12px; background: #007bff; color: white; border: none; border-radius: 8px; width: 100%; margin-top: 5px; cursor: pointer; }
        .del-app-btn { background: #ff4444; color: white; border: none; padding: 4px 8px; border-radius: 4px; font-size: 12px; cursor: pointer; }
    </style>
</head>
<body>
    <header>
        <div class="logo">
            <span class="plus-red">+</span> MINTECH PHARMA
        </div>
    </header>
    <div id="doctor-list"></div>
    <input type="file" id="fileInput" style="display:none" accept="image/*" onchange="addDoc(this)">
    <button class="fab" onclick="document.getElementById('fileInput').click()">+</button>
    <div id="modal" class="modal">
        <div class="modal-content">
            <h3 id="modal-title"></h3>
            <input type="text" id="pName" placeholder="Patient Name">
            <input type="text" id="pPhone" placeholder="Phone Number">
            <button class="btn" onclick="saveAppointment()">Add Appointment</button>
            <div id="doc-specific-apps" style="margin-top:20px; border-top: 1px solid #444; padding-top: 10px;"></div>
            <button class="btn" style="background:#444" onclick="document.getElementById('modal').style.display='none'">Close</button>
        </div>
    </div>
    <script>
        let currentDocId = null;
        function addDoc(input) {
            if (input.files[0]) {
                let name = prompt("Doctor Name:");
                let degree = prompt("Degree:");
                let reader = new FileReader();
                reader.onload = (e) => {
                    let docs = JSON.parse(localStorage.getItem('my_doctors') || '[]');
                    docs.push({ id: Date.now(), name, degree, photo: e.target.result });
                    localStorage.setItem('my_doctors', JSON.stringify(docs));
                    location.reload();
                };
                reader.readAsDataURL(input.files[0]);
            }
        }
        function openModal(id, name) {
            currentDocId = id;
            document.getElementById('modal-title').innerText = "Appointments: " + name;
            let apps = JSON.parse(localStorage.getItem('apps_' + id) || '[]');
        document.getElementById('doc-specific-apps').innerHTML = apps.map((a, index) => `
                <div style="background:#333; padding:8px; border-radius:5px; margin-bottom:5px; display:flex; justify-content:space-between; align-items:center;">
                    <span>${a.name} - ${a.phone}</span>
                    <button class="del-app-btn" onclick="deleteAppointment(${index})">Delete</button>
                </div>
            `).join('');
            document.getElementById('modal').style.display = 'block';
        }
        function saveAppointment() {
            let name = document.getElementById('pName').value;
            let phone = document.getElementById('pPhone').value;
            if(name && phone) {
                let apps = JSON.parse(localStorage.getItem('apps_' + currentDocId) || '[]');
                apps.push({ name, phone });
                localStorage.setItem('apps_' + currentDocId, JSON.stringify(apps));
                document.getElementById('pName').value = '';
                document.getElementById('pPhone').value = '';
                openModal(currentDocId, document.getElementById('modal-title').innerText.replace("Appointments: ", ""));
            }
        }
        function deleteAppointment(index) {
            let apps = JSON.parse(localStorage.getItem('apps_' + currentDocId) || '[]');
            apps.splice(index, 1);
            localStorage.setItem('apps_' + currentDocId, JSON.stringify(apps));
            openModal(currentDocId, document.getElementById('modal-title').innerText.replace("Appointments: ", ""));
        }
        function deleteDoc(id, e) {
            e.stopPropagation();
            if(confirm("Delete doctor?")) {
                let docs = JSON.parse(localStorage.getItem('my_doctors') || '[]');
                localStorage.setItem('my_doctors', JSON.stringify(docs.filter(d => d.id !== id)));
                localStorage.removeItem('apps_' + id);
                location.reload();
            }
        }
        let docs = JSON.parse(localStorage.getItem('my_doctors') || '[]');
        document.getElementById('doctor-list').innerHTML = docs.map(d => `
            <div class="doctor-card" onclick="openModal(${d.id}, '${d.name}')">
                <div style="display:flex; align-items:center;">
                    <img src="${d.photo}" class="img-preview">
                    <div><b>${d.name}</b><br><small style="color:#aaa">${d.degree}</small></div>
                </div>
                <button class="btn" style="width:auto; background:#ff4444" onclick="deleteDoc(${d.id}, event)">Delete</button>
            </div>
        `).join('');
    </script>
</body>
</html>

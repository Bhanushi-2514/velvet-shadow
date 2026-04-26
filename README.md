# 🖤 Velvet Shadow

> Where love is intense and silence keeps secrets.

Velvet Shadow is a cinematic storytelling web experience built with Django.  
It is not just a website — it is an atmosphere.

Users explore emotional romance tropes, read poetic story pages, write reflections, and enter the Shadow Chamber where their thoughts are quietly observed.

---

## 🌍 Live Experience

Velvet Shadow is now live.

Enter the atmosphere:

🔗 https://velvet-shadow.onrender.com

Some stories stay.  
Some scars don’t fade.



---

## 📸 Preview

### 🏠 Home Page
![Home](assets/home.png)

### 📖 Story Page
![Story](assets/story.png)

### 🌑 Shadow Chamber
![Chamber](assets/chamber.png)

---

## ✨ Features

- 🌌 Cinematic dark aesthetic design  
- 📚 Four interactive romance tropes  
- ✍ Reflection submission system  
- 🧠 Chamber observation logic  
- 🗳 Mystic poll interaction  
- 🎵 Soft audio experience after poll submission  
- 🌑 Emotional closing section  

---

🎧 Sound Experience

Velvet Shadow uses sound carefully — not to distract, but to deepen the feeling.

🔇 Default silent mode (no autoplay)
🔊 User-controlled sound toggle
📖 Soft page-flip feedback on interaction
🎹 Low-volume ambient piano background
🌑 Context-based sound (Shadow Chamber only)

Sound is not always heard… sometimes it is simply felt.

---

## 🛠 Tech Stack

- Python  
- Django  
- HTML  
- CSS  
- JavaScript  
- SQLite  

---

```
📂 Project Structure
VelvetShadow/
│
├── VelvetShadow/              # Project settings (settings.py, urls.py)
│
├── shadowverse/               # Main application
│   ├── migrations/
│   ├── models.py              # Reflection & chamber logic
│   ├── views.py               # Page rendering & interaction logic
│   ├── urls.py
│
│   ├── templates/
│   │   └── shadowverse/
│   │       ├── base.html
│   │       ├── index.html
│   │       ├── story.html
│   │       └── shadow_chamber.html
│
│   ├── static/
│   │   └── shadowverse/
│   │       ├── css/
│   │       │   └── style.css
│   │       ├── images/
│   │       │   └── background.jpg
│   │       └── audio/
│   │           ├── piano_bg_music.mp3
│   │           ├── page_flip.wav
│   │           └── velvet_end.mp3
│
├── assets/                   # GitHub preview screenshots
│   ├── home.png
│   ├── story.png
│   └── chamber.png
│
├── staticfiles/              # Collected static files (production)
├── manage.py
└── README.md
'''
---
⚙️ Run Locally
You can run Velvet Shadow easily on your system.
---

'''
1️⃣ Clone the repository
git clone https://github.com/your-username/velvet-shadow.git
cd velvet-shadow
'''

'''
2️⃣ Create virtual environment (optional)
python -m venv venv
venv\Scripts\activate
'''

'''
3️⃣ Install dependencies
pip install django whitenoise

4️⃣ Apply migrations
python manage.py migrate

5️⃣ Collect static files (important)
python manage.py collectstatic

Type yes when prompted.
'''

'''
6️⃣ Run the server
python manage.py runserver
'''

---
💸 Usage
✅ Completely free to use
💻 Works on any laptop or PC
🔧 Fully customizable

No paid tools or services are required.
---

---

📱 Future Improvements
Mobile & tablet responsiveness
Persistent sound preference (remember user choice)
Enhanced audio transitions
More immersive UI interactions
---

---
💭 Final Note

Velvet Shadow is not built to be fast.
It is built to be felt.

Some users will scroll.
Some will pause.
And a few… will stay.
---


# 🦙 ExplainLLama Web App

Welcome to **ExplainLLama**, an AI-powered web application designed for Java bug fixing and explanation generation. This tool utilizes a **dual decoder transformer model** trained to analyze Java code bugs and generate detailed explanations for debugging assistance. The project provides both a backend API and a user-friendly frontend interface for seamless interactions.

🧑‍🎓 **This project is developed as part of our Final Year Research Project.** 🎓

<img src="https://filedn.eu/lVNP1DcGQUE5OPMMHbPaQeb/ExplainLlama_Web_App/ExplainLLama_Web_UI.png" width="700">

---

## 🌟 Features
✅ **Java Bug Fixing Assistance** - Identify and fix Java code errors efficiently.  
✅ **AI-Powered Explanation Generation** - Get detailed insights into why a bug occurs.  
✅ **Web-Based Interface** - Easy-to-use UI for debugging and explanations.  
✅ **Robust Backend API** - Efficient request handling and model interaction.  
✅ **Secure & Scalable** - Built with best practices for security and performance.

---

## 📦 Installation

### 📌 Prerequisites
Ensure you have the following installed before proceeding:
- 🐍 **Python** (>=3.8)
- 📦 **pip** (for managing dependencies)
- 🔹 **Virtual environment** (optional but recommended)
- 🖥 **Node.js** and **npm** (for frontend setup)

### 🔧 Setup
1. **Clone the Repository**
   ```sh
   git clone https://github.com/your-repo/ExplainLLama_Web_App.git
   cd ExplainLLama_Web_App
   ```

2. **Create a Virtual Environment (Recommended)**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Backend Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

---

## ▶️ Running the Application

### ⚙️ Backend Setup
1. **Navigate to the Backend Directory**
   ```sh
   cd backend
   ```
2. **Apply Migrations** (Ensuring the database is up-to-date)
   ```sh
   python manage.py migrate
   ```
3. **Start the Development Server**
   ```sh
   python manage.py runserver
   ```

### 🎨 Frontend Setup
1. **Navigate to the Frontend Directory**
   ```sh
   cd frontend
   ```
2. **Install Dependencies**
   ```sh
   npm install
   ```
3. **Start the Frontend Server**
   ```sh
   npm start
   ```

This will start the frontend development server, and you can access the application at `http://localhost:3000`.

---

## 🔑 Environment Variables
Copy `.env_sample` to `.env` and update necessary configurations:
```sh
cp .env_sample .env
```

---

## 🤝 Contributing
We welcome contributions! 🎉 If you'd like to improve ExplainLLama, follow these steps:
1. Fork the repository 🍴
2. Create a new branch 🌿
3. Make your changes ✍️
4. Submit a pull request 📩


## 👥 Team Members
- 🧑‍💻 **Suwan Sankaja** - [GitHub Profile](https://github.com/SuwanSankaja)  
- 🧑‍💻 **Gimhan Sandeeptha** - [GitHub Profile](https://github.com/gimhansandeeptha)  
- 🧑‍💻 **Ruwan Ranasinghe** - [GitHub Profile](https://github.com/RuwanUdayanga)  

🚀 **GitHub Organization:** [ExplainaCode Organization](https://github.com/ExplainaCode)

---

## 📧 Contact
📩 **For issues or inquiries, reach out at:** dev@suwansankaja.com`  
🐙 **GitHub Issues:** [Open an issue](https://github.com/SuwanSankaja/ExplainLLama_Web_App/issues)

💡 _Thank you for using ExplainLLama! Happy coding!_ 🎉


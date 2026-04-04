<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,12,24&height=200&section=header&text=🍔%20FoodDelivery&fontSize=52&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Full-Stack%20Food%20Ordering%20Platform%20|%20React%20+%20Node.js%20+%20MongoDB&descAlignY=60&descAlign=50" width="100%"/>

<div align="center">

[![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://reactjs.org)
[![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)](https://nodejs.org)
[![Express](https://img.shields.io/badge/Express.js-000000?style=for-the-badge&logo=express&logoColor=white)](https://expressjs.com)
[![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://mongodb.com)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)

</div>

---

## 📌 Project Overview

**FoodDelivery** is a complete full-stack food ordering web application with three integrated modules — a **customer-facing frontend**, a **RESTful backend API**, and a dedicated **admin dashboard**. Users can browse menus, place orders, and track them in real time, while admins manage restaurants, items, and orders from a separate panel.

> 🎯 Built as a production-grade MERN-stack application with clean separation of concerns across client, server, and admin layers.

---

## 🏗️ Architecture

```
Customer Frontend (React) ──► REST API (Node.js + Express) ──► MongoDB
         ▲                             │
         │                             ▼
   Admin Panel (React) ◄──────── Auth Middleware
```

---

## 🔄 Application Workflow

```
User Signup/Login → Browse Menu → Add to Cart → Place Order → Payment → Order Tracking → Admin Updates Status
```

### 1️⃣ Customer Frontend (`/frontend`)
- Browse restaurant menus and food items
- Add/remove items to cart with quantity control
- User authentication (Register / Login)
- Place orders and view order history
- Real-time order status tracking

### 2️⃣ Backend API (`/backend`)
- RESTful API built with Express.js
- JWT-based user authentication & authorization
- MongoDB with Mongoose ODM for data persistence
- Handles orders, users, food items, and payments
- Secure middleware for protected routes

### 3️⃣ Admin Dashboard (`/admin`)
- Separate React application for management
- Add / update / delete food items and categories
- View and manage all incoming orders
- Update order delivery status in real time
- Inventory and menu management

---

## 📦 Features

| Feature | Frontend | Backend | Admin |
|:---|:---:|:---:|:---:|
| User Authentication (JWT) | ✅ | ✅ | ✅ |
| Menu Browsing & Search | ✅ | ✅ | — |
| Cart Management | ✅ | ✅ | — |
| Order Placement | ✅ | ✅ | — |
| Order Status Tracking | ✅ | ✅ | ✅ |
| Food Item CRUD | — | ✅ | ✅ |
| Admin Order Management | — | ✅ | ✅ |
| Responsive Design | ✅ | — | ✅ |

---

## 🗂️ Repository Structure

```
FoodDelivery/
│
├── frontend/                  # Customer-facing React app
│   ├── src/
│   │   ├── components/        # Reusable UI components
│   │   ├── pages/             # Route-level pages (Home, Cart, Orders)
│   │   ├── context/           # React Context for global state
│   │   └── assets/            # Images and static files
│   └── package.json
│
├── backend/                   # Node.js + Express REST API
│   ├── controllers/           # Route handler logic
│   ├── models/                # Mongoose schemas (User, Food, Order)
│   ├── routes/                # API route definitions
│   ├── middleware/             # Auth middleware (JWT)
│   └── server.js              # Entry point
│
├── admin/                     # Admin panel React app
│   ├── src/
│   │   ├── components/        # Admin UI components
│   │   ├── pages/             # Add Items, List Items, Orders
│   │   └── assets/
│   └── package.json
│
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites
- Node.js ≥ 18.x
- MongoDB (local or Atlas URI)
- npm or yarn

### 1. Clone the repo
```bash
git clone https://github.com/ronakrajput8882/FoodDelivery.git
cd FoodDelivery
```

### 2. Setup Backend
```bash
cd backend
npm install
# Create .env file
echo "MONGODB_URI=your_mongodb_uri" >> .env
echo "JWT_SECRET=your_jwt_secret" >> .env
npm start
```

### 3. Setup Frontend
```bash
cd ../frontend
npm install
npm run dev
```

### 4. Setup Admin Panel
```bash
cd ../admin
npm install
npm run dev
```

> **Default ports:** Backend → `5000` | Frontend → `5173` | Admin → `5174`

---

## 🔍 Key Highlights

- 🔐 **JWT Authentication** — Secure token-based auth across frontend and admin
- 🛒 **Context API** — Global cart and user state management without Redux overhead
- 📱 **Responsive UI** — Mobile-first design with CSS modules
- 🗄️ **MongoDB Atlas ready** — Cloud database connection via environment variable
- 🔄 **Real-time order updates** — Admin can push status changes instantly visible to users
- 🧩 **Modular architecture** — Three independent apps, cleanly decoupled

---

## 🧠 Key Learnings

- Designing a multi-app monorepo with shared API contracts between frontend and admin
- Implementing JWT auth flow end-to-end: sign-up → token → protected routes
- Managing global state with React Context + `useReducer` for cart operations
- Building RESTful APIs with Express following MVC pattern
- Handling async operations and error boundaries in React

---

## 🛠️ Tech Stack

| Tool | Purpose |
|:---|:---|
| React.js | Frontend & Admin UI framework |
| Node.js | Backend JavaScript runtime |
| Express.js | REST API framework |
| MongoDB | NoSQL database |
| Mongoose | MongoDB ODM |
| JWT | Authentication & authorization |
| CSS3 | Styling & responsive layout |
| React Context API | Global state management |
| Vite | Frontend build tool |

---

<div align="center">

### Connect with me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/ronakrajput8882)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/techwithronak)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ronakrajput8882)

*If you found this useful, please ⭐ the repo!*

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,12,24&height=100&section=footer" width="100%"/>

</div>
<p align="center">
  <img src="frontend/src/components/img/logo.png" alt="Fleet Manager Logo" width="120" />
</p>

<h1 align="center">Fleet Manager — Vehicle Fleet Management System</h1>

<p align="center">
  <strong>Full-stack web application for managing corporate vehicle fleets, built for Algerie Telecom</strong>
</p>

<p align="center">
  <a href="https://dot-parcauto.netlify.app/">Live Demo</a> ·
  <a href="#features">Features</a> ·
  <a href="#tech-stack">Tech Stack</a> ·
  <a href="#getting-started">Getting Started</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/React-19-61DAFB?style=for-the-badge&logo=react&logoColor=white" alt="React" />
  <img src="https://img.shields.io/badge/TypeScript-5-3178C6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript" />
  <img src="https://img.shields.io/badge/Node.js-Express-339933?style=for-the-badge&logo=node.js&logoColor=white" alt="Node.js" />
  <img src="https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL" />
  <img src="https://img.shields.io/badge/Tailwind_CSS-3-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white" alt="Tailwind CSS" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="MIT License" />
</p>

---

## Preview

<p align="center">
  <img src="screenshots/login-page.png" alt="Login Page" width="700" />
</p>

---

## About

> Web application developed as part of the SPE internship (2nd year Cycle Supérieur, Software Engineering track) at ESI — the internship required to advance to the specialization year of the cycle supérieur — carried out within the General Resources department of **Algerie Telecom**.

Algerie Telecom operates a fleet of vehicles distributed across multiple regional centers. Managing vehicle data manually — mileage tracking, fuel costs, repairs, spare parts inventory — led to inefficiencies, human errors, and a lack of visibility for decision-making.

**Fleet Manager** was built to **centralize, secure, and automate** these operations through a modern web interface with role-based access control:

| Role | Description |
|------|-------------|
| **Administrator** | General Resources Engineer — full access to all centers and data |
| **Center Manager** | Regional center head — access restricted to their own center |

---

## Features

### Vehicle Management
- Full CRUD operations on the vehicle registry
- Monthly mileage tracking (start/end index, distance traveled)
- Cost tracking per vehicle (fuel, maintenance, total)
- Assignment of a responsible person per vehicle

### Repair Management
- Complete lifecycle tracking: `Planned` → `In Progress` → `Completed` / `Cancelled`
- Spare parts association per repair (quantity, unit price at time of use)
- Full repair history per vehicle

### Spare Parts Inventory
- Parts catalog with name, reference, unit price, current and minimum stock levels
- Low-stock alerts

### User Management
- Secure authentication with JWT (access + refresh tokens)
- Role-based permissions system: `ADMIN` / `CHEF`
- Admins see all centers; center managers only see their own data

### Reporting & Export
- Data export to **Excel** (`.xlsx`)
- Global export for admins, filtered by center for managers
- Automatic cost calculation: `Total cost = Sum(fuel) + Sum(maintenance)`

---

## Architecture

The project follows an **MVC (Model-View-Controller)** architecture:

```
User  <->  View (React)  <->  Controller (Node/Express)  <->  Model  <->  MySQL Database
```

```
fleet-manager/
├── backend/                  # REST API (Node.js / Express / TypeScript)
│   ├── src/
│   │   ├── config/           # Database configuration & schema
│   │   ├── middleware/       # JWT authentication & request validation
│   │   ├── routes/           # REST API route handlers
│   │   │   ├── authroutes.js
│   │   │   ├── vehiculeroutes.js
│   │   │   ├── reparationroutes.js
│   │   │   ├── piecesroutes.js
│   │   │   ├── carburantroutes.js
│   │   │   └── usersroutes.js
│   │   ├── services/         # Business logic layer
│   │   ├── types/            # TypeScript type definitions
│   │   └── server.ts         # Server entry point
│   ├── .env.example
│   ├── package.json
│   └── tsconfig.json
│
├── frontend/                 # Client application (React / TypeScript / Vite)
│   ├── src/
│   │   ├── components/       # React components (Login, VehicleList, RepairList, etc.)
│   │   ├── context/          # Authentication context
│   │   ├── hooks/            # Custom React hooks
│   │   ├── lib/              # Utilities & API client
│   │   ├── pages/            # Application pages
│   │   └── types/            # TypeScript type definitions
│   ├── package.json
│   ├── vite.config.ts
│   └── tailwind.config.ts
│
└── README.md
```

---

## Tech Stack

| Layer | Technologies |
|-------|-------------|
| **Backend** | Node.js, Express.js, TypeScript |
| **Frontend** | React 19, TypeScript, Vite, Tailwind CSS |
| **UI Components** | Radix UI, shadcn/ui, Lucide Icons, Framer Motion |
| **Database** | MySQL |
| **Authentication** | JWT (jsonwebtoken), bcryptjs |
| **State & Data Fetching** | Zustand, TanStack React Query |
| **Forms & Validation** | React Hook Form, Zod |
| **Excel Export** | SheetJS (xlsx) |
| **UI Design** | Figma |

---

## Data Model

```
┌────────────────────┐          ┌────────────────────────┐
│   UTILISATEUR      │          │      VEHICULE          │
│   (User)           │          │      (Vehicle)         │
├────────────────────┤          ├────────────────────────┤
│ PK id_utilisateur  │<────────┐│ PK id_vehicule         │
│    nom             │         ││    marque (brand)      │
│    email (UNIQUE)  │         ││    modele (model)      │
│    mot_de_passe    │         ││    annee (year)        │
│    role (ADMIN/CHEF│         ││    vin (UNIQUE)        │
│    is_active       │         ││    numero_plaque       │
│    last_login      │         ││ FK responsable_id ─────┘
│    created_at      │         │    statut (status)     │
│    updated_at      │         │    index_debut_mois    │
└────────────────────┘         │    index_fin_mois      │
         │                     │    total_carburant_prix │
         │                     │    total_maintenance_prix│
         │ created_by          │    created_at           │
         │                     │    updated_at           │
         v                     └───────────┬────────────┘
┌────────────────────┐                     │ vehicle_id
│   REPARATION       │<────────────────────┘
│   (Repair)         │
├────────────────────┤
│ PK id_reparation   │
│    date_reparation  │
│    description     │         ┌────────────────────────┐
│    cout_total      │         │  REPARATION_PIECE      │
│    statut          │         │  (Repair-Part)         │
│ FK vehicule_id     │<────────│ PK/FK reparation_id    │
│ FK created_by      │         │ PK/FK piece_id ────────┤
│    created_at      │         │    quantite            │
│    completed_at    │         │    prix_unitaire_utilise│
└────────────────────┘         └────────────┬───────────┘
                                            │
                               ┌────────────v───────────┐
                               │      PIECE             │
                               │      (Spare Part)      │
                               ├────────────────────────┤
                               │ PK id_piece            │
                               │    nom (name)          │
                               │    reference           │
                               │    prix_unitaire       │
                               │    stock_actuel        │
                               │    stock_minimum       │
                               │    created_at          │
                               └────────────────────────┘
```

---

## Roles & Permissions

| Feature | Admin | Center Manager |
|---------|:-----:|:--------------:|
| Manage users | Yes | No |
| View all vehicles (all centers) | Yes | No |
| View vehicles in own center | Yes | Yes |
| Full repair history | Yes | No |
| View repairs in own center | Yes | Yes |
| Update repair status | Yes | No |
| Request a new repair | Yes | Yes |
| Edit spare part prices | Yes | No |
| Global Excel export | Yes | No |
| Filtered Excel export (own center) | Yes | Yes |

---

## Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) (v18+)
- [MySQL](https://www.mysql.com/) (v8+)
- [Git](https://git-scm.com/)

### 1. Clone the repository

```bash
git clone https://github.com/boutainadts1/fleet-manager.git
cd fleet-manager
```

### 2. Set up the backend

```bash
cd backend
npm install
```

Create a `.env` file from the provided template:

```bash
cp .env.example .env
```

Then edit `.env` with your own values:

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=dbtelecom
JWT_SECRET=your_secret_key
PORT=3001
```

> **Note:** The database schema and tables are created automatically on server startup.

### 3. Set up the frontend

```bash
cd ../frontend
npm install
```

### 4. Run the application

**Backend** (from `/backend`):
```bash
npm run dev
```

**Frontend** (from `/frontend`):
```bash
npm run dev
```

The app will be available at `http://localhost:5173` (frontend) and the API at `http://localhost:3001` (backend).

---

## Deployment

The application is deployed to production and actively used by real end users at Algerie Telecom:

| Component | Platform | URL |
|-----------|----------|-----|
| **Frontend** | Netlify | [dot-parcauto.netlify.app](https://dot-parcauto.netlify.app/) |
| **Backend API** | Render | Secured REST API |
| **Database** | Clever Cloud | MySQL with automated backups |

---

## Results

- Fully functional application **deployed to production** and used by real users (administrators and center managers)
- Positive user testing feedback: interface rated as **intuitive**, authentication and permissions working reliably
- Excel export appreciated for **monthly reporting**
- Significant **reduction in manual work** and improved traceability of fleet data

---

## Author

**Doulate-Serouri Boutaina**

Engineering student — [ESI](https://www.esi.dz/) (Ecole Nationale Superieure d'Informatique)
2nd year Higher Cycle (2CS), Software & Information Systems track

**Internship supervised by:** Drief Adda, IT Network Engineer — Algerie Telecom

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

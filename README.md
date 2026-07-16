<p align="center">
  <img src="frontend/src/components/img/logo.png" alt="Fleet Manager Logo" width="120" />
</p>

<h1 align="center">Fleet Manager — Gestion de Parc Automobile</h1>

<p align="center">
  <strong>Application web de gestion de flotte automobile pour Algerie Telecom</strong>
</p>

<p align="center">
  <a href="https://dot-parcauto.netlify.app/">Demo en ligne</a> ·
  <a href="#fonctionnalites">Fonctionnalites</a> ·
  <a href="#stack-technique">Stack technique</a> ·
  <a href="#installation">Installation</a>
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

## Apercu

<p align="center">
  <img src="screenshots/login-page.png" alt="Login Page" width="700" />
</p>

---

## Contexte

> Projet realise dans le cadre d'un **stage de fin d'etudes** (SPE, 2eme annee Cycle Superieur, option Systemes Informatiques et Logiciels) a l'**Ecole Nationale Superieure d'Informatique (ESI)**, au sein du service des **Moyens Generaux** de la **Direction Operationnelle d'Algerie Telecom — Relizane**.

Algerie Telecom gere une flotte de **47 vehicules operationnels** repartis sur plusieurs centres dans la wilaya de Relizane. La gestion manuelle et fragmentee des donnees (kilometrage, couts de carburant, reparations, pieces detachees) entrainait des pertes de temps, des risques d'erreurs et un manque de visibilite pour la prise de decision.

**Fleet Manager** a ete concu pour **centraliser, securiser et automatiser** ces processus via une interface web moderne adaptee a deux profils d'utilisateurs :

| Role | Description |
|------|-------------|
| **Administrateur** | Ingenieur des Moyens Generaux — acces complet a tous les centres |
| **Chef de Centre** | Responsable CMP/Actel — acces restreint a son centre uniquement |

---

## Fonctionnalites

### Gestion des vehicules
- Ajout, modification, suppression et consultation des vehicules
- Suivi du kilometrage (index debut/fin de mois, distance parcourue)
- Suivi des couts (carburant, maintenance, total)
- Attribution d'un responsable par vehicule

### Gestion des reparations
- Cycle de vie complet : `Planifiee` → `En cours` → `Terminee` / `Annulee`
- Association de pieces detachees (quantite, prix unitaire utilise)
- Historique complet des interventions par vehicule

### Gestion des pieces detachees
- Inventaire complet (nom, reference, prix unitaire, stock actuel/minimum)
- Alertes de stock bas

### Gestion des utilisateurs
- Authentification securisee via JWT (access + refresh tokens)
- Systeme de roles/permissions : `ADMIN` / `CHEF`
- L'admin gere tous les centres ; le chef ne voit que son propre centre

### Reporting & Export
- Export des donnees en **Excel** (`.xlsx`)
- Global pour l'admin, filtre par centre pour le chef
- Calcul automatique : `Cout total = Sigma carburant + Sigma maintenance`

---

## Architecture

Le projet suit une architecture **MVC (Modele–Vue–Controleur)** :

```
User  <->  View (React)  <->  Controller (Node/Express)  <->  Model  <->  MySQL Database
```

```
fleet_manager/
├── backend/                  # API REST (Node.js / Express / TypeScript)
│   ├── src/
│   │   ├── config/           # Configuration base de donnees + schema
│   │   ├── middleware/       # Authentification JWT & validation
│   │   ├── routes/           # Routes API REST
│   │   │   ├── authroutes.js
│   │   │   ├── vehiculeroutes.js
│   │   │   ├── reparationroutes.js
│   │   │   ├── piecesroutes.js
│   │   │   ├── carburantroutes.js
│   │   │   └── usersroutes.js
│   │   ├── services/         # Logique metier
│   │   ├── types/            # Types TypeScript
│   │   └── server.ts         # Point d'entree serveur
│   ├── .env.example
│   ├── package.json
│   └── tsconfig.json
│
├── frontend/                 # Interface utilisateur (React / TypeScript / Vite)
│   ├── src/
│   │   ├── components/       # Composants React (Login, VehicleList, RepairList, etc.)
│   │   ├── context/          # Contexte d'authentification
│   │   ├── hooks/            # Hooks personnalises
│   │   ├── lib/              # Utilitaires & appels API
│   │   ├── pages/            # Pages de l'application
│   │   └── types/            # Types TypeScript
│   ├── package.json
│   ├── vite.config.ts
│   └── tailwind.config.ts
│
└── README.md
```

---

## Stack technique

| Couche | Technologies |
|--------|-------------|
| **Backend** | Node.js, Express.js, TypeScript |
| **Frontend** | React 19, TypeScript, Vite, Tailwind CSS |
| **UI Components** | Radix UI, shadcn/ui, Lucide Icons, Framer Motion |
| **Base de donnees** | MySQL |
| **Authentification** | JWT (jsonwebtoken), bcryptjs |
| **Etat & Data Fetching** | Zustand, TanStack React Query |
| **Formulaires** | React Hook Form, Zod (validation) |
| **Export Excel** | SheetJS (xlsx) |
| **Maquettage** | Figma |

---

## Modele de donnees

```
┌────────────────────┐          ┌────────────────────────┐
│   UTILISATEUR      │          │      VEHICULE          │
├────────────────────┤          ├────────────────────────┤
│ PK id_utilisateur  │<────────┐│ PK id_vehicule         │
│    nom             │         ││    marque              │
│    email (UNIQUE)  │         ││    modele              │
│    mot_de_passe    │         ││    annee               │
│    role (ADMIN/CHEF│         ││    vin (UNIQUE)        │
│    is_active       │         ││    numero_plaque       │
│    last_login      │         ││ FK responsable_id ─────┘
│    created_at      │         │    statut              │
│    updated_at      │         │    index_debut_mois    │
└────────────────────┘         │    index_fin_mois      │
         │                     │    total_carburant_prix │
         │                     │    total_maintenance_prix│
         │ created_by          │    created_at           │
         │                     │    updated_at           │
         v                     └───────────┬────────────┘
┌────────────────────┐                     │ vehicle_id
│   REPARATION       │<────────────────────┘
├────────────────────┤
│ PK id_reparation   │
│    date_reparation  │
│    description     │         ┌────────────────────────┐
│    cout_total      │         │  REPARATION_PIECE      │
│    statut          │         ├────────────────────────┤
│ FK vehicule_id     │<────────│ PK/FK reparation_id    │
│ FK created_by      │         │ PK/FK piece_id ────────┤
│    created_at      │         │    quantite            │
│    completed_at    │         │    prix_unitaire_utilise│
└────────────────────┘         └────────────┬───────────┘
                                            │
                               ┌────────────v───────────┐
                               │      PIECE             │
                               ├────────────────────────┤
                               │ PK id_piece            │
                               │    nom                 │
                               │    reference           │
                               │    prix_unitaire       │
                               │    stock_actuel        │
                               │    stock_minimum       │
                               │    created_at          │
                               └────────────────────────┘
```

---

## Roles et permissions

| Fonctionnalite | Admin | Chef |
|----------------|:-----:|:----:|
| Gerer les utilisateurs | Oui | Non |
| Voir tous les vehicules (tous centres) | Oui | Non |
| Voir les vehicules de son centre | Oui | Oui |
| Historique complet des reparations | Oui | Non |
| Consulter les reparations de son centre | Oui | Oui |
| Changer le statut d'une reparation | Oui | Non |
| Demander une nouvelle reparation | Oui | Oui |
| Modifier les prix des pieces | Oui | Non |
| Export Excel global | Oui | Non |
| Export Excel (filtre par centre) | Oui | Oui |

---

## Installation

### Prerequis

- [Node.js](https://nodejs.org/) (v18+)
- [MySQL](https://www.mysql.com/) (v8+)
- [Git](https://git-scm.com/)

### 1. Cloner le depot

```bash
git clone https://github.com/<your-username>/fleet-manager.git
cd fleet-manager
```

### 2. Configurer le backend

```bash
cd backend
npm install
```

Creer un fichier `.env` a partir du template :

```bash
cp .env.example .env
```

Puis modifier les variables dans `.env` avec vos propres valeurs :

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=dbtelecom
JWT_SECRET=your_secret_key
PORT=3001
```

> **Note :** La base de donnees et les tables sont creees automatiquement au demarrage du serveur.

### 3. Configurer le frontend

```bash
cd ../frontend
npm install
```

### 4. Lancer l'application

**Backend** (depuis `/backend`) :
```bash
npm run dev
```

**Frontend** (depuis `/frontend`) :
```bash
npm run dev
```

L'application sera accessible sur `http://localhost:5173` (frontend) et l'API sur `http://localhost:3001` (backend).

---

## Deploiement

L'application est deployee en production et utilisee par les utilisateurs reels d'Algerie Telecom :

| Composant | Plateforme | URL |
|-----------|-----------|-----|
| **Frontend** | Netlify | [dot-parcauto.netlify.app](https://dot-parcauto.netlify.app/) |
| **Backend (API)** | Render | API REST securisee |
| **Base de donnees** | Clever Cloud | MySQL avec sauvegardes automatisees |

---

## Resultats

- Application **fonctionnelle et deployee en production**, utilisee par les utilisateurs reels (administrateur et chefs de centre)
- Tests utilisateurs concluants : interface jugee **intuitive**, authentification/permissions fiables
- Export Excel apprecie pour les **rapports mensuels**
- **Reduction du travail manuel** et meilleure tracabilite des donnees du parc automobile

---

## Auteure

**Doulate-Serouri Boutaina**

Eleve ingenieure — [ESI](https://www.esi.dz/) (Ecole Nationale Superieure d'Informatique)
2eme annee Cycle Superieur (2CS), option Systemes Informatiques et Logiciels

**Stage encadre par :** Drief Adda, Ingenieur Reseau Informatique — Algerie Telecom, Direction Operationnelle de Relizane

---

## Licence

Ce projet est distribue sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus d'informations.

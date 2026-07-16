# GitHub Repository Setup Guide

## Repository Description (paste into GitHub "About" section)

Fleet management web app for Algerie Telecom — Built with React, Node.js, Express & MySQL | Internship project at ESI (Ecole Nationale Superieure d'Informatique)

## Topics (add these as GitHub topics)

react, nodejs, express, mysql, typescript, tailwindcss, fleet-management, vite, jwt-authentication, rest-api, shadcn-ui, internship-project

## Steps to Push to GitHub

### 1. Initialize Git (from fleet_manager_algerieTelecom directory)

```bash
cd fleet_manager_algerieTelecom
git init
```

### 2. Make sure .env is NOT tracked

```bash
# If backend/.env was already tracked, remove it from git tracking:
git rm --cached backend/.env 2>/dev/null
```

### 3. Stage and commit

```bash
git add .
git commit -m "Initial commit — Fleet Manager (Algerie Telecom internship project)"
```

### 4. Create repo on GitHub, then push

```bash
git branch -M main
git remote add origin https://github.com/<your-username>/fleet-manager.git
git push -u origin main
```

## Important: Security Check Before Pushing

Make sure the following are NOT being pushed:
- `backend/.env` (contains real database credentials)
- `node_modules/` directories
- `.mgx/` directory

You can verify by running:
```bash
git status
```

And making sure none of the above appear in the list.

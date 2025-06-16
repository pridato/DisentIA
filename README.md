# 🧠 Veritas — Pensamiento Crítico Asistido por IA

Veritas es una plataforma que promueve la **búsqueda activa de la verdad**, analizando afirmaciones mediante inteligencia artificial. El sistema detecta posibles sesgos, clasifica el tipo de evidencia, genera contraargumentos razonados y sugiere fuentes alternativas. Está diseñado para estudiantes, educadores, creadores de contenido y cualquier persona interesada en fortalecer su pensamiento crítico.

---

## ✨ Características principales

- 🧩 Análisis semántico de afirmaciones (con IA)
- ⚖️ Generación automática de contraargumentos estructurados
- 📚 Clasificación de evidencia: opinión, dato, hipótesis, etc.
- 📈 Panel de métricas y sesgos comunes
- 🔗 Sugerencia de fuentes externas confiables
- 🐳 Arquitectura modular con Docker y microservicios

---

## 🧱 Arquitectura del sistema

```plaintext
React (Vite)
   ↓
NestJS (Backend API)
   ├── PostgreSQL (persistencia)
   ├── Redis (caché / colas)
   └── NLP Microservicio (FastAPI / Python)
```

---

## 📁 Estructura del proyecto

```
veritas-project/
├── frontend/          → Aplicación React con Vite + TS
├── backend/           → API NestJS modular
├── nlp-service/       → Microservicio en Python (FastAPI) para IA y PLN
├── docker/            → Dockerfiles de cada servicio
├── docker-compose.yml → Orquestación completa del sistema
├── .env               → Variables de entorno (no versionar)
└── README.md
```

---

## 🚀 Cómo ejecutar (modo desarrollo)

### Requisitos:
- Node.js >= 18.20.8
- Python >= 3.10
- Docker y Docker Compose

### Paso a paso:

```bash
# Clona el proyecto
git clone https://github.com/tu-usuario/veritas.git
cd veritas

# Arranca todo con Docker
docker-compose up --build
```

Servicios disponibles:
- 🖥️ Frontend: http://localhost:5173  
- 🔧 Backend API: http://localhost:3000  
- 🤖 NLP Service: http://localhost:5000

---

## ⚙️ Scripts útiles

```bash
# Frontend (React)
cd frontend
npm install
npm run dev

# Backend (NestJS)
cd backend
npm install
npm run start:dev

# NLP Microservicio (Python)
cd nlp-service
python -m venv env
source env/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 5000
```

---

## 🔐 Variables de entorno (.env)

Ejemplo mínimo:
```
DATABASE_URL=postgresql://user:password@localhost:5432/veritas
REDIS_URL=redis://localhost:6379
OPENAI_API_KEY=tu_api_key
```

---

## 📈 Roadmap (ideas a futuro)

- [ ] Clasificación automática de falacias lógicas
- [ ] Plugin para navegadores (analizar textos en Twitter/Reddit)
- [ ] Panel educativo para profesores
- [ ] API pública para terceros

---

## 🧠 Filosofía del proyecto

> “Veritas no busca convencerte, sino mostrarte lo que quizás no habías considerado. Porque pensar críticamente es cuestionar incluso lo que uno cree saber.”

---

## 📄 Licencia

MIT © pridato

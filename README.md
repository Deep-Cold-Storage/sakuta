<p align="center">
  <h3 align="center">Sakuta</h3>
  <p align="center">Contractor management module built for a university assignment.</p>
</p>

---

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

Source code of **Sakuta**, contractor management module built for a university assignment with **FastAPI** and **Vue.js**.

> 🔥 Sakuta was built as an assignment for my university course.

> 👑 It's alive! Check it out live at [sakuta.bednarski.dev](https://sakuta.bednarski.dev/)!

<br>

## 🛠 Best Features

Below are the most important features.

- Docker container **health check** with a custom monitoring solution.

- Managed **Sentry** used for application monitoring and exception tracking.

- **CI/CD** pipelines for automatic building and deploying on my infrastructure build on top of **GitHub Actions**.

- Simple **End-To-End tests** build with the **Cypress** testing framework run before each frontend deploy by CI/CD system to achieve the best user experience.

<br>

### Backend Specific

- **Integration tests** for the API service build with **PyTest** modules.

- Python 3 (FastAPI) **RESTful** API build on top of **PostgreSQL** for storing application state.

- Monitoring `/health` endpoint with microservice status.

- Fully **Dockerized** development and deploy workflow.

<br>

### Frontend Specific

- **SPA** frontend build with **Vue.js** and **Vue-Router**.

<br>

## 💻 Running Locally

**It's easy to get started with developing Sakuta!**

This project uses **Docker** as a development and production deployment tool, so **you need It** first!

<br>

### Backend

> 💡 Execute every command in the `./backend` directory!

**If you only want to run It**, you need to:

- Spin up Sakuta as containers, simply type:

  ```bash
  docker run -e DATABASE_URL="" -p 8000:8000 rangerdigital/sakuta:latest
  ```

This will spin up Sakuta and expose service **API** at `http://127.0.0.1:8000`.

<br>

**If you want to make changes** to the **FastAPI** app, you need to:

- Install **Python 3.8**, then projects requirements.

  ```bash
  pip3 install -r requirements.txt
  ```

- Run `main.py`, entry point for FastAPI app.

  ```bash
  uvicorn backend.main:app
  ```

  This will spin up the development server at `http://127.0.0.1:5000`.

<br>

### Frontend

> 💡 Execute every command in the `./frontend` directory!

If **you want to make changes** to the **Vue.js** app, you need to:

- Install **NPM**, then projects requirements.

  ```bash
  npm install
  ```

- To then serve a website, simply type:

  ```bash
  npm run serve
  ```

This will create a development web server at `http://127.0.0.1:8080`.
And It's a lot simpler!

<br>

## 📋 Running Tests

**Sakuta has a simple set of functional tests!**

This project uses **PyTest** and **Cypress** as a testing tools, so **you need them** first!

- To run **backend tests**, run Sakuta API service and in the `./backend` directory type:

  ```bash
  pytest .
  ```

- To run **Cypress E2E** tests, with everything running, open dashboard by typing:

  ```bash
  npm run open
  ```

  This will open a dashboard that will let you run all the specs.

<br>

## 🚧 Contributing

**You are more than welcome to help me improve Sakuta!**

Just fork this project from the `master` branch and submit a Pull Request (PR).  
It's probably a good idea to run all the tests beforehand.

<br>

## 📃 License

This project is licensed under [GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/) .

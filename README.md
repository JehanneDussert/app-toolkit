# app-toolkit

Basic frontend and backend for faster launch of new repositories.

## Front-end

### General

#### 🔋 Stack: TypeScript, React, Tailwind
#### 💅 Code formatter: prettier
#### 📚 Libraries
- [x] [Base Mui](https://mui.com/base-ui/)
- [x] [Mui Charts](https://mui.com/x/react-charts/getting-started/)
- [x] [Tailwind UI](https://tailwindui.com/)

### Usage

Dev mode:
```
npm run dev
npx tailwindcss -i ./src/style/input.css -o ./src/style/output.css --watch
```

Build mode:
```
npm run build
```

Dockerize:
```
docker build -t frontend:latest .
docker run -p 3000:3000 frontend
```

## Backend-end

### General

#### 🔋 Stack: Python, FastAPI, SQLite
<!-- #### 💅 Code formatter: ? -->
#### 📚 Libraries
- [x] [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
- [x] [Requests](https://pypi.org/project/requests/)
- [x] [Pydantic](https://docs.pydantic.dev/latest/)
- [x] [SQLAlchemy](https://www.sqlalchemy.org/)

### Usage

```
uvicorn main:app --reload
```

Dockerize:
```
docker build -t backend:latest .
docker run -p 8000:8000 backend
```
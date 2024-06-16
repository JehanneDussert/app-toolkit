# app-toolkit

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

#### 🔋 Stack: Python, FastAPI
#### 💅 Code formatter: ?
#### 📚 Libraries
- [x]

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
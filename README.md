# DevOps Assignment

## ✅ Tasks Covered

1. Linear Regression using sklearn’s diabetes dataset.
2. Dockerize the model training and save it as a .pkl file.
3. Accept 3 numbers and find the largest using Python & Docker.
4. Accept 5 names and save them to a file using Docker.
5. Read the names from the file using Docker.

---

## 🐳 Docker Instructions

### Build & Run for Each Task

#### Task 1 - Linear Regression
```
docker build -t linear-regression-app -f Dockerfile .
docker run linear-regression-app
```

#### Task 3 - Largest of 3 Numbers
```
docker build -t largest-app -f Dockerfile_q3 .
docker run -it largest-app
```

#### Task 4 - Save 5 Names
```
docker build -t save-names-app -f Dockerfile_q4 .
docker run -it save-names-app
```

#### Task 5 - Read Names
```
docker build -t read-names-app -f Dockerfile_q5 .
docker run read-names-app
```

---

## 🧠 Git Workflow

### Steps to Follow
1. Create a GitHub repository.
2. Clone it to your local machine:
```
git clone https://github.com/your-username/devops-assignment.git
cd devops-assignment
```
3. Add all files to the repo:
```
git add .
git commit -m "Initial commit - DevOps Assignment"
git push origin main
```

Make sure you replace the GitHub link with your actual repo URL.
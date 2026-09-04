"""
Skill graph data for the AI Learning Path Generator.

Each career path is a dict of:
    skill_name -> {
        "prereqs": [list of skill names that must come before this one],
        "hours": estimated hours to learn this skill,
        "course": a suggested course/resource name,
        "category": grouping used for display
    }

This graph is the backbone of the roadmap generator (topological sort)
and the gap analysis engine (set difference + ordering).
"""

CAREER_PATHS = {

    "Java Developer": {
        "Java Basics":            {"prereqs": [], "hours": 15, "course": "Java Programming Masterclass", "category": "Foundations"},
        "OOP Concepts":           {"prereqs": ["Java Basics"], "hours": 12, "course": "Java OOP Concepts", "category": "Foundations"},
        "Collections Framework":  {"prereqs": ["OOP Concepts"], "hours": 10, "course": "Java Collections Deep Dive", "category": "Core Java"},
        "Exception Handling":     {"prereqs": ["OOP Concepts"], "hours": 5,  "course": "Java Exceptions & Debugging", "category": "Core Java"},
        "Multithreading":         {"prereqs": ["Collections Framework"], "hours": 12, "course": "Java Concurrency in Practice", "category": "Core Java"},
        "JDBC":                   {"prereqs": ["Exception Handling"], "hours": 8,  "course": "JDBC & SQL for Java Devs", "category": "Data Access"},
        "Spring Core":            {"prereqs": ["Collections Framework", "Exception Handling"], "hours": 15, "course": "Spring Framework 6 Fundamentals", "category": "Frameworks"},
        "Spring Boot":            {"prereqs": ["Spring Core"], "hours": 15, "course": "Spring Boot 3 Bootcamp", "category": "Frameworks"},
        "REST APIs":              {"prereqs": ["Spring Boot"], "hours": 10, "course": "Building REST APIs with Spring Boot", "category": "Frameworks"},
        "Hibernate / JPA":        {"prereqs": ["JDBC", "Spring Boot"], "hours": 12, "course": "Hibernate & JPA in Depth", "category": "Data Access"},
        "JUnit Testing":          {"prereqs": ["Spring Boot"], "hours": 8,  "course": "JUnit 5 & Mockito", "category": "Testing"},
        "Microservices":          {"prereqs": ["REST APIs", "Hibernate / JPA"], "hours": 20, "course": "Microservices with Spring Cloud", "category": "Architecture"},
        "Docker & Deployment":    {"prereqs": ["Microservices"], "hours": 12, "course": "Docker for Java Developers", "category": "DevOps"},
    },

    "Data Analyst": {
        "Excel Fundamentals":     {"prereqs": [], "hours": 8,  "course": "Excel for Data Analysis", "category": "Foundations"},
        "SQL Basics":             {"prereqs": [], "hours": 10, "course": "SQL for Data Analysis", "category": "Foundations"},
        "Advanced SQL":           {"prereqs": ["SQL Basics"], "hours": 10, "course": "Advanced SQL: Window Functions & CTEs", "category": "Data Querying"},
        "Python Basics":          {"prereqs": [], "hours": 15, "course": "Python for Everybody", "category": "Foundations"},
        "Pandas & NumPy":         {"prereqs": ["Python Basics"], "hours": 15, "course": "Data Analysis with Pandas", "category": "Data Wrangling"},
        "Data Cleaning":          {"prereqs": ["Pandas & NumPy"], "hours": 8,  "course": "Practical Data Cleaning", "category": "Data Wrangling"},
        "Statistics Fundamentals":{"prereqs": [], "hours": 12, "course": "Statistics for Data Analysts", "category": "Foundations"},
        "Data Visualization":     {"prereqs": ["Pandas & NumPy"], "hours": 10, "course": "Matplotlib & Seaborn", "category": "Visualization"},
        "Tableau / Power BI":     {"prereqs": ["Data Visualization"], "hours": 12, "course": "Tableau A-Z", "category": "Visualization"},
        "Excel Dashboards":       {"prereqs": ["Excel Fundamentals"], "hours": 8,  "course": "Excel Dashboard Design", "category": "Visualization"},
        "A/B Testing":            {"prereqs": ["Statistics Fundamentals"], "hours": 8, "course": "A/B Testing in Practice", "category": "Analysis"},
        "Business Storytelling":  {"prereqs": ["Tableau / Power BI", "A/B Testing"], "hours": 6, "course": "Data Storytelling for Analysts", "category": "Communication"},
    },

    "ML Engineer": {
        "Python Basics":          {"prereqs": [], "hours": 15, "course": "Python for Everybody", "category": "Foundations"},
        "Math for ML":            {"prereqs": [], "hours": 20, "course": "Linear Algebra & Calculus for ML", "category": "Foundations"},
        "Statistics & Probability":{"prereqs": [], "hours": 15, "course": "Statistics for Machine Learning", "category": "Foundations"},
        "Pandas & NumPy":         {"prereqs": ["Python Basics"], "hours": 15, "course": "Data Analysis with Pandas", "category": "Data Wrangling"},
        "Data Visualization":     {"prereqs": ["Pandas & NumPy"], "hours": 10, "course": "Matplotlib & Seaborn", "category": "Data Wrangling"},
        "Supervised Learning":    {"prereqs": ["Math for ML", "Statistics & Probability", "Pandas & NumPy"], "hours": 20, "course": "Andrew Ng's Machine Learning Specialization", "category": "Core ML"},
        "Unsupervised Learning":  {"prereqs": ["Supervised Learning"], "hours": 12, "course": "Clustering & Dimensionality Reduction", "category": "Core ML"},
        "Model Evaluation":       {"prereqs": ["Supervised Learning"], "hours": 8,  "course": "Model Evaluation & Validation", "category": "Core ML"},
        "Feature Engineering":    {"prereqs": ["Model Evaluation"], "hours": 10, "course": "Feature Engineering for ML", "category": "Core ML"},
        "Deep Learning Basics":   {"prereqs": ["Feature Engineering"], "hours": 20, "course": "Deep Learning Specialization", "category": "Deep Learning"},
        "Neural Networks (CNN/RNN)":{"prereqs": ["Deep Learning Basics"], "hours": 20, "course": "CNNs & RNNs in Practice", "category": "Deep Learning"},
        "MLOps Basics":           {"prereqs": ["Model Evaluation"], "hours": 12, "course": "MLOps Fundamentals", "category": "Deployment"},
        "Model Deployment":       {"prereqs": ["MLOps Basics", "Neural Networks (CNN/RNN)"], "hours": 15, "course": "Deploying ML Models with Docker & FastAPI", "category": "Deployment"},
    },

    "Frontend Developer": {
        "HTML & CSS":             {"prereqs": [], "hours": 12, "course": "HTML & CSS Full Course", "category": "Foundations"},
        "JavaScript Basics":      {"prereqs": ["HTML & CSS"], "hours": 15, "course": "JavaScript: The Basics", "category": "Foundations"},
        "DOM & Events":           {"prereqs": ["JavaScript Basics"], "hours": 8,  "course": "JS DOM Manipulation", "category": "Foundations"},
        "ES6+ Features":          {"prereqs": ["JavaScript Basics"], "hours": 8,  "course": "Modern JavaScript ES6+", "category": "Foundations"},
        "Git & GitHub":           {"prereqs": [], "hours": 5,  "course": "Git & GitHub Crash Course", "category": "Tooling"},
        "React Fundamentals":     {"prereqs": ["DOM & Events", "ES6+ Features"], "hours": 18, "course": "React - The Complete Guide", "category": "Frameworks"},
        "React Hooks":            {"prereqs": ["React Fundamentals"], "hours": 10, "course": "React Hooks Deep Dive", "category": "Frameworks"},
        "State Management":       {"prereqs": ["React Hooks"], "hours": 10, "course": "Redux & Context API", "category": "Frameworks"},
        "API Integration":        {"prereqs": ["React Hooks"], "hours": 8,  "course": "Consuming REST APIs in React", "category": "Frameworks"},
        "Responsive Design":      {"prereqs": ["HTML & CSS"], "hours": 8,  "course": "Responsive Web Design / Tailwind CSS", "category": "Styling"},
        "Testing (Jest/RTL)":     {"prereqs": ["State Management"], "hours": 10, "course": "Testing React Apps", "category": "Testing"},
        "Deployment (Vercel/Netlify)": {"prereqs": ["API Integration", "Responsive Design"], "hours": 5, "course": "Deploying Frontend Apps", "category": "DevOps"},
    },

    "DevOps Engineer": {
        "Linux Fundamentals":     {"prereqs": [], "hours": 15, "course": "Linux Command Line Basics", "category": "Foundations"},
        "Networking Basics":      {"prereqs": [], "hours": 10, "course": "Networking Fundamentals", "category": "Foundations"},
        "Git & GitHub":           {"prereqs": [], "hours": 5,  "course": "Git & GitHub Crash Course", "category": "Tooling"},
        "Bash Scripting":         {"prereqs": ["Linux Fundamentals"], "hours": 10, "course": "Bash Scripting for Automation", "category": "Scripting"},
        "Python for Automation":  {"prereqs": ["Bash Scripting"], "hours": 12, "course": "Python Automation Scripts", "category": "Scripting"},
        "Docker":                 {"prereqs": ["Linux Fundamentals"], "hours": 15, "course": "Docker Mastery", "category": "Containers"},
        "Kubernetes":             {"prereqs": ["Docker"], "hours": 20, "course": "Kubernetes for Beginners", "category": "Containers"},
        "CI/CD Pipelines":        {"prereqs": ["Git & GitHub", "Docker"], "hours": 15, "course": "CI/CD with GitHub Actions / Jenkins", "category": "Automation"},
        "Infrastructure as Code": {"prereqs": ["CI/CD Pipelines"], "hours": 15, "course": "Terraform for Beginners", "category": "Cloud"},
        "Cloud Basics (AWS)":     {"prereqs": ["Networking Basics"], "hours": 20, "course": "AWS Certified Cloud Practitioner", "category": "Cloud"},
        "Monitoring & Logging":   {"prereqs": ["Kubernetes"], "hours": 10, "course": "Prometheus & Grafana", "category": "Observability"},
        "Cloud Deployment":       {"prereqs": ["Infrastructure as Code", "Cloud Basics (AWS)"], "hours": 15, "course": "Deploying to AWS with Terraform", "category": "Cloud"},
    },
}

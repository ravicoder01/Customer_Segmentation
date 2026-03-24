# Customer Segmentation AI Dashboard

A Machine Learning project that uses **K-Means Clustering** to segment retail store customers based on their purchasing behavior.

The project also includes an **interactive dashboard web application** built using Flask and JavaScript where users can predict customer segments in real time.

---

# Project Overview

This project analyzes customer data from a mall dataset and divides customers into meaningful groups based on:

- Annual Income
- Spending Score

Customer segmentation helps businesses understand their audience and create **targeted marketing strategies**.

---

# Tech Stack

|      Category        |     Technologies 
|----------------------|----------------------------------|
| Programming Language |     Python                       |
| Machine Learning     | Scikit-learn (K-Means Clustering)|
| Data Processing      | Pandas, NumPy                    |
| Data Visualization   | Matplotlib, Seaborn, Chart.js    |
| Backend              | Flask                            |
| Frontend             | HTML, CSS, JavaScript            |
| Dashboard            | Chart.js                         |
| Version Control      | Git & GitHub                     |

---

# Project Folder Structure

|    Folder / File              |      Description 
|-------------------------------|-----------------------|
| `backend/`                    | Flask backend API |
| `frontend/`                   | Web dashboard UI |
| `model/`                      | Saved ML model |
| `Customer_Segmentation.ipynb` | Jupyter notebook for ML model development |
| `Mall_Customers.csv`          | Dataset used for clustering |
| `README.md`                   | Project documentation |

### Detailed Structure
```
Customer_Segmentation
│
├── backend
│ └── app.py
│
├── frontend
│ ├── index.html
│ ├── style.css
│ └── script.js
│
├── model
│ └── kmeans_model.pkl
│
├── Customer_Segmentation.ipynb
├── Mall_Customers.csv
└── README.md
---
```

# Dataset Information

The dataset used in this project is **Mall_Customers.csv**.
```
|     Feature            |       Description 
|------------------------|-------------------------|
| CustomerID             | Unique ID of the customer |
| Gender                 | Male or Female |
| Age                    | Customer age |
| Annual Income (k$)     | Customer income |
| Spending Score (1-100) | Spending behavior score |

For clustering, we selected:

- **Annual Income (k$)**
- **Spending Score (1-100)**

---
```
# Machine Learning Workflow
```
| Step | Description |
|-----|-------------|
| Data Loading | Dataset loaded using Pandas |
| Feature Selection | Selected Income & Spending Score |
| Feature Scaling | StandardScaler used |
| Finding Optimal K | Elbow Method |
| Model Training | K-Means clustering applied |
| Cluster Assignment | Customers assigned cluster labels |
| Visualization | Scatter plot used to visualize clusters |

---
```
# Customer Segments Identified
```
The algorithm identified **5 customer segments**:

| Cluster   | Customer Type  |
|-----------|----------------|
| Cluster 0 | Low Income – Low Spending |
| Cluster 1 | Low Income – High Spending |
| Cluster 2 | Average Customers |
| Cluster 3 | High Income – Low Spending |
| Cluster 4 | High Income – High Spending |

---
```
# Web Dashboard Features

The project also includes an **interactive AI dashboard**.
```
|       Feature         |     Description |
|-----------------------|-----------------|
| Prediction Panel      | Enter customer income & spending score |
| Real-time Prediction  | Predict customer cluster |
| Cluster Visualization | Scatter graph showing clusters |
| ML API                | Flask backend serving predictions |
| Interactive UI        | Responsive dashboard layout |

---
```
# How To Run The Project

### 1 Clone Repository

```bash
git clone https://github.com/ravicoder01/Customer_Segmentation.git
cd Customer_Segmentation
2 Install Required Libraries
pip install pandas numpy scikit-learn flask flask-cors matplotlib seaborn
3 Run Backend Server
cd backend
python app.py

Server will start at:

http://127.0.0.1:5000
4 Run Frontend

Open the frontend using Live Server or open:

frontend/index.html

in the browser.

Real World Applications

Customer segmentation helps businesses:

Application	Benefit
Targeted Marketing	Personalized campaigns
Customer Insights	Understand customer behavior
Product Recommendations	Suggest relevant products
Marketing Optimization	Better ROI
Business Strategy	Data-driven decisions
Future Improvements
Deploy dashboard online
Add real-time analytics
Add customer demographic segmentation
Improve visualization with Plotly
Author

Ravi

B.Tech Student | Machine Learning Enthusiast

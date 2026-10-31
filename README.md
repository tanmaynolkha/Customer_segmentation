# 📊 Customer Segmentation Using K-Means Clustering

A Machine Learning project that applies **K-Means Clustering**, an unsupervised learning algorithm, to customer segmentation.

The goal is to organize customers into groups based on patterns in the available customer data, helping explore customer behavior and support data-driven business decisions.

## 🎯 Project Overview

Customer segmentation is a useful technique in Data Science and business analytics. It helps identify groups of customers with similar characteristics rather than treating all customers as one group.

This project explores customer segmentation using K-Means clustering and includes a saved model and scaler for reuse.

## 🛠️ Tech Stack

- **Language:** Python
- **Data Analysis:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Development:** Jupyter Notebook
- **Model:** K-Means Clustering
- **Model Persistence:** Pickle

## 📁 Project Structure

```text
Customer_segmentation/
│
├── Customer_segmention.ipynb
├── customer_segmentation.csv
├── segmentation.py
├── kmeans_model.pkl
├── scaler.pkl
└── README.md
```

| File | Description |
|---|---|
| `Customer_segmention.ipynb` | Jupyter notebook containing the project analysis |
| `customer_segmentation.csv` | Customer segmentation dataset |
| `segmentation.py` | Python implementation of the segmentation workflow |
| `kmeans_model.pkl` | Saved K-Means model |
| `scaler.pkl` | Saved feature scaler |

## ⚙️ Methodology

The project uses the following general machine learning workflow:

1. **Data Exploration** – Examine the customer dataset and understand its features.
2. **Data Preprocessing** – Prepare the input features for clustering.
3. **Feature Scaling** – Use a scaler to prepare features for distance-based clustering.
4. **K-Means Clustering** – Apply the K-Means algorithm to group similar customers.
5. **Model Persistence** – Save the trained model and scaler using Pickle.
6. **Segmentation Analysis** – Explore the resulting customer groups.

## 🧠 Algorithm: K-Means Clustering

K-Means is an unsupervised machine learning algorithm that divides data points into a predefined number of clusters.

It works by:

- Initializing cluster centroids.
- Assigning data points to their nearest centroid.
- Updating centroids based on assigned data points.
- Repeating the process until the clusters converge.

The algorithm helps discover patterns and similarities within customer data without requiring predefined labels.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/tanmaynolkha/Customer_segmentation.git
```

### 2. Navigate to the project directory

```bash
cd Customer_segmentation
```

### 3. Install dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

### 4. Launch the notebook

```bash
jupyter notebook Customer_segmention.ipynb
```

Open the notebook and run the cells to explore the project.

## 📌 Future Improvements

- Add detailed exploratory data analysis.
- Evaluate cluster quality using suitable clustering metrics.
- Compare different values of K using the Elbow Method and Silhouette Score.
- Add clear visualizations of customer clusters.
- Provide business-oriented interpretations and recommendations.
- Develop an interactive dashboard for exploring customer segments.

## 👨‍💻 Author

**Tanmay Nolkha**

B.Tech – Artificial Intelligence & Data Science

- GitHub: [@tanmaynolkha](https://github.com/tanmaynolkha)
- Project Repository: [Customer Segmentation](https://github.com/tanmaynolkha/Customer_segmentation)

---

⭐ If you find this project interesting, consider giving the repository a star!

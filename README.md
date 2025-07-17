# Customer Segmentation using K-means Clustering

## Project Overview
In this project, I used the **K-means Clustering** machine learning algorithm to divide a retail store's customers into different groups (segments) based on their purchasing behavior. This helps businesses better understand their customers and create tailored strategies for them.

## Goal
My main goal was to identify the natural customer groups within the `Mall_Customers.csv` dataset, allowing the store to optimize its marketing and sales efforts.

## Dataset Used
For this project, I used the **`Mall_Customers.csv`** dataset. This dataset contains information such as customers' `Annual Income (k$)` and `Spending Score (1-100)`.

## Tools and Libraries Used
* **Python**: The programming language used.
* **Pandas**: For loading and managing data.
* **Scikit-learn**: For the K-means clustering algorithm and data scaling.
* **Matplotlib**: For creating plots and graphs.
* **Seaborn**: For making attractive and informative data visualizations.

## Key Steps Performed

1.  **Data Loading**: The `Mall_Customers.csv` file was loaded into a Pandas DataFrame.
2.  **Data Preprocessing & Feature Selection**:
    * The `Annual Income (k$)` and `Spending Score (1-100)` columns were selected for clustering.
    * These features were standardized using `StandardScaler` to bring all features to a similar scale (mean ~ 0, standard deviation ~ 1). This is crucial for distance-based        algorithms like K-means.
3.  **Optimal K Value Finding (Elbow Method)**:
    * The Elbow Method was employed to find the best number of clusters (`K`) for the K-means algorithm.
    * WCSS (Within-Cluster Sum of Squares) was calculated for different `K` values (from 1 to 10), and a graph was plotted. The "elbow" point on the graph indicates the             optimal `K` value (in this case, `K=5` was chosen).
4.  **Applying K-means Clustering**:
    * The `KMeans` algorithm was applied to the scaled data using the identified `optimal_k` (5 clusters).
    * Each customer was assigned their respective cluster label (from `0` to `4`).
    * The **centroids** (average income and spending score) for each cluster were also calculated, representing the "center" of each group.
5.  **Visualization of Clusters**:
    * A scatter plot was created with `Annual Income` on the X-axis and `Spending Score` on the Y-axis.
    * Each customer is represented by a dot, and **different colors** are used to denote their assigned cluster.
    * The **centroids** of each cluster are marked with large **red 'X's**, clearly showing the average behavior of each group.

## Understanding the Output Graph

The graph provides a visual summary of your customer base:

* **X-axis (`Annual Income (k$)`)**: Shows the customer's annual income.
* **Y-axis (`Spending Score (1-100)`)**: Indicates how much a customer spends at the store (higher score = more spending).
* **Colored Dots**: Each dot is a customer. Dots of the same color belong to the same customer group.
* **Red 'X' (Centroids)**: This is the average point for each group. It helps you understand the typical characteristics (average income and spending) of customers within       that group.

By looking at the graph, you can easily identify different customer segments, such as:
* High Income, High Spending Customers
* Low Income, High Spending Customers
* High Income, Low Spending Customers
* Low Income, Low Spending Customers
* And customers with average income/spending.

## Real-World Applications & Benefits

Customer segmentation offers significant advantages for businesses:

* **Targeted Marketing**: Businesses can create specific marketing campaigns for each customer group. For example, exclusive offers for high-value customers, or budget-friendly discounts for price-sensitive shoppers.
* **Personalized Product Recommendations**: Customers can receive product suggestions tailored to their preferences, leading to increased sales.
* **Improved Customer Service**: Understanding the needs of each segment allows for better and more relevant customer support.
* **Resource Optimization**: Focusing marketing budgets on the right segments can lead to a better ROI (Return on Investment).
* **New Product Development**: Insights into segment needs can guide the development of new products or services.

## How to Run the Code

1.  **Clone this repository:**
    ```bash
    git clone [Your_GitHub_Repo_URL_Here]
    cd [Your_Repo_Name]
    ```
2.  **Install the required libraries:**
    ```bash
    pip install pandas scikit-learn matplotlib seaborn
    ```
3.  **Download the dataset:**
    * Make sure the `Mall_Customers.csv` file is in the same directory as your Python script.
4.  **Run the Python script:**
    ```bash
    python your_script_name.py
    ```
    (Replace `your_script_name.py` with the actual name of your Python file, e.g., `kmeans_segmentation.py`)

This will execute the clustering algorithm and display the Elbow Method graph followed by the final customer segmentation plot.

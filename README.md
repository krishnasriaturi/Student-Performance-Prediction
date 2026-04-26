<h1>Student Performance Prediction</h1>

<h2>Overview</h2>
<p>
This project presents a hybrid deep learning framework for predicting student performance in virtual learning environments.
The system combines an Enhanced Convolutional Neural Network (ECNN) with a ResNet architecture and integrates the
Butterfly Optimization Algorithm (BOA) for feature selection. The model analyzes academic and behavioral data to classify
student outcomes into Fail, Withdrawn, Pass, and Distinction.
</p>

<h2>Technology Stack</h2>
<ul>
  <li>Python</li>
  <li>TensorFlow / Keras</li>
  <li>Pandas and NumPy</li>
  <li>Streamlit</li>
  <li>Butterfly Optimization Algorithm (BOA)</li>
</ul>

<h2>Key Features</h2>
<ul>
  <li>Hybrid ECNN + ResNet based deep learning model</li>
  <li>BOA-based feature selection for improved efficiency</li>
  <li>Predicts student performance with confidence scores</li>
  <li>Interactive Streamlit dashboard</li>
  <li>File upload support for dataset and model</li>
  <li>Visualization of prediction probabilities</li>
</ul>

<h2>Model Architecture</h2>
<p>The proposed system uses a hybrid deep learning approach consisting of:</p>
<ul>
  <li>Enhanced Convolutional Neural Network (ECNN) for feature extraction</li>
  <li>ResNet architecture for capturing deep relationships and avoiding vanishing gradients</li>
  <li>Butterfly Optimization Algorithm (BOA) for selecting the most relevant features</li>
</ul>
<p>
This architecture enables the model to capture both simple and complex patterns in student behavior data.
</p>

<h2>Workflow</h2>
<ol>
  <li>Data Collection from OULAD dataset</li>
  <li>Data Preprocessing and normalization</li>
  <li>Feature Selection using BOA</li>
  <li>Model Training using ECNN + ResNet</li>
  <li>Prediction generation</li>
  <li>Evaluation and visualization</li>
</ol>

<h2>Dataset</h2>
<p>
The model is trained on the Open University Learning Analytics Dataset (OULAD), which includes:
</p>
<ul>
  <li>Student interaction data</li>
  <li>Assessment scores</li>
  <li>Clickstream activity</li>
  <li>Engagement metrics</li>
</ul>

<p>
<strong>Dataset:</strong><br>
<a href="https://drive.google.com/file/d/1vKIkvHa6J0EmBP8h9phvCd-xvPXD5Znn/view?usp=sharing">Download Dataset</a>
</p>

<p>
<strong>Model:</strong><br>
<a href="https://drive.google.com/file/d/1ALhD4ZC6m0dzzAK2dDwkubIiRB-Jv9BA/view?usp=sharing">Download Model</a>
</p>

<h2>Evaluation Metrics</h2>
<ul>
  <li>Accuracy</li>
  <li>Precision</li>
  <li>Recall</li>
  <li>F1 Score</li>
  <li>Confusion Matrix</li>
</ul>

<h2>Results</h2>
<ul>
  <li>Achieved approximately 91% accuracy</li>
  <li>Outperformed traditional machine learning models</li>
  <li>Demonstrated strong generalization with minimal overfitting</li>
  <li>Effectively identifies at-risk students early</li>
</ul>

<h2>Impact</h2>
<ul>
  <li>Enables early identification of at-risk students</li>
  <li>Supports timely intervention by educators</li>
  <li>Improves student retention and academic performance</li>
  <li>Facilitates data-driven decision making in education systems</li>
</ul>

<h2>How to Run</h2>
<ol>
  <li>Clone the repository</li>
  <li>Install dependencies:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li>Run the application:
    <pre><code>streamlit run App.py</code></pre>
  </li>
  <li>Upload the dataset and model using the sidebar</li>
</ol>

<h2>Notes</h2>
<ul>
  <li>Dataset and trained model are not included in the repository</li>
  <li>Download and upload both files before running predictions</li>
</ul>

<h2>Future Enhancements</h2>
<ul>
  <li>Integration of Explainable AI (XAI)</li>
  <li>Real-time student monitoring</li>
  <li>Deployment in educational platforms</li>
  <li>Personalized learning recommendations</li>
</ul>

<h2>Project Structure</h2>
<ul>
  <li>App.py – Streamlit application</li>
  <li>Main.py – Model execution script</li>
  <li>assets/ – Screenshots and visuals</li>
  <li>README.md – Project documentation</li>
</ul>

<h2>Authors</h2>
<ul>
  <li>A. Krishna Sri</li>
  <li>B. Nagaraju</li>
  <li>T. Dinesh</li>
  <li>R. Spandana</li>
</ul>

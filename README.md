# 🏗️ Concrete Strength Prediction

[![Streamlit App](https://img.shields.io/badge/Live%20Demo-Streamlit-brightgreen)](https://yanetniguse-concrete-strength-app-esbush.streamlit.app/)  
[![GitHub Repository](https://img.shields.io/badge/View%20on-GitHub-black)](https://github.com/yanetniguse/concrete_strength)  
[![Portfolio](https://img.shields.io/badge/Portfolio-Yanet%20Niguse-blue)](https://yanet-niguse-tesfay.vercel.app/)  

## 📌 Project Overview
**Concrete Strength Prediction** is a **Machine Learning (ML) application** that accurately predicts the compressive strength of concrete based on various material compositions. 

🎯 **Problem Statement:** Traditional concrete strength testing is time-consuming and costly. Engineers often rely on experimental data to determine optimal mixtures, leading to inefficiencies.

💡 **Solution:** By leveraging **Ridge & Lasso Regression**, we provide an ML-driven predictive model that helps engineers estimate concrete strength more efficiently, reducing material waste and improving construction quality.

## 🚀 Live Demo & Code
- **🔗 Try it now:** [Concrete Strength Prediction App](https://yanetniguse-concrete-strength-app-esbush.streamlit.app/)
- **📂 GitHub Repository:** [View Code](https://github.com/yanetniguse/concrete_strength)
- **📖 ML Training Notebook:** [Google Colab](https://colab.research.google.com/drive/1d8rFpiZDlpEJ2DoZfCPQq5sTdQerg_2H?usp=sharing)

![image](https://github.com/user-attachments/assets/dde397fb-5d5d-44ba-a359-b1ee6aab782b)


## 🧪 Machine Learning Analysis
### **1️⃣ Feature Selection & Importance**
- **Lasso Regression:** Selected the most impactful features: *cement, slag, fly ash, water, superplasticizer, fine aggregate, and age*.
- **Ridge Regression:** Kept all features but shrunk their impact to avoid overfitting.
- **Findings:** *Cement, Water, and Age* had the highest impact on concrete strength.

### **2️⃣ Model Performance**
- **Baseline Ridge Regression RMSE:** *9.80*
- **After Feature Selection (Lasso):** *9.82* → No significant improvement, meaning all features contribute meaningfully.
- **Final Decision:** Retained all features for Ridge Regression.

### **3️⃣ Key Takeaways & Next Steps**
✔️ **Feature selection didn’t significantly improve Ridge, confirming the importance of all variables.**
✔️ **Exploring non-linear models like XGBoost or Random Forest could improve accuracy.**
✔️ **Further feature engineering (e.g., PCA or ElasticNet Regression) might refine performance.**

## 💻 How to Run Locally
1. Clone the repository:  
   ```bash
   git clone https://github.com/yanetniguse/concrete_strength.git
   ```
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:  
   ```bash
   streamlit run app.py
   ```
📊 Analysis 

⚠️ Challenges Faced

1️⃣ Feature Selection Impact: Removing ‘coarse_agg’ (via Lasso Regression) did not improve Ridge Regression performance, highlighting the importance of all features.

2️⃣ Data Scaling: Without proper feature normalization, regression models performed inconsistently.

3️⃣ Overfitting Concerns: Ridge Regression shrunk coefficients to mitigate overfitting, but testing non-linear models could enhance performance.

4️⃣ Hyperparameter Tuning: Finding the best alpha (λ) for Ridge & Lasso required cross-validation to avoid bias.


🏆 Final Conclusion

Lasso Regression removed ‘coarse_agg’, but it did not improve Ridge Regression RMSE (9.80 → 9.82), confirming that all features contribute meaningfully.


Cement, Water, and Age had the highest impact on concrete strength.


Further improvements using non-linear models & additional data collection could enhance predictive power.


This ML model successfully demonstrates how AI can optimize concrete strength prediction, reducing manual testing time & material waste in construction.

## 🏆 About the Author
👩‍💻 **Yanet Niguse Tesfay** – A **Software Engineer & ML Enthusiast** passionate about AI-driven solutions for real-world problems.  
🔗 [Portfolio](https://yanet-niguse-tesfay.vercel.app/) | [LinkedIn](https://www.linkedin.com/in/yanetniguse7/)

---
📢 **Looking for collaborations, internships, or job opportunities?** Let’s connect! 🚀

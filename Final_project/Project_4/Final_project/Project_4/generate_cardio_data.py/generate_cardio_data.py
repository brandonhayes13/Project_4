# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
 
# Set random seed for reproducibility
np.random.seed(42)
 
def generate_cardio_data(num_records=7000):
    """
    Generate synthetic cardiovascular disease data focusing on key predictive factors:
    - Age
    - Systolic blood pressure
    - Diastolic blood pressure
    - BMI
    - Blood pressure category
    """
 
    # Generate age (in years)
    ages = np.random.randint(30, 70, num_records)
 
    # Generate systolic blood pressure with realistic ranges
    # Normal: 90-129
    # Stage 1: 130-139
    # Stage 2: 140-179
    # Critical: 180+
    base_systolic = np.random.normal(135, 20, num_records)
    systolic_bp = np.clip(base_systolic, 90, 200)
 
    # Generate diastolic blood pressure (correlated with systolic)
    # Normal: 60-79
    # Stage 1: 80-89
    # Stage 2: 90-109
    # Critical: 110+
    base_diastolic = np.random.normal(85, 10, num_records)
    diastolic_bp = np.clip(base_diastolic, 60, 120)
 
    # Calculate BMI with realistic ranges
    # Calculate height in meters (normal distribution around 1.7m)
    heights = np.random.normal(1.7, 0.1, num_records)
    # Calculate weight giving a BMI distribution centered around 25
    base_weights = heights**2 * np.random.normal(25, 5, num_records)
    bmis = base_weights / (heights**2)
 
    # Determine blood pressure categories based on both systolic and diastolic
    def get_bp_category(systolic, diastolic):
        if systolic < 120 and diastolic < 80:
            return 'Normal'
        elif systolic < 130 and diastolic < 80:
            return 'Elevated'
        elif systolic < 140 or diastolic < 90:
            return 'Stage 1 Hypertension'
        else:
            return 'Stage 2 Hypertension'
 
    bp_categories = [get_bp_category(s, d) for s, d in zip(systolic_bp, diastolic_bp)]
 
    # Calculate cardiovascular disease risk (target variable)
    def calculate_cardio_risk(age, systolic, diastolic, bmi):
        # Risk increases with:
        # - Higher age
        # - Higher blood pressure
        # - Higher BMI
        risk_score = (
            (age - 30) / 40 * 0.3 +  # Age contribution
            (systolic - 90) / 110 * 0.3 +  # Systolic contribution
            (diastolic - 60) / 50 * 0.2 +  # Diastolic contribution
            (bmi - 18.5) / 16.5 * 0.2  # BMI contribution
        )
        return 1 if risk_score > 0.5 else 0
 
    cardio_disease = [calculate_cardio_risk(a, s, d, b) 
                     for a, s, d, b in zip(ages, systolic_bp, diastolic_bp, bmis)]
 
    # Create DataFrame
    data = pd.DataFrame({
        'Age': ages,
        'Systolic_BP': systolic_bp.round(0),
        'Diastolic_BP': diastolic_bp.round(0),
        'BMI': bmis.round(2),
        'BP_Category': bp_categories,
        'Cardiovascular_Disease': cardio_disease
    })
 
    return data
 
def analyze_cardio_data(df):
    """Analyze and visualize cardiovascular disease data"""
 
    print("\nDataset Summary:")
    print(f"Total records: {len(df)}")
    print("\nDisease Distribution:")
    print(df['Cardiovascular_Disease'].value_counts(normalize=True))
    print("\nBlood Pressure Categories:")
    print(df['BP_Category'].value_counts())
 
    # Create visualizations
    plt.figure(figsize=(15, 5))
 
    # BP Distribution
    plt.subplot(1, 3, 1)
    df['BP_Category'].value_counts().plot(kind='bar')
    plt.title('Blood Pressure Category Distribution')
    plt.xticks(rotation=45)
 
    # BMI vs Blood Pressure
    plt.subplot(1, 3, 2)
    plt.scatter(df['BMI'], df['Systolic_BP'], c=df['Cardiovascular_Disease'], 
               alpha=0.5, cmap='coolwarm')
    plt.title('BMI vs Blood Pressure')
    plt.xlabel('BMI')
    plt.ylabel('Systolic BP')
 
    # Age Distribution by Disease Status
    plt.subplot(1, 3, 3)
    plt.hist([
        df[df['Cardiovascular_Disease'] == 0]['Age'],
        df[df['Cardiovascular_Disease'] == 1]['Age']
    ], label=['No Disease', 'Disease'])
    plt.title('Age Distribution by Disease Status')
    plt.legend()
 
    plt.tight_layout()
    plt.savefig('cardio_analysis.png')
    plt.close()
 
    # Save data
    df.to_csv('cardio_data.csv', index=False)
 
if __name__ == "__main__":
    df = generate_cardio_data()
    analyze_cardio_data(df)
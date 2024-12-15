# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
 
# Set random seed for reproducibility
np.random.seed(42)
 
def generate_mock_health_data(num_records=5000):
    # Lists for categorical data
    countries = ['USA', 'UK', 'France', 'Germany', 'Italy', 'Spain', 'Japan', 'China', 
                'India', 'Brazil', 'Canada', 'Australia', 'Russia', 'South Korea']
 
    diseases = {
        'Respiratory': ['COVID-19', 'Tuberculosis', 'Pneumonia', 'Bronchitis'],
        'Cardiovascular': ['Heart Disease', 'Hypertension', 'Stroke'],
        'Infectious': ['Malaria', 'HIV', 'Hepatitis', 'Influenza'],
        'Chronic': ['Diabetes', 'Cancer', 'Arthritis'],
        'Neurological': ['Alzheimer\'s', 'Parkinson\'s', 'Multiple Sclerosis']
    }
 
    age_groups = ['0-18', '19-35', '36-50', '51-65', '65+']
    genders = ['Male', 'Female', 'Other']
    treatments = ['Medication', 'Surgery', 'Therapy', 'Vaccination', 'Combined']
 
    # Generate data
    data = {
        'Country': np.random.choice(countries, num_records),
        'Year': np.random.randint(2010, 2024, num_records),
        'Disease_Category': np.random.choice(list(diseases.keys()), num_records)
    }
 
    # Generate disease names based on categories
    data['Disease_Name'] = [np.random.choice(diseases[cat]) for cat in data['Disease_Category']]
 
    # Generate other fields with realistic ranges
    data.update({
        'Prevalence_Rate': np.random.uniform(0.1, 15.0, num_records),
        'Incidence_Rate': np.random.uniform(0.1, 10.0, num_records),
        'Mortality_Rate': np.random.uniform(0.1, 8.0, num_records),
        'Age_Group': np.random.choice(age_groups, num_records),
        'Gender': np.random.choice(genders, num_records),
        'Population_Affected': np.random.randint(1000, 1000000, num_records),
        'Healthcare_Access': np.random.uniform(40.0, 99.0, num_records),
        'Doctors_Per_1000': np.random.uniform(1.0, 10.0, num_records),
        'Hospital_Beds_Per_1000': np.random.uniform(1.0, 15.0, num_records),
        'Treatment_Type': np.random.choice(treatments, num_records),
        'Avg_Treatment_Cost_USD': np.random.uniform(100, 50000, num_records),
        'Availability_of_Vaccines_Treatment': np.random.choice(['Yes', 'No'], num_records),
        'Recovery_Rate': np.random.uniform(50.0, 99.0, num_records),
        'DALYs': np.random.uniform(100, 10000, num_records),
        'Improvement_in_5_Years': np.random.uniform(-5.0, 20.0, num_records),
        'Per_Capita_Income_USD': np.random.uniform(5000, 80000, num_records),
        'Education_Index': np.random.uniform(0.3, 0.9, num_records),
        'Urbanization_Rate': np.random.uniform(40.0, 95.0, num_records)
    })
 
    return pd.DataFrame(data)
 
def analyze_and_visualize_data(df):
    # Print basic statistics
    print("\nDataset Overview:")
    print(f"Total records: {len(df)}")
    print("\nBasic Statistics for Numerical Columns:")
    print(df.describe())
 
    # Disease category distribution
    print("\nDisease Category Distribution:")
    print(df['Disease_Category'].value_counts())
 
    # Create visualizations
    plt.figure(figsize=(12, 6))
    df['Disease_Category'].value_counts().plot(kind='bar')
    plt.title('Distribution of Disease Categories')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('disease_distribution.png')
    plt.close()
 
    # Healthcare vs Recovery Rate
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Healthcare_Access'], df['Recovery_Rate'], alpha=0.5)
    plt.xlabel('Healthcare Access (%)')
    plt.ylabel('Recovery Rate (%)')
    plt.title('Healthcare Access vs. Recovery Rate')
    plt.tight_layout()
    plt.savefig('healthcare_recovery.png')
    plt.close()
 
    # Save data to CSV
    df.to_csv('mock_health_data.csv', index=False)
    print("\nData has been saved to 'mock_health_data.csv'")
    print("Visualizations have been saved as PNG files")
 
if __name__ == "__main__":
    # Generate mock data
    print("Generating mock health data...")
    df = generate_mock_health_data()
 
    # Analyze and visualize
    analyze_and_visualize_data(df)
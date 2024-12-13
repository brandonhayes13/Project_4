from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/project4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Basic route to test the app 
@app.route('/') 
def hello(): 
    return "Hello, welcome to our homepage for Project 4!" 

# Define the HealthStatistics model
class healthstatistics(db.Model):
    __tablename__ = 'healthstatistics'
    
    # Add a primary key column
    id = db.Column(db.Integer, primary_key=True)
    
    #columns
    country = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    disease_name = db.Column(db.String(150), nullable=False)
    disease_category = db.Column(db.String(100), nullable=False)
    prevalence_rate = db.Column(db.Float, nullable=True)
    incidence_rate = db.Column(db.Float, nullable=True)
    mortality_rate = db.Column(db.Float, nullable=True)
    age_group = db.Column(db.String(50), nullable=True)
    gender = db.Column(db.String(10), nullable=True)
    population_affected = db.Column(db.BigInteger, nullable=True)
    healthcare_access = db.Column(db.Float, nullable=True)
    doctors_per_1000 = db.Column(db.Float, nullable=True)
    hospital_beds_per_1000 = db.Column(db.Float, nullable=True)
    treatment_type = db.Column(db.String(150), nullable=True)
    avg_treatment_cost_usd = db.Column(db.Float, nullable=True)
    availability_of_vaccines_treatment = db.Column(db.String(10), nullable=True)
    recovery_rate = db.Column(db.Float, nullable=True)
    dalys = db.Column(db.Float, nullable=True)
    improvement_in_5_years = db.Column(db.Float, nullable=True)
    per_capita_income_usd = db.Column(db.Float, nullable=True)
    education_index = db.Column(db.Float, nullable=True)
    urbanization_rate = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return f"<HealthStatistics {self.Country}, {self.Disease_Name}>"

# Route to display all records
@app.route('/data')
def show_data():
    records = healthstatistics.query.limit(100).all()
    data = [
        {
            "Country": record.country,
            "Year": record.year,
            "Disease_Name": record.disease_name,
            "Disease_Category": record.disease_category,
            "Prevalence_Rate": record.prevalence_rate,
            "Incidence_Rate": record.incidence_rate,
            "Mortality_Rate": record.mortality_rate,
            "Age_Group": record.age_group,
            "Gender": record.gender,
            "Population_Affected": record.population_affected,
            "Healthcare_Access": record.healthcare_access,
            "Doctors_Per_1000": record.doctors_per_1000,
            "Hospital_Beds_Per_1000": record.hospital_beds_per_1000,
            "Treatment_Type": record.treatment_type,
            "Avg_Treatment_Cost_USD": record.avg_treatment_cost_usd,
            "Availability_of_Vaccines_Treatment": record.availability_of_vaccines_treatment,
            "Recovery_Rate": record.recovery_rate,
            "DALYs": record.dalys,
            "Improvement_in_5_Years": record.improvement_in_5_years,
            "Per_Capita_Income_USD": record.per_capita_income_usd,
            "Education_Index": record.education_index,
            "Urbanization_Rate": record.urbanization_rate,
        }
        for record in records
    ]
    return jsonify(data)

# Create the database tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)


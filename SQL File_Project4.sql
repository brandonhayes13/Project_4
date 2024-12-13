CREATE TABLE HealthStatistics (
    Country VARCHAR(100),
    Year INT,
    Disease_Name VARCHAR(150),
    Disease_Category VARCHAR(100),
    Prevalence_Rate DECIMAL(5, 2), -- percentage with up to 2 decimal places
    Incidence_Rate DECIMAL(5, 2),
    Mortality_Rate DECIMAL(5, 2),
    Age_Group VARCHAR(50),
    Gender VARCHAR(10),
    Population_Affected BIGINT,
    Healthcare_Access DECIMAL(5, 2), -- percentage
    Doctors_Per_1000 DECIMAL(5, 2),
    Hospital_Beds_Per_1000 DECIMAL(5, 2),
    Treatment_Type VARCHAR(150),
    Avg_Treatment_Cost_USD DECIMAL(10, 2), -- cost in USD with two decimal precision
    Availability_of_Vaccines_Treatment VARCHAR(10), -- Yes/No
    Recovery_Rate DECIMAL(5, 2), -- percentage
    DALYs DECIMAL(10, 2), -- Disability-Adjusted Life Years
    Improvement_in_5_Years DECIMAL(5, 2), -- percentage
    Per_Capita_Income_USD DECIMAL(10, 2),
    Education_Index DECIMAL(5, 3), -- index values typically range from 0 to 1
    Urbanization_Rate DECIMAL(5, 2) -- percentage
);

SELECT * FROM HealthStatistics;

ALTER TABLE HealthStatistics
ADD COLUMN id SERIAL PRIMARY KEY;
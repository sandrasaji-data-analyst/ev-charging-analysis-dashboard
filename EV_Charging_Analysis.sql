CREATE DATABASE ev_charging_analysis;
USE ev_charging_analysis;

SELECT *
FROM ev_charging_cleaned;
SELECT COUNT(*) AS total_records
FROM ev_charging_cleaned;

#Identify missing values, duplicates and incorrect records
SELECT *
FROM ev_charging_cleaned
WHERE 'User ID' IS NULL;

#Average Charging Duration by Charger Type
SELECT
    `Charger Type`,
    ROUND(AVG(`Charging Duration (hours)`), 2)
    AS avg_duration
FROM ev_charging_cleaned
GROUP BY `Charger Type`;

SELECT *
FROM ev_charging_cleaned
WHERE `Charging Cost (USD)` > 50;

SELECT
    `Charger Type`,
    COUNT(*) AS total_sessions
FROM ev_charging_cleaned
GROUP BY `Charger Type`;

-- 8.2 Unique Users by User Type
SELECT
    `User Type`,
    COUNT(DISTINCT `User ID`) AS unique_users
FROM ev_charging_cleaned
GROUP BY `User Type`;

#Charging Sessions by Location
SELECT
    `Charging Station Location`,
    COUNT(*) AS total_sessions
FROM ev_charging_cleaned
GROUP BY `Charging Station Location`
ORDER BY total_sessions DESC;

#Top 3 Most Used Charging Stations
SELECT
    `Charging Station ID`,
    `Charging Station Location`,
    COUNT(*) AS total_sessions
FROM ev_charging_cleaned
GROUP BY
    `Charging Station ID`,
    `Charging Station Location`
ORDER BY total_sessions DESC
LIMIT 3;

#Charging Sessions by Charger Type
SELECT
    `Charger Type`,
    COUNT(*) AS total_sessions
FROM ev_charging_cleaned
GROUP BY `Charger Type`
ORDER BY total_sessions DESC;
-- Insert Data
-- Insert all the ConferenceDivision data (8 rows)
-- Insert team data for AFC North (4 rows)

INSERT INTO ConferenceDivision (ConferenceDivisionID, Division, Conference)
VALUES
(1, 'East', 'AFC'),
(2, 'North', 'AFC'),
(3, 'South', 'AFC'),
(4, 'West', 'AFC'),
(5, 'East', 'NFC'),
(6, 'North', 'NFC'),
(7, 'South', 'NFC'),
(8, 'West', 'NFC');

INSERT INTO Team (Team_id, TeamName, TeamCityState, TeamColors, ConferenceDivisionID)
VALUES
(1, 'Baltimore Ravens', 'Baltimore', 'Purple', 'Black', 2)
(2, 'Cincinnati Bengals', 'Cincinnati', 'Black', 'Orange', 2),
(3, 'Cleveland Browns', 'Cleveland', 'Brown', 'Orange', 2),
(4, 'Pittsburgh Steelers', 'Pittsburgh', 'Black', 'Yellow', 2);

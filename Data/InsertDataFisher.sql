-- Insert Data
-- Insert all the ConferenceDivision data (8 rows)
-- Insert team data for AFC North (4 rows)

use NFL_RDB_Fisher;

INSERT INTO ConferenceDivision (Division, Conference)
VALUES
('East', 'AFC'),
('North', 'AFC'),
('South', 'AFC'),
('West', 'AFC'),
('East', 'NFC'),
('North', 'NFC'),
('South', 'NFC'),
('West', 'NFC');
GO

select * from ConferenceDivision;
GO

INSERT INTO Team (TeamName, TeamCityState, TeamColors, ConferenceDivisionID)
VALUES
('Baltimore Ravens', 'Baltimore, MD', 'Purple, Black', 2),
('Cincinnati Bengals', 'Cincinnati, OH', 'Black, Orange', 2),
('Cleveland Browns', 'Cleveland, OH', 'Brown, Orange', 2),
('Pittsburgh Steelers', 'Pittsburgh, PA', 'Black, Yellow', 2),

('Houston Texans', 'Houston, TX', 'Deep Steel Blue, Battle Red, Liberty White', 3),
('Indianapolis Colts', 'Indianapolis, IN', 'Speed Blue, White', 3),
('Jacksonville Jaguars', 'Jacksonville, FL', 'Teal, Black, Gold', 3),
('Tennessee Titans', 'Nashville, TN', 'Titans Navy, Titans Light Blue, Titans Red', 3),

('Buffalo Bills', 'Buffalo, NY', 'Royal Blue, Red, White', 1),
('Miami Dolphins', 'Miami, FL', 'Aqua, Orange', 1),
('New England Patriots', 'Foxborough, MA', 'Navy Blue, Red, Silver', 1),
('New York Jets', 'East Rutherford, NJ', 'Gotham Green, White', 1),

('Denver Broncos', 'Denver, CO', 'Orange, Navy Blue', 4),
('Kansas City Chiefs', 'Kansas City, MO', 'Red, Gold', 4),
('Las Vegas Raiders', 'Las Vegas, NV', 'Silver, Black', 4),
('Los Angeles Chargers', 'Los Angeles, CA', 'Powder Blue, Gold', 4),

('Chicago Bears', 'Chicago, IL', 'Navy Blue, Orange', 6),
('Detroit Lions', 'Detroit, MI', 'Honolulu Blue, Silver', 6),
('Green Bay Packers', 'Green Bay, WI', 'Green, Gold', 6),
('Minnesota Vikings', 'Minneapolis, MN', 'Purple, Gold', 6),

('Atlanta Falcons', 'Atlanta, GA', 'Red, Black', 5),
('Carolina Panthers', 'Charlotte, NC', 'Black, Panther Blue, Silver', 5),
('New Orleans Saints', 'New Orleans, LA', 'Black, Old Gold', 5),
('Tampa Bay Buccaneers', 'Tampa, FL', 'Red, Pewter, Black', 5),

('Arizona Cardinals', 'Phoenix, AZ', 'Cardinal Red, White', 8),
('Los Angeles Rams', 'Los Angeles, CA', 'Royal Blue, Yellow Gold', 8),
('San Francisco 49ers', 'San Francisco, CA', 'Red, Gold', 8),
('Seattle Seahawks', 'Seattle, WA', 'College Navy, Action Green, Wolf Grey', 8);
GO


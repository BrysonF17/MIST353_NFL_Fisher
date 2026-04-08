-- Insert Data
-- Insert all the ConferenceDivision data (8 rows)
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

-- Insert team data
INSERT INTO Team (TeamName, TeamCityState, TeamColors, ConferenceDivisionID)
VALUES
-- AFC East
('Buffalo Bills', 'Buffalo, NY', 'Royal Blue, Red, White', 1),
('Miami Dolphins', 'Miami, FL', 'Aqua, Orange', 1),
('New England Patriots', 'Foxborough, MA', 'Navy Blue, Red, Silver', 1),
('New York Jets', 'East Rutherford, NJ', 'Gotham Green, White', 1),
-- AFC North
('Baltimore Ravens', 'Baltimore, MD', 'Purple, Black', 2),
('Cincinnati Bengals', 'Cincinnati, OH', 'Black, Orange', 2),
('Cleveland Browns', 'Cleveland, OH', 'Brown, Orange', 2),
('Pittsburgh Steelers', 'Pittsburgh, PA', 'Black, Yellow', 2),
-- AFC South
('Houston Texans', 'Houston, TX', 'Deep Steel Blue, Battle Red, Liberty White', 3),
('Indianapolis Colts', 'Indianapolis, IN', 'Speed Blue, White', 3),
('Jacksonville Jaguars', 'Jacksonville, FL', 'Teal, Black, Gold', 3),
('Tennessee Titans', 'Nashville, TN', 'Titans Navy, Titans Light Blue, Titans Red', 3),
-- AFC West
('Denver Broncos', 'Denver, CO', 'Orange, Navy Blue', 4),
('Kansas City Chiefs', 'Kansas City, MO', 'Red, Gold', 4),
('Las Vegas Raiders', 'Las Vegas, NV', 'Silver, Black', 4),
('Los Angeles Chargers', 'Los Angeles, CA', 'Powder Blue, Gold', 4),
-- NFC East
('Dallas Cowboys', 'Dallas, TX', 'Navy Blue, Silver', 5),
('New York Giants', 'East Rutherford, NJ', 'Blue, Red, White', 5),
('Philadelphia Eagles', 'Philadelphia, PA', 'Green, Silver, Black', 5),
('Washington Commanders', 'Landover, MD', 'Burgundy, Gold', 5),
-- NFC North
('Chicago Bears', 'Chicago, IL', 'Navy Blue, Orange', 6),
('Detroit Lions', 'Detroit, MI', 'Honolulu Blue, Silver', 6),
('Green Bay Packers', 'Green Bay, WI', 'Green, Gold', 6),
('Minnesota Vikings', 'Minneapolis, MN', 'Purple, Gold', 6),
-- NFC South
('Atlanta Falcons', 'Atlanta, GA', 'Red, Black', 7),
('Carolina Panthers', 'Charlotte, NC', 'Black, Panther Blue, Silver', 7),
('New Orleans Saints', 'New Orleans, LA', 'Black, Old Gold', 7),
('Tampa Bay Buccaneers', 'Tampa, FL', 'Red, Pewter, Black', 7),
-- NFC West
('Arizona Cardinals', 'Phoenix, AZ', 'Cardinal Red, White', 8),
('Los Angeles Rams', 'Los Angeles, CA', 'Royal Blue, Yellow Gold', 8),
('San Francisco 49ers', 'San Francisco, CA', 'Red, Gold', 8),
('Seattle Seahawks', 'Seattle, WA', 'College Navy, Action Green, Wolf Grey', 8);
GO

GO
insert into AppUser (Firstname, Lastname, Email, Phone, PasswordHash, UserRole)
VALUES
('Tom', 'Brady', 'tom.brady@example.com', '555-1234', 0x01, N'NFLFan'),
('Aaron', 'Rodgers', 'aaron.rodgers@example.com', '555-9012', 0x01, N'NFLFan'),
('Drew', 'Brees', 'drew.brees@example.com', '555-2222', 0x01, N'NFLFan'),
('Patrick', 'Mahomes', 'patrick.mahomes@example.com', '555-7890', 0x01, N'NFLFan'),
('Bill', 'Belichick', 'bill.belichick@example.com', '555-5678', 0x01, N'NFLAdmin'),
('Sean', 'McVay', 'sean.mcay@example.com', '555-3456', 0x01, N'NFLAdmin'),
('Mike', 'Tomlin', 'mike.tomlin@example.com', '555-1111', 0x01, N'NFLAdmin'),
('Andy', 'Reid', 'andy.reid@example.com', '555-3333', 0x01, N'NFLAdmin');
GO
insert into NFLFan (NFLFanID)
VALUES
(1),
(2),
(3),
(4);
GO
insert into NFLAdmin (NFLAdminID)
VALUES
(5),
(6),
(7),
(8);
GO
--select * from Team;
insert into FanTeam (NFLFanID, TeamID, PrimaryTeam)
VALUES
(1, 11, 1),
(1, 24, 0), -- Tom Brady is a fan of New England Patriots and Tampa Bay Buccaneers, but Patriots is his primary team
(2, 19, 1),
(2, 12, 0),
(2, 4, 0),-- Aaron Rodgers is a fan of Green Bay Packers, New York Jets, and Pittsburgh Steelers, but Packers is his primary team
(3, 3, 1), -- Drew Brees is a fan New Orleans Saints (primary) and Los Angeles Chargers
(3, 16, 0),
(4, 14, 1); -- Patrick Mahomes is a fan of Kansas City Chiefs (primary)


-- Create a database for NFL app
--use master;
--Create DATABASE NFL_RDB_Fisher;
-- Create tables for first itteration 

use NFL_RDB_Fisher;
GO

IF OBJECT_ID('Team', 'U') IS NOT NULL
    DROP TABLE Team;
GO
IF OBJECT_ID('ConferenceDivision', 'U') IS NOT NULL
    DROP TABLE ConferenceDivision;
GO

Create TABLE ConferenceDivision (
    ConferenceDivisionID INT IDENTITY(1,1)
        constraint PK_ConferenceDivision PRIMARY KEY,
    Conference NVARCHAR (50) NOT NULL
        CONSTRAINT CK_ConferenceNames CHECK (Conference IN ('AFC', 'NFC')),
    Division NVARCHAR(50) NOT NULL
        constraint CK_DivisionNames CHECK(Division IN ('East', 'North', 'South', 'West')),
        CONSTRAINT UK_ConferenceDivision UNIQUE (Conference, Division)
);

/*
alter TABLE ConferenceDivision
    NOCHECK CONSTRAINT CK_ConferenceNames;

    alter TABLE ConferenceDivision
    CHECK CONSTRAINT CK_ConferenceNames;
*/
GO

create TABLE Team (
    Team_id int IDENTITY(1,1)
        CONSTRAINT PK_Team PRIMARY KEY,
    TeamName NVARCHAR(50) NOT NULL,
    TeamCityState NVARCHAR(50) NOT NULL,
    TeamColors NVARCHAR(50) not null,
    ConferenceDivisionID INT NOT NULL,
        CONSTRAINT FK_TEAM_ConferenceDivision FOREIGN KEY (ConferenceDivisionID) REFERENCES ConferenceDivision(ConferenceDivisionID)
);

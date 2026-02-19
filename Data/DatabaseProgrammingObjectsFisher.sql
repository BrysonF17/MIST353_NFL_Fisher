-- 3 qureies 
-- 1 each for ConferenceDivision and team tables, and 1 join query


-- Lists all the different coferences and divisions
select CD.Conference, CD.Division
from ConferenceDivision as CD
order by CD.Conference, CD.Division;

-- Gets all the teams with their city, state, and colors
Select T.TeamName, T.TeamCityState, T.TeamColors
from Team as T
order by T.TeamName;


-- Shows each team with their division and conference.
select T.TeamName, CD.Conference, CD.Division
from Team as T
inner join ConferenceDivision as CD on T.ConferenceDivisionID = CD.ConferenceDivisionID
order by CD.Conference, CD.Division;
-- Perform an INNER JOIN on the two tables
SELECT players.first_name, players.last_name, players.hand, matches.loser_rank
FROM matches
INNER JOIN players ON
players.player_id=matches.loser_id;

-- Alternative solution:
-- Perform an INNER JOIN on the two tables
SELECT p.first_name, p.last_name, p.hand, m.loser_rank
FROM matches AS m
INNER JOIN players AS p ON
p.player_id=m.loser_id;

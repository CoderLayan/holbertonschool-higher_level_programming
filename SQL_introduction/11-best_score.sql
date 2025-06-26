-- Lists records with score >= 10 from second_table
-- Displays score and name, ordered by score (highest first)
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;

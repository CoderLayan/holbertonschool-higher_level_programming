-- Lists all records of second_table with non-null names
-- Displaying score and name, ordered by descending score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;

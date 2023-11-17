-- Retrieves all genres associated with the TV show 'Dexter' from the 'hbtn_0d_tvshows' database.
-- The query joins the 'tv_genres' and 'tv_show_genres' tables based on genre IDs, 
-- and the 'tv_shows' table based on show IDs. Results are ordered alphabetically by genre name.
SELECT tv_genres.name
FROM tv_genres 
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id 
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = "Dexter"
ORDER BY tv_genres.name;

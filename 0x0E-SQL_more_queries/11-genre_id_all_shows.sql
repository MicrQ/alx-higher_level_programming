-- a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- If a show doesn’t have a genre, display NULL
SELECT t.title, g.genre_id
FROM `tv_shows` AS t LEFT JOIN `tv_show_genres` AS g
ON t.id = g.show_id ORDER BY t.title, g.genre_id;

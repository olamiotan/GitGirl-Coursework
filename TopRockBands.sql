--Names of top 10 rock bands
SELECT ar.Name AS ArtistName, COUNT(t.TrackId) AS TrackCount FROM tracks t
INNER JOIN albums al ON t.AlbumId = al.AlbumId
INNER JOIN artists ar ON al.ArtistId = ar.ArtistId
INNER JOIN genres g ON t.GenreId = g.GenreId
WHERE g.GenreId = 1 
GROUP BY al.ArtistId 
ORDER BY TrackCount DESC LIMIT 10

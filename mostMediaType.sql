select mt.Name, count(mt.MediaTypeId) AS Amount 
from media_types mt
inner join tracks t on mt.MediaTypeId = t.MediaTypeId
GROUP BY mt.MediaTypeId
ORDER BY Amount DESC;

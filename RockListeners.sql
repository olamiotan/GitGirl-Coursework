--Details of rock music listeners
SELECT DISTINCT c.Email, c.FirstName, c.LastName, g.name FROM customers c
INNER JOIN invoices i ON c.CustomerId = i.CustomerId
INNER JOIN invoice_items ii ON i.InvoiceId = ii.InvoiceId
INNER JOIN tracks t ON ii.TrackId = t.TrackId
INNER JOIN genres g ON t.GenreId = g.GenreId
WHERE g.Name = "Rock" ORDER BY c.Email

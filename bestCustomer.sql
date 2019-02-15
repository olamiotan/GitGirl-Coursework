SELECT (c.FirstName || " " || c.LastName) As CustomerName, round(sum(i.Total),2) As AmountSpent FROM invoices i
inner join customers c on i.CustomerId = c.CustomerId
INNER JOIN invoice_items it ON i.InvoiceId = it.InvoiceId
group by c.FirstName, c.LastName
ORDER BY AmountSpent DESC
LIMIT 1;

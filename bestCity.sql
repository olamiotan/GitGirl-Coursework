SELECT BillingCity, round(sum(Total),2) as TotalInvoice
FROM invoices
group by BillingCity
ORDER by TotalInvoice DESC
limit 1;

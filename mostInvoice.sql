SELECT BillingCountry, sum(Total)as Invoices
FROM invoices
group by BillingCountry
order by Invoices Desc;

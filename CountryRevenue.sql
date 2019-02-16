SELECT BillingCountry, round(sum(Total),2) as Revenue
FROM invoices
group by BillingCountry
order by Revenue Desc;

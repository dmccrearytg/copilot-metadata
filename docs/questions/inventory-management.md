# Inventory Management

## Description

In the contemporary business environment mastering inventory management transcends mere necessity evolving into a strategic competitive advantage. Enterprises contend with a labyrinth of challenges including management of vast data volumes, intricate supply chain networks, and the critical need for real-time insights. Traditional inventory management approaches with their linear and static structures often stumble when confronted with the agility and depth demanded by this complexity.
In summary, as businesses confront the multifaceted challenges of inventory management in today's dynamic landscape TigerGraph offers a compelling solution with the ability to model complex relationships, deliver real-time insights, and adapt to change empowering organizations to turn inventory management into strategic advantage.

## Personas

```python
personas = [
    "Inventory Manager", 
    "Supply Chain Analyst", 
    "Procurement Specialist", 
    "Warehouse Supervisor", 
    "Business Intelligence Analyst", 
    "Data Analyst"]
```

## Persona Questions

### Persona: Inventory Manager 

1. What is the current stock level of [product name] in the inventory?
2. How many units of [product name] were sold in the last [time period]?
3. When is the next replenishment of [product name] scheduled?
4. What is the average sales velocity of [product name] in the last [time period]?
5. What is the current status of incoming shipment [shipment ID]?
6. Are there any backorders for [product name]?
7. How many units of [product name] have been damaged or returned in the last [time period]?
8. Can you project the optimal reorder point for [product name]?
9. What is the forecasted demand for [product name] in next [time period]?
10. What are the top-selling products in the [geographic location] for the last [time period]?
11. Are there any products that are about to expire in the next [time period]?
12. How much of [product name] was lost to waste or shrinkage in the last [time period]?
13. What is the oversupply risk for [product name] in the next [time period]?
14. Show me the inventory turnover rate for the last [time period].
15. Are there any flagged inventory discrepancies for [product name]?

### Persona: Supply Chain Analyst 

1. What is the current inventory level for [product name/item code] at [warehouse location]?
2. How many units of [product name/item code] were sold in the last [time period]?
3. What is the forecasted demand for [product name/item code] in the next [time period]?
4. When was the last time [product name/item code] was restocked at [warehouse location]?
5. What are the top-selling items in our inventory during the [time period]?
6. How many units of [product name/item code] should we order to meet the forecasted demand for the next [time period]?
7. Who is the supplier for [product name/item code]?
8. Are there any anticipated delivery delays from suppliers for [product name/item code] in the next [time period]?
9. What is the delivery status of our latest purchase order for [product name/item code]?
10. How often should we reorder the [product name/item code] so that we do not face stockout situations?
11. How many incoming orders are there in the pipeline for [product name/item code] including backorders?
12. Is there any critical stock level alerts for [product name/item code] at [warehouse location]?
13. What is the lead time for getting [product name/item code] from our supplier?
14. How much storage space is left in [warehouse location]?  
15. How many damaged/unsellable units of [product name/item code] were reported in the last [time period]?

### Persona: Procurement Specialist 

1. What is the current inventory level for [specific item]?
2. Can you update me on the status of [specific item] ordered from [supplier]?
3. Can you display the list of items that are running low in the inventory?
4. How many days' supply do we have left for [specific item]?
5. Can you forecast the demand for [specific item] over the next [time period]?
6. What are the most ordered items during [specific time period]?
7. Can you identify any potential issues in the supply chain for [specific item] or [specific supplier]?
8. Can you help me find the average order cycle time for [the specific supplier]?
9. What is the total value of our current inventory?
10. Could you show me the usage pattern of [specific item] over [specific time period]?
11. Can you generate a new order for [specific item] from [specific supplier]?
12. Can you predict the estimated delivery time for [specific item] from [specific supplier]?
13. Can you alert me when [specific item] reaches re-order level?
14. Can you display the trend chart for [specific item] sales over the [specific time frame]?
15. How has the cost of [specific item] fluctuated over the past [specific time period]?
16. What is the optimal order quantity for [specific item] to minimize cost and meet demand?
17. Could you generate a supply chain analysis report for the past [specific time period]?
18. What is the impact on the inventory if [specific item] supply is delayed by [specific time period]?
19. Can you compare the demand of [specific product] with [another specific product] over the [specific time period]?
20. Can you provide improvements suggestions for our inventory management regarding [particular issue or process]?

### Persona: Warehouse Supervisor 

1. What is the current status of our inventory? 
2. How many units of [product name] do we currently have in stock?
3. When was the last restock for [product name]?
4. What is the expiration date of [product name] in our inventory?
5. Show me the inventory turnover rate for [product name] for [time period].
6. What products have the lowest stock levels right now?
7. What products have the highest demand over the last [time period]?
8. Is there any product nearing its expiration date?
9. What was the total value of our inventory at the end of last [time period]?
10. What is the estimated time of arrival for our next shipment of [product name]?
11. Could you notify me when the stock levels of [product name] drop below [specified quantity]?
12. Which items have been in the inventory the longest?
13. In which [geographic location] are we experiencing the highest demand for our products?
14. Which suppliers have the shortest lead time for [product name]?
15. Can you generate a reorder report for the upcoming [time period]?

### Persona: Business Intelligence Analyst 

1. What is the current inventory status for [Product Name/ID]?
2. How many [Product Name/ID] do we have left in our [Geographic Location] warehouse?
3. Can you show me the sales trend of [Product Name/ID] over the [Time Period]?
4. How many [Product Name/ID] were sold in the [Time Period]?
5. Can you provide the demand forecast for [Product Name/ID] in the next [Time Period]?
6. Can you show me the supply chain network for [Product Name/ID]?
7. What was the average time for inventory turnover for [Product Name/ID] in the last [Time Period]?
8. What is the lead time for restocking [Product Name/ID]?
9. What's the current total cost of inventory for [Product Name/ID]?
10. Can you suggest any optimization strategies to improve inventory management for [Product Name/ID]?

### Persona: Data Analyst 

1. What is the current stock level of [product name] in [warehouse location]?
2. Can you generate a summary report of inventory across all [geographic locations] for the [time period]?
3. Could you show me the aging inventory report for [product category] in the [time period]?
4. What was the average inventory turnover ratio for [product name] in the [time period]?
5. Can you provide the out-of-stock history for [product name] within the [time period]?
6. What is the predicted stock level of [product name] in [warehouse location] for the next [time period]?
7. Can you show me a comparative analysis of inventory costs for [product category] from [start date] to [end date]?
8. How many [product name] do we need to reorder to maintain optimal inventory levels for the next [time period]?
9. Could you pull up the most frequently sold items in [geographic location] during the [time period]?
10. What is the trend of inventory shrinkage for [product category] over the [time period]?
11. Can you generate a vendor performance report for the [time period]? The report should include details like how often they delivered on time and the quality of the goods.
12. Can you provide a forecast of the demand for [product name] in [geographic location] for the next [time period]?
13. What were the top 5 best-selling products in [geographic location] during the [time period]?
14. What were the slow-moving products in [geographic location] during the [time period]?
15. Can you give me a breakdown of inventory holding costs for [product name] over the [time period]?
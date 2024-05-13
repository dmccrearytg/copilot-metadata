# Supply Chain Management

## Application Description

Supply chain management is full of dependencies: a product is the result of hundreds of upstream components and processes fulfilling their requirements.  Unfortunately, manufacturers (and other businesses that have multiple levels of inputs contributing to the final outputs) often cannot get basic reports on the bill of materials, timeliness and efficiency, because their information is spread across too many systems, or the systems are poor at working with dependencies.  A graph-based operational digital twin of a supply chain can solve these problems. The graph excels at modeling dependencies. Not only does it show you the current state of your supply chain (observability), but it can simulate operations, to help you respond agilely to shocks and to make preemptive changes to improve supply chain resiliency.
Observability and monitoring: 
Tracing impact and root causes: When a particular component/supply/region is disrupted and can't be fixed immediately, the business needs to be able to trace downstream to see what will be affected. A graph-based digital twin can show and report on downstream effects using a Directed Breadth-First Search.  Similarly, the digital twin can trace upstream to see what are the possible root causes of a defect.
Identifying alternatives: 
Assessing risks and improving resiliency: Supply change shocks and disruptions WILL occur, but well-prepared businesses work to minimize both the likelihood and impact of disruptions. Algorithms such as degree centrality and betweenness centrality can identify the riskiest stages of a supply chain.

## Personas

```python
personas = [
    'Supply Chain Manager', 
    'Operations Manager', 
    'Logistics Coordinator', 
    'Inventory Manager', 
    'Warehouse Manager', 
    'Purchasing Manager', 
    'Production Manager', 
    'Quality Assurance Manager', 
    'Top Management Executives']
```

## Persona Questions

### Persona: Supply Chain Manager 

1. What is the current status of our supply chain operations?
2. Can you show me a visual representation of our supply chain graph?
3. Are there any disruptions in the supply chain currently?
4. What is the impact of [specific disruption] on our supply chain operations?
5. What are the downstream effects if [specific component/supply/region] is disrupted?
6. What are the upstream causes for the defect in [specific component/supply]?
7. Can you suggest any alternative suppliers for [specific component/supply]?
8. How can we improve the resiliency of our supply chain?
9. What are the riskiest stages in our supply chain and how can we mitigate these risks?
10. What is the degree centrality of [specific stage] in our supply chain?
11. What is the betweenness centrality of [specific stage] in our supply chain?
12. Can you simulate our supply chain operations for [specific time period]?
13. What are the expected shocks or disruptions in the supply chain for [specific time period]?
14. What is the efficiency of our supply chain for [specific product]?
15. How can we increase the efficiency of [specific process] in our supply chain? 
16. Can you provide a detailed report on the bill of materials for [specific product]?
17. How will the lack of [specific input] affect our final output?
18. Can you help me optimize logistics for the supply chain in [specific region]?
19. Are there any supply chain issues that may affect the delivery of [specific product]?
20. Can we simulate potential strategies for better handling shocks and disruptions in the supply chain?

### Persona: Operations Manager 

1. What is the current status of our [specific supply chain component]?
2. Are there any disruptions detected in our supply chain [in a specific time period]?
3. Can you trace the possible root causes for the defects in [specific product]?
4. What will be the downstream effect if component/supply [specific component] is disrupted?
5. Can you suggest any alternative suppliers for [specific product or component]?
6. What were the total supply chain disruptions [in a specific time period]?
7. How can we reduce the risk at [specific supply chain stage]?
8. Can you provide a report on the timeliness and efficiency of [specific supply chain stage]?
9. What are the most vulnerable stages in our supply chain?
10. Can you simulate the supply chain operations under [specific scenario or condition]?
11. What are the impacts of disruptions in [geographic location] on our supply chain?
12. Can you provide a forecast for possible supply bottlenecks [in a specific time period]?
13. Which elements of our supply chain have the highest degree of dependency or centrality?
14. Can you provide a detailed analysis of our supply chain resiliency?
15. Can we compare our supply chain efficiency with [specific competitor or industry benchmark]?

### Persona: Logistics Coordinator 

1. What is the status of the shipment for [product name]?
2. When is the estimated time of arrival for the [product name] shipment?
3. How many units of [product name] are available in stock?
4. Are there any delays or disruptions in our [item name] supply chain?
5. Can you trace the root cause for the defect in [product name]?
6. Show me all alternative suppliers for [product name].
7. What are the potential downstream effects for the disruption in [product name] production?
8. How does the delay in [product's region of production] affect our supply chain?
9. Can you propose efficient routing options for the shipment of [product name]?
10. How can we improve the resiliency of our supply chain for [product name]?
11. What are the riskiest stages in our supply chain for [product name]?
12. What is the overall cost of the shipment for [product name]?
13. Are there any quality reports for [product name] in our inventory?
14. Can you run a simulation of operations for [product_name] based on projected demand [time period]?
15. What is the reorder point for [product name]?

### Persona: Inventory Manager 

1. What is the current status of our inventory for [specific product]?
2. Can you provide a breakdown of our stock levels for [geographic location]?
3. Are there any pending deliveries from our suppliers for [specific product or material]?
4. Can you generate a report on the demand forecast for [specific product] over the next [time period]?
5. What is the estimated arrival date for our shipment from [supplier]?
6. Could you provide a history of on-time deliveries by [specific supplier]?
7. How does the current stock level of [product] compare to the demand forecast for the next [time period]?
8. What are the potential risks or disruptions in our supply chain for [specific product or material]?
9. Can you predict the impact on our inventory if [specific supplier] is unable to fulfill their delivery for [time period]?
10. What alternative suppliers do we have in case of disruption with [current supplier]? 
11. What are the possible root causes of the current defect in [specific product]? 
12. Are there any upcoming maintenance schedules that could affect our inventory levels for [specific product]?
13. How resilient is our supply chain to potential disruptions in [specific region]?
14. Can you find the best transport route for delivering [product] to [destination]? 
15. What's the predicted inventory turnover rate for [specific product] over the next [time period]? 
16. Can you provide the degree centrality and betweenness centrality for [product/material] in our supply chain? 
17. What's the stock replenishment schedule for [specific product] at [geographic location]? 
18. What's the current utilization rate of our warehouse in [geographic location]?

### Persona: Warehouse Manager 

1. What is the current status of inventory in [specific warehouse location]?
2. Can you provide a report on the movement of [specific product] in [specific time period]?
3. Have there been any disruptions in the supply chain for [product or component]?
4. What are the possible downstream effects if [specific component/supply/region] is disrupted?
5. What are the possible root causes for the defect in [specific product]?
6. What are the alternative suppliers for [specific product]?
7. Could you highlight the riskiest stages in our supply chain?
8. How can we improve the resiliency of our supply chain?
9. Can you provide a list of products with low stock levels in [specific warehouse location]?
10. What is the lead time for [specific product] from [supplier]?
11. Can you generate a report on the weekly/monthly/yearly performance of [specific supplier]?
12. Do we have any outstanding orders with [specific supplier]?
13. Can you provide an overview of our warehouse capacity in [specific location or overall]?
14. Are there any anticipated disruptions to our supply based on recent trends or incidents?
15. What has been the turnover rate for [specific product] in our warehouse over the [specific time period]?

### Persona: Purchasing Manager 

1. What is the current status of [supplier's name] delivery?
2. Can you provide me with the list of alternative suppliers for [product name]?
3. How is the disruption in [region] affecting our supply chain?
4. What are the possible root causes of the delays in [product/component name] supply?
5. Can you show me the risk assessment for our key suppliers?
6. What are the most risk-prone stages in our supply chain for [product name]?
7. How can we improve the resiliency of our supply chain for [product/component name]?
8. What are the recommended actions to minimize the impact of disruptions from [supplier's name]?
9. Can you trace the impact of a delay in [component's name] on our final product delivery?
10. Can you provide a report on the timeliness and efficiency of [product name]'s supply chain over the [time period]?
11. Can I get the bill of materials for [product name]?
12. What's the level of inventory for [product/part name] in our warehouse [location]?
13. Can you provide a forecast of supply demand for the next [time period]?
14. Can you provide a list of our top [number] suppliers by volume/amount for [product name] in the past [time period]?
15. Can you provide a breakdown of [product name]'s manufacturing cost?

### Persona: Production Manager 

1. What is the current state of my supply chain across all regions?
2. Can you show the impact if [particular product/component] is disrupted?
3. What are the possible root causes of [specific defect] in our products?
4. What are the alternatives for [specific component] in the event of a supply chain disruption?
5. How could disruption in [specific region/supplier] affect our production line?
6. Can you provide a report on the efficiency of our supply chain operations over the last [time period]?
7. Based on our supply chain data, which stages are the riskiest?
8. What is the degree of centrality and betweenness centrality of [particular component/stage] in our supply chain?
9. How can we improve resilience in our supply chain to minimize both the likelihood and impact of disruptions?
10. What steps can we take to ensure timely delivery of [specific product] under current supply chain conditions?
11. How has the bill of material changed over [time period] for [specific product]?
12. How can we increase the efficiency of our supply chain for [specific product]?
13. How are our supply chain operations likely to be affected by [specific event/shock]?
14. What measures can be implemented to prevent [specific disruption] from happening again? 
15. Can you simulate the operations of our supply chain under [specific conditions/shocks]?

### Persona: Quality Assurance Manager 

1. What is the current state of [product/component] in the supply chain?
2. Is there any disruption at the [specific location/stage] of the supply chain?
3. What is the impact on the downstream if [product/component] is disrupted?
4. What could be the possible root causes of a defect in [product/component]?
5. Can you show the alternate routes for [product/component] delivery in the supply chain?
6. Are there any risk factors for [product/component] in the current supply chain setup?
7. How can we improve the resiliency of our supply chain for [product/component]?
8. What is the timeliness and efficiency report for [product/component] for the [time period]?
9. Is there any delay in the supply of [product/component] for the [time period]?
10. What are the most risk-prone stages for [product/component] in the supply chain?

### Persona: Top Management Executives 

1. What is the current status of our supply chain?
2. Can you show me the dependencies of [specific product] in the supply chain?
3. What is the impact of a disruption in [specific component/supply/region] on our production?
4. What are the possible root causes of a defect in [specific product]?
5. Can you identify alternatives for [specific disrupted component/supply] in our supply chain?
6. What are the riskiest stages in our supply chain?
7. How can we improve the resiliency of our supply chain?
8. What is the efficiency of our supply chain over [specific time period]?
9. Who are our top suppliers for [specific material/component]?
10. How can we reduce the likelihood and impact of disruptions in our supply chain?
11. How has [a recent event or decision] affected our supply chain?
12. What would be the potential impact if we change [specific process/component/supplier] in our supply chain?
13. Can you simulate the operation of our supply chain under [specific scenario]?
14. How can we increase the efficiency of our production for [specific product]?
15. Can you give me a report on the bill of materials for [specific product] over the last [specific time period]? 
16. How long does it take to produce [specific product] from start to finish?
17. Which component or process in our supply chain has the longest lead time?
18. What are the most significant costs in our supply chain for producing [specific product]?
19. How often do we experience supply chain disruptions? What is the most common cause?
20. Is there a bottleneck in our current supply chain? If so, where?
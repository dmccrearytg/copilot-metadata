# Investment Product Recommendations

## Application Description

Investment Product Recommendations empower leading financial companies to suggest highly relevant financial product offerings to their users. By modeling the complex relationships between assets, clients, and investment products as a graph financial companies can uncover hidden patterns and correlations that traditional databases miss. With TigerGraph's scalable and high-performance graph processing capabilities vast amounts of data can be analyzed in real-time, providing highly personalized investment recommendations that take into account each client's unique financial profile, risk tolerance, and investment goals. By leveraging TigerGraph's graph database financial companies can deliver unparalleled user experiences that drive client loyalty and growth while staying ahead of the competition.

## Personas

user_personas = [
    "Investment Advisors",
    "Financial Planners",
    "Asset Managers",
    "Wealth Managers",
    "Retail Bankers",
    "Insurance Advisors",
    "Private Bankers",
    "Retail Investors",
    "Institutional Investors",
    "Pension Fund Managers"
]

### Persona Questions

### Persona: Investment Advisors 

1. What is the predicted performance of [specific investment product]?
2. Can you show me the historical returns of [specific investment product] over the last [time period]?
3. Can you recommend investment products best suited for a client with [risk tolerance] and [investment goals]?
4. What are the trend changes in the portfolio value of [specific client] in the last [time period]?
5. Can you provide a comparison between [investment product 1] and [investment product 2] considering their risk level and returns?
6. What are the highest performing sectors over the [time period]?
7. What is the risk level of [specific investment product]?
8. Are there any investment product trends or patterns I should be aware of for [time period]?
9. How does [specific investment product] perform against its market benchmark?
10. Which type of clients are likely interested in [specific investment product] considering their risk tolerance and investment goals?
11. What are the potential impacts on [specific client]'s portfolio if we invest in [specific investment product]?
12. Can you suggest any alternative investment products for a client with a risk profile similar to [specific client]?
13. Provide a summary of the overall portfolio performance for [specific client] over the [time period].
14. Show me the investment products that have outperformed their market benchmarks over the [time period].
15. What are the top-performing investment products for risk profiles similar to [specific client]?



### Persona: Financial Planners 

1. What investment products would you recommend for a client with a [risk tolerance] and [investment goal]?
2. Could you provide details about the [specific investment product]?
3. Can you suggest products with a high return rate for a client with a [risk tolerance]?
4. What is the performance history for [investment product] over the past [time period]?
5. Is there any correlation between [investment product 1] and [investment product 2]?
6. What are the top investment products preferred by clients with [specific investment goal]?
7. What is the expected return on [investment product] over [time period]?
8. Can you suggest some low risk investment products for customers in the [age group] with [investment goal]?
9. How has [specific asset] performed relative to [investment product] over [time period]?
10. Can I get a risk analysis report for [investment product] over the last [time period]?
11. What are the tax implications for a client investing in [investment product]?
12. Can you provide a comparative analysis between [investment product 1] and [investment product 2] over [time period]?
13. Can you suggest investment products expected to perform well in the [geographic region]?
14. How diversified is the portfolio of a client who invested in [investment product]?
15. What are clients with a similar financial profile as [client's name] investing in recently?
16. What is the projected market outlook for [investment product] in the next [time period]?
17. Can you suggest investment products that align with a client's [personal values or interest] in addition to their [investment goal] and [risk tolerance]?
18. What are the liquidity options for [investment product]?
19. Can I get a thorough analysis of hidden patterns and correlations between different assets and investment products?  
20. What are some emerging investment products that could fit a client with [specific investment behaviour] and [investment goal]?



### Persona: Asset Managers 

1. What are the top-performing [type of financial product] over the [time period]?
2. Can you show me the risk analysis of the [specific financial product]?
3. Are there any untapped investment opportunities in the [geographic location]?
4. What are some suggested [type of financial products] for a client with [specific risk tolerance] and [specific investment goals]?
5. Can I get a comparison of the performance of these [list of financial products] over the [time period]?
6. Which financial products have the highest correlation over the [time period]? 
7. What are some recommended investment products for a portfolio of [portfolio size] with a [specific risk profile]?
8. What are the current market trends for [type of financial product] in [geographic location]?
9. How has [specific financial product] performed over the [time period]?
10. Could you project the performance of [specific financial product] over the next [time period] based on current market trends?
11. Which [type of financial product] are currently undervalued? 
12. What are the environmental, social, and governance (ESG) scores of [specific financial product]?
13. What is the volatility of [specific financial product] over the [time period]?
14. Are there any emerging market trends or risks I should be aware of in [type of financial product] or [geographic location]? 
15. Show me all the financial products that fit the risk profile of [specific client profile].



### Persona: Wealth Managers 

1. What investment opportunities are best for my client with a risk tolerance of [risk level] and investment goal of [goal]?
2. How are [specific asset or investment product] performing over the [time period]?
3. How well does my client [client name]’s current portfolio align with their financial profile [client financial profile]?
4. Can you suggest alternate investments similar to the performance of [specific asset or investment product]?
5. How has the investment market varied in the [geographic location] over the [time period]?
6. What are the investment trends of clients with a risk tolerance of [risk level] and investment goal of [goal]?
7. Can you provide financial product offerings that are popular among clients with [client profile or specific characteristics]?
8. What are the potential risks associated with the investment in [specific asset or investment product]?
9. How will the latest market trends in the [geographic location] impact the performance of [specific investment product or asset]?
10. What are the historical return rates for financial products within the risk spectrum of [risk level]?



### Persona: Retail Bankers 

1. What are the most favorable investment products for a client with [risk tolerance level]?
2. Could you provide a list of financial products suitable for [client's age group] with a [investment goal]?
3. How do I access the latest market trends and patterns for [specific asset]?
4. Can you predict the performance of [investment product] over the [time period]?
5. Can you suggest the best investment strategy for a client with [investment goal] and [risk tolerance]?
6. How can I match [specific investment product] with a client's unique [financial profile]?
7. How can we optimize our investment product offerings to better fit our clients' [gender, age, financial profile]?
8. Could you provide insight into the correlations between [asset type] and [investment product] in the [market environment]?
9. Can you analyze the historical performance of our [investment product] in real-time?
10. How can we improve our clients' user experience with tailored investment recommendations to meet their [financial goals]?



### Persona: Insurance Advisors 

1. What are the most suitable investment products for my client with [client's financial profile, risk tolerance, and investment goals]?
2. Can I view a graph analysis for [specific asset or investment]?
3. Can you analyze the performance of [specified asset or investment product] based on past [time period]?
4. How did [specific investment product] perform in the [specified geographical area]?
5. What are some investment products that have performed well in the same category as [specified investment product] over the past [specified time period]?
6. Can you show me a correlation graph that includes [asset or financial product]?
7. Provide a risk analysis for [specified investment product]?
8. Can you provide asset allocation recommendations for a client with [client's risk tolerance and investment goal]?
9. What's the predicted growth for [specified investment product] over the next [time period]?
10. How would an investment in [specified investment product] have performed if invested [specified number of years] ago?
11. Can you analyze the impact of [specific event] on the performance of [specific investment product]?
12. What investment products do we offer that are similar to [specified competitor's product]?



### Persona: Private Bankers 

1. What are the investment product recommendations for my client [client name]?
2. Can you provide a risk assessment for [investment product]?
3. What is the latest market information for [specific asset or investment product]?
4. How does [investment product] align with the risk profile of my client [client name]?
5. What is the performance of [investment product] over the last [time period]?
6. Can you suggest alternative investment products for my client [client name], given their risk tolerance and investment goals?
7. What are the potential returns for [investment product] over [time period]?
8. How are my clients' investments performing relative to the market [time period]?
9. What are some suitable investment products for a new client with a [risk tolerance level] risk tolerance?
10. Can you provide a summary of my client [client name]'s investment portfolio? 
11. Are there any relevant market updates or news for [investment product or asset]? 
12. Can you suggest any diversification options for my client [client name]?
13. What are the tax implications of investing in [investment product] for my client [client name]?
14. How have recent market events impacted the performance of [investment product]?
15. Can you compare the performance of [investment product] to [another investment product] over [time period]?



### Persona: Retail Investors 

1. What investment products do you recommend based on my [financial profile]?
2. What is the performance history of [specific investment product]?
3. Can you suggest investment products that match my [risk tolerance]?
4. Can you provide a list of the best-performing [investment product type] over the past [time period]?
5. How does [specific investment product] compare to other similar products in the market?
6. What are the potential risks and returns of investing in [specific investment product]?
7. Could you explain the terms and conditions of [specific investment product]?
8. Can you suggest investment products that align with my [investment goals]?
9. What alternative investment products can you recommend if I don't prefer [specific investment product]?
10. Can you give an overview of the current market trends for [investment product type]?
11. How does the current market condition affect the performance of [specific investment product]?
12. Are there any upcoming changes or new products in the [specific investment product type] category?
13. What is the minimum and maximum investment limit for [specific investment product]?
14. Can you suggest the best time to invest in [specific investment product] based on the market trends? 
15. Are there any additional benefits of investing in [specific investment product]?



### Persona: Institutional Investors 

1. What investment products do you recommend based on my [financial profile], [risk tolerance], and [investment goals]?
2. Can I get real-time analysis of my [investment portfolio]?
3. How does my current [portfolio of assets] correlate with other [investment products] on the market?
4. Can you suggest any adjustments to my [investment strategy] based on the projected [market trends]?
5. What are some overlooked [investment opportunities] that may be relevant in my case?
6. In which [geographic location] would you recommend to invest given my [financial plan] and [investment goals]?
7. How has the [investment product] performed over the [time period]?
8. What is the growth potential of my [investment product] based on the current [economic trends]?
9. Can you provide some insights on how my [investment product] compares against competitor [investment products] in [specific industry]?
10. What are the risk factors associated with my current [investment portfolio] that I should be aware of?
11. Considering my [risk tolerance], what changes do you suggest for my [investment portfolio] to achieve my [investment goals] over the [time period]?
12. Can this system analyze [investment data] in real-time to provide updates on my [investment portfolio performance]?
13. What kind of user experiences can I expect from using your application in managing my [investment portfolio]?
14. How secure is my [investor data] with this application? 
15. How can I leverage this application to stay ahead of the [investment market competition]?



### Persona: Pension Fund Managers 

1. What are the top performing [asset classes] over the [specified time period]?
2. How has the [specific investment product] performed over the [specified time period]?
3. What are the risk factors associated with [specific investment product]?
4. Can you provide portfolio recommendations based on a [specified risk tolerance]?
5. What are the most profitable investment products for pension funds in the [specified sector]?
6. Can you suggest some investment products with good returns for a [specified investment horizon]?
7. What are the trending investment products in the [specified geographic location]?
8. How does investing in [specific investment product] align with our current investment strategy?
9. Can you recommend some diversification strategies for our pension fund portfolio?
10. What are the projected returns for [specific investment product] over the [specified time period]?
11. What is the impact of recent market trends on our current investment portfolio?
12. Are there any recommended changes or tweaks needed for our current investment portfolio?
13. Can you analyse the correlations between [specified assets] in our portfolio?
14. What is the sector-wise distribution of our current investments?
15. What is the risk to reward ratio for the investment in [specific investment product]?
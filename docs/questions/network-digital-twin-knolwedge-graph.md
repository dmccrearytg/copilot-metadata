# Network Digital Twin Knowledge Graph

# Description

Cybersecurity is a crucial aspect of big organizations. Enterprises have their own data centers and their own network infrastructure involving a lot of devices. A well-planned attack can lead to serious issues, like data breach, corrupted files, and loss of data. Billions of dollars are lost each year due to cyberattacks.

TigerGraph allows you to connect data from different sources. Data at a scale of terabytes can be loaded into TigerGraph to give a comprehensive view of the network infrastructure of your organization. With visualizations in TigerGraph, users can gain a better visibility of the platform by seeing different components in their Network Infrastructure and tracing different paths leading from a suspicious device or IP address. Different graph algorithms can be run at scale and allows us to detect various kinds of cybersecurity attacks close to real-time. With TigerGraph, users can also extract graph features to Machine Learning models which has the potential to improve the accuracy of those models for tasks like anomaly detection.

## Personas

```python
 personas = [
    "Network Administrator", 
    "IT Manager", 
    "Data Analyst", 
    "IT Consultant", 
    "Threat Analyst", 
    "IT Auditor", 
    "Chief Information Officer", 
    "Research and Development Engineer",
     "Network Architect"]
```

## Persona Questions

### Persona: Network Administrator 

1. What devices are currently connected to our network infrastructure?
2. Are there any suspicious devices or IP addresses connected to our network?
3. What is the workload distribution across our servers over the past [time period]?
4. Have there been any significant changes in network traffic over [time period]?
5. What were the most recent attacks detected in our network?
6. Can you run a vulnerability scan on our network?
7. Show me a visualization of our current network infrastructure.
8. Are there any anomalies detected in our network over the past [time period]?
9. What graph algorithms have been run on our network data?
10. How has the accuracy of our Machine Learning models for anomaly detection changed over [time period]?
11. Could you show me the pathway leading from a certain [suspicious device or IP address] in our network?
12. How many potential cybersecurity threats have we detected in the last [time period]?
13. Show me the log of any failed login attempts over the past [time period]. 
14. Can you provide a report of the most frequent types of detected attacks on our network over the [time period]?
15. Have we had any data breaches in the past [time period]? How was the breach resolved?

### Persona: IT Manager 

1. What is the current status of our network infrastructure?
2. Have there been any unusual activities detected in our network in the [time period]?
3. Can you show me a detailed report of the security incidents occurred in the last [time period]?
4. Can you provide an overview of all the devices connected to our network?
5. How many data breaches have we had in the last [time period]?
6. What are the most common cybersecurity threats we've faced in the past [time period]?
7. Are there any devices in our network currently showing suspicious activity?
8. Which IP addresses have had the most security incidents in the past [time period]?
9. Can you show me the network path tracing from [specific device/IP]?
10. Have there been any significant changes in our network configuration recently?
11. What are the potential vulnerabilities or weak points in our current network infrastructure?
12. How have our cybersecurity countermeasures performed in the last [time period]?
13. How can we further improve our network security?
14. Can you provide a visualization of our network infrastructure?
15. What is the data load of our network infrastructure for the past [time period]?

### Persona: Data Analyst 

1. What is the total volume of data loaded into TigerGraph for [specified time period]?
2. Can you show me the visual representation of network infrastructure for [specified department]?
3. How many suspect devices or IP addresses were detected in the last [specified time period]?
4. Can you provide a list of all devices and IP addresses traced path from a suspicious device or IP address for [specified time period]?
5. Can I see the report of different kind of cybersecurity attacks detected in the last [specified time period]?
6. How many potential threats have been detected by our machine learning model for anomaly detection in [specified time period]?
7. Can you tell me the accuracy of our machine learning models for tasks like anomaly detection in the last [specified time period]?
8. What were the most common types of cyberattacks detected during [specified time period]?
9. How many data breaches occured in the last [specified time period]?
10. Can I see the monthly report of the total loss caused by cyberattacks during [specified year]?

### Persona: IT Consultant 

1. What is the current status of our [network infrastructure]?
2. Can you tell me the latest [cybersecurity attacks] detected in our infrastructure?
3. Can you identify any suspicious activities from [IP address]?
4. Can you identify any suspicious activities on [device name]?
5. Can you show me the data visualization of our [network infrastructure]?
6. What graph algorithms could we use to detect [specific type of cyberattack]?
7. Could you provide an update on the [Machine Learning model] accuracy for anomaly detection?
8. How much data in terabytes is currently loaded into our TigerGraph?
9. Can you show me the paths leading from the suspicious [device/IP address]?
10. What are the major sources of data feeding into our TigerGraph?
11. How quickly can TigerGraph detect a potential [type of cyberattack]?
12. Can this system identify and trace any unusual activities involving [specific device, IP address, or user ID]?
13. Can you provide a report on the recent [time period] cybersecurity incidents?
14. Can you assist in leveraging TigerGraph for our upcoming [migrating/anomaly detection] project? 
15. Can you help optimize our system to reduce the time taken for [cybersecurity attack detection]?

### Persona: Threat Analyst 

1. What were the most common types of cybersecurity threats detected in the network over the last [time period]?
2. How many suspected threats have been identified from [IP address]?
3. Can you provide a visualization of the network traffic from [specific device]?
4. What is the forecasted cyber risk for our network over the next [time period]?
5. Have there been any anomalies detected in the data traffic from [specific device] over the last [time period]?
6. How many cyber attacks have been detected from [geographical location] over [time period]?
7. What are various paths traced back from the suspicious [device/IP address]?
8. What were the top targeted devices in the network infrastructure over the last [time period]?
9. How has the activity pattern of [specific device] changed over [time period]?
10. Has the [specific device] been part of any cyber attacks in the past [time period]? If yes, can you provide the details of those attacks?
11. Can the machine learning model predict if there will be an anomaly in the data traffic from [specific device] in the next [time period]?
12. Are there any unsecured devices in our network infrastructure?

### Persona: IT Auditor 

1. What are the most common network vulnerabilities detected over the last [time period]?
2. Can I get a visualization of the current network infrastructure?
3. Show me a list of all devices connected to our network in the [geographic location].
4. What are the top most impacted sub-networks from the latest cyberattack?
5. Is there any suspicious activity traced back to device with IP address [IP address] in the last [time period]?
6. Are there any cybersecurity attacks that have been detected but not yet resolved?
7. How many data breaches occurred in the past [time period]?
8. Can I get a detailed report on the cyberattack that occurred on [specific date]?
9. What were the source and destination nodes involved in the data breach incident on [specific date]?
10. Can you predict the potential threats to our network during [time period] based on historical data?
11. What are the steps taken to prevent a similar cyber-attack that happened on [specific date]?
12. Compare the number of cybersecurity attacks between [specific time period] and [specific time period].
13. Show me the graph of IP addresses with suspicious activities in the past [time period].
14. Are there any patterns or anomalies noticed with the usage data of our network over the [time period]?
15. Which machine learning model will provide the most accurate predictions for anomaly detection based on our network data?

### Persona: Chief Information Officer 

1. What is the current status of our network infrastructure [time period]?
2. Can you provide an overview of the cybersecurity threats detected in [time period]?
3. What is the highest risk cybersecurity threat our infrastructure currently faces?
4. How many cyberattacks have been detected in the last [time period]?
5. Which devices or IP addresses have been identified as suspicious in the past [time period]?
6. Can you provide a visualization of the network infrastructure?
7. How does the Network Digital Twin Knowledge Graph work?
8. How effective has the TigerGraph been in identifying cyber threats in the last [time period]?
9. How accurate are the machine learning models in predicting anomaly detection?
10. How is our data protected in the Network Digital Twin Knowledge Graph?
11. How often is our network data updated in TigerGraph?
12. How can we improve the visibility of different components in our Network Infrastructure?
13. Can you provide a report on the various kinds of cybersecurity attacks detected in the last [time period]?
14. Are there any devices or IP addresses that need immediate attention?
15. Can you provide a progress report on the actions taken against the detected cyber threats in the last [time period]?

### Persona: Research and Development Engineer 

1. How can I load [data size] worth of data from different sources into TigerGraph in [time period]?
2. How does the visualization in TigerGraph work for enhancing the visibility of the platform for our network infrastructure?
3. How can I trace different paths leading from [specific device or IP address] in TigerGraph?
4. Can you run different graph algorithms at scale to detect [type of cybersecurity attack] in real-time using TigerGraph?
5. How can I extract graph features to Machine Learning models to improve the accuracy for tasks like anomaly detection in TigerGraph?
6. How is the data structured in the Network Digital Twin Knowledge Graph for [specific organization]?
7. How frequently does the data in Network Digital Twin Knowledge Graph update for [specific organization]?
8. Which graph algorithms are most effective for detecting [specific type of anomaly] in our network infrastructure using TigerGraph?
9. What type of visualizations does TigerGraph offer to help me better understand the network infrastructure of [specific organization]?
10. Can TigerGraph help to improve the accuracy of our [specific Machine Learning model] for anomaly detection in our network infrastructure?

### Persona: Network Architect 

1. What devices are connected to the [given IP address]?
2. Which users have been accessing device [device name] over the [selected time period]?
3. Has there been any suspicious activity reported on server [server name] within the [selected time period]?
4. When was the latest firmware update applied to device [device name]?
5. What is the current status of firewall [firewall id]?
6. What transport protocols are being used by device [device name]?
7. How much data has been transferred from device [device name] over the [selected time period]?
8. How many failed login attempts have been made on server [server name] within the [selected time period]?
9. Which devices have been communicating with IP address [given IP address] within the [selected time period]?
10. Which users have the highest data usage over the [selected time period]?
11. What is the most common type of activity on device [device name]?
12. Are there any unusual data transfers reported from IP address [given IP address] over the [selected time period]?
13. Who was the last user to log into the server [server name]?
14. What is the current network speed of device [device name]?
15. Can you generate a report of all activity from device [device name] over the [selected time period]?
16. How many devices are currently connected to the server [server name]?
17. What is the current upload/download speed of device [device name]?
18. How much total data has been transferred over the network within the [selected time period]?
19. What is the percentage of CPU utilization of device [device name]?
20. Can you provide an overview of the network topology?
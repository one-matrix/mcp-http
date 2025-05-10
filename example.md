# Large Model Interaction Example
"""
User: Please get the top 3 news from Baidu Hot Search.
AI: Calling http_request tool...
  ↳ Parameters:
     method=GET
     url=https://baidu.com/api/hotsearch
     headers={"Accept": "application/json"}
Response: Returns JSON data and automatically generates a summary:
     [
       {"title": "Shenzhou 18 Launch Successful", "heat": 9500000},
       {"title": "May Day Holiday Tourism Data Released", "heat": 8700000}
     ]
"""

User: Please get the HTML content of Baidu's homepage.
AI: Calling http_request tool...
   ↳ Parameters: method=GET, url=https://www.baidu.com
Response: Returns <html>...</html> and automatically renders


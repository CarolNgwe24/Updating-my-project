import mysql.connector
from typing import List, Dict, Any
class FinancialEngineBridge:
    """Connects your 2026_Sales database directly to your AI Agent Logic."""

def __init__(self) :
        self.host ="localhost"
        self.user = "root"
        self.password = "Masego24#"
        self.database = "2026 Sales"
        self.conn = self._connect_to_mysql()
        
def _connect_to_mysql(self):
            try:
                return mysql.connector.connect(
                    host=self.host, user=self.user,
                    password=self.password, database=self.database
                )
            except Exception as e:
                    raise ConnectionError( f"Database link failed: {str(e)}")
                    
def fetch_data_for_ai(self, sql_query: str, params: tuple =()) -> List:
    try:    
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute (sql_query, params)
        results  = cursor.fetchall()
        cursor.close()
        return results
    except  Exception as e:

     print (f"Error fetching data: {e}")
     return []
     
if __name__ == "__main__":
    bridge  = FinancialEngineBridge()
    print("Linked Python to your 2026_Sales Dashboard Database!")

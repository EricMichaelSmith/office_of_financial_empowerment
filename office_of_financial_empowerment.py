# -*- coding: utf-8 -*-
"""
Created on Sat May 31 15:33:02 2014

@author: Eric
"""

from __future__ import print_function
import MySQLdb
import sys

configLocalPathS = r'C:\E\Dropbox\Computing\Personal\sudointellectual\county_data_analysis'

sys.path.append(configLocalPathS)
import config_local
reload(config_local)



def main():
    """
    Loads the original MySQL Office of Financial Empowerment database and merges the counselor's form
    """
    
    # Pull data from original database
    con = MySQLdb.connect(user='root',
                          passwd=config_local.pwordS,
                          db='ofe')
    cur = con.cursor()
    cur.execute('SELECT last_name, first_name, ssn, language_spoken, email, phone1, phone2, banking, credit, debt, savings FROM clients')
    rows = cur.fetchall()    
    
    # Get counselor form input
    counselor_table_name = counselor_form_input()
    
    # Join databases
    mysql_s = """
        SELECT *
        FROM clients FULL OUTER JOIN {counselor_table_name}
        ON clients.ssn = {counselor_table_name}.ssn;
        """
    cur.execute(mysql_s.format(counselor_table_name=counselor_table_name))
    
    # Output results
    cur.execute('SELECT * FROM {table_name}'.format(table_name=counselor_table_name))
    rows = cur.fetchall()
    for row in rows:
        print(row)
        
    
    
def counselor_form_input():
    """
    Sample counselor form input
    """
    
    con = MySQLdb.connect(user='root',
                          passwd=config_local.pwordS,
                          db='ofe')
    cur = con.cursor()
    table_name = 'sample_form_input'
    cur.execute('DROP TABLE IF EXISTS {table_name}'.format(table_name=table_name))
    mysql_s = """
        CREATE TABLE {table_name}
        (
        ssn char(9) DEFAULT NULL,
        next_meeting_date date DEFAULT NULL,
        office_address char(75) DEFAULT NULL,
        grow_personal_income boolean DEFAULT NULL,
        bank_to_use char(50) DEFAULT NULL,
        bank_savings_per_month float(8, 2) DEFAULT NULL,
        deposit_goal float(8, 2) DEFAULT NULL,
        current_bank_name char(50) DEFAULT NULL,
        PRIMARY KEY (ssn)
        );
        """
    cur.execute(mysql_s.format(table_name=table_name))
    mysql_s = """
        INSERT INTO {table_name} (ssn, next_meeting_date, office_address, grow_personal_income, bank_to_use, bank_savings_per_month, deposit_goal, current_bank_name)
        VALUES ('123456789', '2014-06-04', '123 Office Place, Brooklyn, NY 12345', 1, NULL, NULL, 100, 'Bank Of America'),
               ('987654321', '2014-06-12', '123 Office Place, Brooklyn, NY 12345', 0, NULL, NULL, NULL, NULL),
               ('271828182', '2014-06-23', '321 Building Boulevard, Queens, NY 54321', 1, 'Citibank', 75, 50, 'Citibank')
        """        
    
    return table_name
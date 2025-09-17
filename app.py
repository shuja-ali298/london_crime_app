import sqlite3
import pandas as pd
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Initialize the database and load the CSV data
def initialize_database():
    # Reset and recreate schema
    reset_database()
    recreate_schema()
    # Load data from CSV
    load_csv_data()

def load_csv_data():
    # Load CSV data into Pandas DataFrame
    df = pd.read_csv('data/crime_data.csv')

    # Connect to SQLite database (create if not exists)
    conn = sqlite3.connect('crime.db')
    cursor = conn.cursor()

    # Insert data into crime_data table
    for index, row in df.iterrows():
        cursor.execute('''
            INSERT INTO crime_data (MajorText, MinorText, BoroughName,
                                    Jul_2022, Aug_2022, Sep_2022, Oct_2022, Nov_2022, Dec_2022,
                                    Jan_2023, Feb_2023, Mar_2023, Apr_2023, May_2023, Jun_2023,
                                    Jul_2023, Aug_2023, Sep_2023, Oct_2023, Nov_2023, Dec_2023,
                                    Jan_2024, Feb_2024, Mar_2024, Apr_2024, May_2024, Jun_2024)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (row['MajorText'], row['MinorText'], row['BoroughName'],
              row['Jul_2022'], row['Aug_2022'], row['Sep_2022'], row['Oct_2022'], row['Nov_2022'], row['Dec_2022'],
              row['Jan_2023'], row['Feb_2023'], row['Mar_2023'], row['Apr_2023'], row['May_2023'], row['Jun_2023'],
              row['Jul_2023'], row['Aug_2023'], row['Sep_2023'], row['Oct_2023'], row['Nov_2023'], row['Dec_2023'],
              row['Jan_2024'], row['Feb_2024'], row['Mar_2024'], row['Apr_2024'], row['May_2024'], row['Jun_2024']))

    # Commit changes and close connection
    conn.commit()
    conn.close()

def reset_database():
    conn = sqlite3.connect('crime.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS crime_data')
    conn.commit()
    conn.close()

def recreate_schema():
    conn = sqlite3.connect('crime.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE crime_data (
            ID INTEGER PRIMARY KEY,
            MajorText TEXT,
            MinorText TEXT,
            BoroughName TEXT,
            Jul_2022 INTEGER,
            Aug_2022 INTEGER,
            Sep_2022 INTEGER,
            Oct_2022 INTEGER,
            Nov_2022 INTEGER,
            Dec_2022 INTEGER,
            Jan_2023 INTEGER,
            Feb_2023 INTEGER,
            Mar_2023 INTEGER,
            Apr_2023 INTEGER,
            May_2023 INTEGER,
            Jun_2023 INTEGER,
            Jul_2023 INTEGER,
            Aug_2023 INTEGER,
            Sep_2023 INTEGER,
            Oct_2023 INTEGER,
            Nov_2023 INTEGER,
            Dec_2023 INTEGER,
            Jan_2024 INTEGER,
            Feb_2024 INTEGER,
            Mar_2024 INTEGER,
            Apr_2024 INTEGER,
            May_2024 INTEGER,
            Jun_2024 INTEGER
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crime_type')
def crime_type():
    return render_template('crime_type.html')

@app.route('/total_crimes')
def total_crimes():
    return render_template('total_crimes.html')

@app.route('/crime_data_by_type')
def get_crime_data_by_type():
    conn = sqlite3.connect('crime.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT MajorText, Jul_2022, Aug_2022, Sep_2022, Oct_2022, Nov_2022, Dec_2022,
               Jan_2023, Feb_2023, Mar_2023, Apr_2023, May_2023, Jun_2023,
               Jul_2023, Aug_2023, Sep_2023, Oct_2023, Nov_2023, Dec_2023,
               Jan_2024, Feb_2024, Mar_2024, Apr_2024, May_2024, Jun_2024
        FROM crime_data
    ''')
    rows = cursor.fetchall()
    conn.close()

    crime_data = []
    for row in rows:
        crime_data.append({
            'MajorText': row[0],
            'Jul_2022': row[1],
            'Aug_2022': row[2],
            'Sep_2022': row[3],
            'Oct_2022': row[4],
            'Nov_2022': row[5],
            'Dec_2022': row[6],
            'Jan_2023': row[7],
            'Feb_2023': row[8],
            'Mar_2023': row[9],
            'Apr_2023': row[10],
            'May_2023': row[11],
            'Jun_2023': row[12],
            'Jul_2023': row[13],
            'Aug_2023': row[14],
            'Sep_2023': row[15],
            'Oct_2023': row[16],
            'Nov_2023': row[17],
            'Dec_2023': row[18],
            'Jan_2024': row[19],
            'Feb_2024': row[20],
            'Mar_2024': row[21],
            'Apr_2024': row[22],
            'May_2024': row[23],
            'Jun_2024': row[24]
        })

    return jsonify(crime_data)

@app.route('/total_crimes_data')
def get_total_crimes_data():
    conn = sqlite3.connect('crime.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT BoroughName, Jul_2022, Aug_2022, Sep_2022, Oct_2022, Nov_2022, Dec_2022,
               Jan_2023, Feb_2023, Mar_2023, Apr_2023, May_2023, Jun_2023,
               Jul_2023, Aug_2023, Sep_2023, Oct_2023, Nov_2023, Dec_2023,
               Jan_2024, Feb_2024, Mar_2024, Apr_2024, May_2024, Jun_2024
        FROM crime_data
    ''')
    rows = cursor.fetchall()
    conn.close()

    total_crimes_data = []
    for row in rows:
        total_crimes_data.append({
            'BoroughName': row[0],
            'Jul_2022': row[1],
            'Aug_2022': row[2],
            'Sep_2022': row[3],
            'Oct_2022': row[4],
            'Nov_2022': row[5],
            'Dec_2022': row[6],
            'Jan_2023': row[7],
            'Feb_2023': row[8],
            'Mar_2023': row[9],
            'Apr_2023': row[10],
            'May_2023': row[11],
            'Jun_2023': row[12],
            'Jul_2023': row[13],
            'Aug_2023': row[14],
            'Sep_2023': row[15],
            'Oct_2023': row[16],
            'Nov_2023': row[17],
            'Dec_2023': row[18],
            'Jan_2024': row[19],
            'Feb_2024': row[20],
            'Mar_2024': row[21],
            'Apr_2024': row[22],
            'May_2024': row[23],
            'Jun_2024': row[24]
        })

    return jsonify(total_crimes_data)

@app.route('/dataset_overview', methods=['GET'])
def dataset_overview():
    '''
    the function for pagination of the interactive dataset overview
    '''
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 50))

    # Get selected months from user input
    selected_months = request.args.getlist('months')
    filter_borough = request.args.get('borough')
    filter_crime_type = request.args.get('crime_type')

    # Default to showing data from May 2024 to June 2024 if no months are selected
    if not selected_months:
        selected_months = ['May_2024', 'Jun_2024']

    # Prepare the columns based on the selected months
    months = [
        'Jul_2022', 'Aug_2022', 'Sep_2022', 'Oct_2022', 'Nov_2022', 'Dec_2022',
        'Jan_2023', 'Feb_2023', 'Mar_2023', 'Apr_2023', 'May_2023', 'Jun_2023',
        'Jul_2023', 'Aug_2023', 'Sep_2023', 'Oct_2023', 'Nov_2023', 'Dec_2023',
        'Jan_2024', 'Feb_2024', 'Mar_2024', 'Apr_2024', 'May_2024', 'Jun_2024'
    ]

    # Validate selected months
    for month in selected_months:
        if month not in months:
            return f"Invalid month selected: {month}", 400

    # Prepare query for filtering data and selecting specific columns
    columns_to_select = ", ".join([month for month in months if month in selected_months])
    if not columns_to_select:
        columns_to_select = '*'

    query = f'''
        SELECT ID, MajorText, MinorText, BoroughName, {columns_to_select}
        FROM crime_data
        WHERE 1=1
    '''

    # Apply filters if specified
    params = []
    if filter_borough:
        query += ' AND BoroughName = ?'
        params.append(filter_borough)
    if filter_crime_type:
        query += ' AND MajorText = ?'
        params.append(filter_crime_type)

    # Count total items
    count_query = f'''
        SELECT COUNT(*)
        FROM crime_data
        WHERE 1=1
    '''
    count_params = []
    if filter_borough:
        count_query += ' AND BoroughName = ?'
        count_params.append(filter_borough)
    if filter_crime_type:
        count_query += ' AND MajorText = ?'
        count_params.append(filter_crime_type)

    conn = sqlite3.connect('crime.db')
    cursor = conn.cursor()
    cursor.execute(count_query, count_params)
    total_items = cursor.fetchone()[0]

    total_pages = (total_items + per_page - 1) // per_page

    # Paginate the results
    query += ' ORDER BY ROWID LIMIT ? OFFSET ?'
    params.extend([per_page, (page - 1) * per_page])
    cursor.execute(query, params)
    data = cursor.fetchall()

    # Get boroughs and crime types for filters
    cursor.execute('SELECT DISTINCT BoroughName FROM crime_data')
    boroughs = [row[0] for row in cursor.fetchall()]
    cursor.execute('SELECT DISTINCT MajorText FROM crime_data')
    crime_types = [row[0] for row in cursor.fetchall()]
    conn.close()

    # Generate pagination range
    def generate_page_range(current_page, total_pages):
        page_range = []
        if total_pages <= 5:
            page_range = list(range(1, total_pages + 1))
        else:
            if current_page <= 3:
                page_range = list(range(1, 6))
                if total_pages > 5:
                    page_range.append('...')
                    page_range.append(total_pages)
            elif current_page >= total_pages - 2:
                page_range = [1, '...'] + list(range(total_pages - 4, total_pages + 1))
            else:
                page_range = [1, '...'] + list(range(current_page - 1, current_page + 2)) + ['...'] + [total_pages]
        return page_range

    page_range = generate_page_range(page, total_pages)

    return render_template('dataset.html',
                           data=data,
                           page=page,
                           per_page=per_page,
                           total_items=total_items,
                           total_pages=total_pages,
                           boroughs=boroughs,
                           crime_types=crime_types,
                           selected_months=selected_months,
                           months=months,
                           page_range=page_range)


if __name__ == '__main__':
    initialize_database()
    app.run(debug=True)

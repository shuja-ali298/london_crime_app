# London Crime Data Dashboard

#### Video Demo: https://youtu.be/AC0csVJMSwI

#### Description:
Welcome to the London Crime Data Dashboard! This project is a web-based application designed to provide insights and analysis of crime data in London. Using this dashboard, users can:

- **View Crime Data by Type:** Explore detailed statistics about different crime types throughout various months. Users can interact with the plot, by selecting and de-selecting the types of crimes they want to see trends for.
- **Total Crimes Overview:** Get an overview of total crimes categorized by borough and year. Users can interact with the plot, by selecting and de-selecting the boroughs they want to see the trends for.
- **Dataset Overview:** Access and interact with a comprehensive dataset, including filtering and pagination options.

The **London Crime Data Dashboard** was created to address the need for an intuitive and user-friendly tool to visualize and analyze crime data. With the increasing availability of public crime datasets, there is a growing demand for applications that can effectively manage and present this data in a meaningful way. By offering a web-based interface for accessing and exploring crime statistics, this project aims to contribute to community awareness, support law enforcement efforts, and foster research into crime trends and prevention strategies.

The dashboard leverages modern web technologies and data processing techniques to provide a seamless user experience, making it easier for individuals and organizations to gain insights from crime data and make informed decisions based on the analysis.

## Features:
- **Interactive Data Filtering:** Filter data by borough and crime type.
- **Month-based Selection:** Choose specific months to display in the dataset view.
- **Pagination:** Navigate through large datasets with ease using pagination controls.
- **Default Views:** View default data for May 2024 to June 2024.

## Technologies Used:
- **Flask:** A lightweight web framework for Python, used to create the web application.
- **SQLite:** A lightweight database used to store crime data.
- **Pandas:** A data analysis library for Python, used to process and load data into the SQLite database.
- **Bootstrap:** A CSS framework for creating responsive and visually appealing web designs.

## Instructions

### **1. Install Dependencies**

Ensure you have the necessary dependencies installed. You can use the following `bash` commands to install required packages:

```bash
sudo apt update
sudo apt install python3 python3-pip sqlite3
pip3 install pandas flask
```
### **2. Run the Application**

Start the flask server with:
```bash
flask run
```

Or:
```bash
python3 app.py
```
The application will automatically set up and populate the SQLite database if it doesn't already exist.

### **3. Troubleshooting**
If you encounter issues, try the following:

Reset the Database:
```bash
python3 reset_database.py
```

Reinstall dependencies:
```bash
pip3 uninstall pandas flask
pip3 install pandas flask
```

## Acknowledgments:
This project benefited from the use of ChatGPT, which assisted in streamlining certain processes, such as efficiently handling month-based data insertion. The assistance provided helped to expedite development and ensure best practices were followed. It is important to note that all critical decisions and implementations were carried out personally to maintain the integrity and originality of the project.

Some code and ideas were inspired from CS50 scripts and work at my university.

Data was used from the London Metropolitan Police

## License:
MIT License

Copyright (c) [2024] [Subhan Shujah Ali]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
---
For more information about the MIT License, visit [Open Source Initiative MIT License](https://opensource.org/licenses/MIT).

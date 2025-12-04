✅ Step-by-Step to Run the Project Using Python Virtual Environment

🔹 1. Create a Virtual Environment
If not already created, set up a virtual environment using Python 3.8:

bash
Copy
Edit
py -3.8 -m venv venv

🔹 2. Activate the Virtual Environment
Activate the virtual environment (you’ll see (venv) in the terminal once it's active):

bash
Copy
Edit
venv\Scripts\activate
pip install -r requirements.txt

🔹 3. Run the Flask Application
Start the Flask development server:

bash
Copy
Edit
python app.py
You should see output like:

csharp
Copy
Edit
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
   
🔹 4. Open the Web App in Your Browser
Visit this URL in your browser:

Copy
Edit
http://localhost:5000/
The Healthcare AI web application should load successfully.

https://www.kaggle.com/datasets/mathchi/diabetes-data-set

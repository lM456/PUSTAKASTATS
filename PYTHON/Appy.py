from flask import Flask, render_template, request, jsonify
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

app = Flask(__name__)

def load_pengunjung_data():
    data = [
        {"Bulan": "Januari", "Fakultas": "FISIP", "Jumlah": 419},
        {"Bulan": "Januari", "Fakultas": "FKIP", "Jumlah": 840},
        {"Bulan": "Januari", "Fakultas": "FEBM", "Jumlah": 298},
        {"Bulan": "Januari", "Fakultas": "FIKP", "Jumlah": 94},
        {"Bulan": "Januari", "Fakultas": "FTTK", "Jumlah": 147},
        {"Bulan": "Februari", "Fakultas": "FISIP", "Jumlah": 423},
        {"Bulan": "Februari", "Fakultas": "FKIP", "Jumlah": 917},
        {"Bulan": "Februari", "Fakultas": "FEBM", "Jumlah": 628},
        {"Bulan": "Februari", "Fakultas": "FIKP", "Jumlah": 222},
        {"Bulan": "Februari", "Fakultas": "FTTK", "Jumlah": 109},
        {"Bulan": "Maret", "Fakultas": "FISIP", "Jumlah": 899},
        {"Bulan": "Maret", "Fakultas": "FKIP", "Jumlah": 1821},
        {"Bulan": "Maret", "Fakultas": "FEBM", "Jumlah": 2173},
        {"Bulan": "Maret", "Fakultas": "FIKP", "Jumlah": 1176},
        {"Bulan": "Maret", "Fakultas": "FTTK", "Jumlah": 312},
        {"Bulan": "April", "Fakultas": "FISIP", "Jumlah": 454},
        {"Bulan": "April", "Fakultas": "FKIP", "Jumlah": 877},
        {"Bulan": "April", "Fakultas": "FEBM", "Jumlah": 1477},
        {"Bulan": "April", "Fakultas": "FIKP", "Jumlah": 717},
        {"Bulan": "April", "Fakultas": "FTTK", "Jumlah": 128},
        {"Bulan": "Mei", "Fakultas": "FISIP", "Jumlah": 1131},
        {"Bulan": "Mei", "Fakultas": "FKIP", "Jumlah": 1396},
        {"Bulan": "Mei", "Fakultas": "FEBM", "Jumlah": 1599},
        {"Bulan": "Mei", "Fakultas": "FIKP", "Jumlah": 855},
        {"Bulan": "Mei", "Fakultas": "FTTK", "Jumlah": 79},
        {"Bulan": "Juni", "Fakultas": "FISIP", "Jumlah": 1022},
        {"Bulan": "Juni", "Fakultas": "FKIP", "Jumlah": 1152},
        {"Bulan": "Juni", "Fakultas": "FEBM", "Jumlah": 1941},
        {"Bulan": "Juni", "Fakultas": "FIKP", "Jumlah": 826},
        {"Bulan": "Juni", "Fakultas": "FTTK", "Jumlah": 129},
    ]
    return pd.DataFrame(data)
def load_peminjaman_data():
    data = [
        {"Bulan": "Januari", "Fakultas": "FISIP", "Jumlah": 14},
        {"Bulan": "Januari", "Fakultas": "FKIP", "Jumlah": 99},
        {"Bulan": "Januari", "Fakultas": "FEBM", "Jumlah": 9},
        {"Bulan": "Januari", "Fakultas": "FIKP", "Jumlah": 2},
        {"Bulan": "Januari", "Fakultas": "FTTK", "Jumlah": 0},
        {"Bulan": "Februari", "Fakultas": "FISIP", "Jumlah": 62},
        {"Bulan": "Februari", "Fakultas": "FKIP", "Jumlah": 135},
        {"Bulan": "Februari", "Fakultas": "FEBM", "Jumlah": 47},
        {"Bulan": "Februari", "Fakultas": "FIKP", "Jumlah": 1},
        {"Bulan": "Februari", "Fakultas": "FTTK", "Jumlah": 1},
        {"Bulan": "Maret", "Fakultas": "FISIP", "Jumlah": 972},
        {"Bulan": "Maret", "Fakultas": "FKIP", "Jumlah": 399},
        {"Bulan": "Maret", "Fakultas": "FEBM", "Jumlah": 757},
        {"Bulan": "Maret", "Fakultas": "FIKP", "Jumlah": 5},
        {"Bulan": "Maret", "Fakultas": "FTTK", "Jumlah": 3},
        {"Bulan": "April", "Fakultas": "FISIP", "Jumlah": 64},
        {"Bulan": "April", "Fakultas": "FKIP", "Jumlah": 84},
        {"Bulan": "April", "Fakultas": "FEBM", "Jumlah": 367},
        {"Bulan": "April", "Fakultas": "FIKP", "Jumlah": 4},
        {"Bulan": "April", "Fakultas": "FTTK", "Jumlah": 0},
        {"Bulan": "Mei", "Fakultas": "FISIP", "Jumlah": 137},
        {"Bulan": "Mei", "Fakultas": "FKIP", "Jumlah": 242},
        {"Bulan": "Mei", "Fakultas": "FEBM", "Jumlah": 409},
        {"Bulan": "Mei", "Fakultas": "FIKP", "Jumlah": 3},
        {"Bulan": "Mei", "Fakultas": "FTTK", "Jumlah": 2},
        {"Bulan": "Juni", "Fakultas": "FISIP", "Jumlah": 73},
        {"Bulan": "Juni", "Fakultas": "FKIP", "Jumlah": 115},
        {"Bulan": "Juni", "Fakultas": "FEBM", "Jumlah": 292},
        {"Bulan": "Juni", "Fakultas": "FIKP", "Jumlah": 2},
        {"Bulan": "Juni", "Fakultas": "FTTK", "Jumlah": 5},
    ]
    return pd.DataFrame(data)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    # Get request data
    analysis_type = request.json.get('type')  # pengunjung or peminjaman

    # Load data based on type
    if analysis_type == 'pengunjung':
        data = load_pengunjung_data()
    elif analysis_type == 'peminjaman':
        data = load_peminjaman_data()
    else:
        return jsonify({"error": "Invalid analysis type"}), 400

    # Transform data for Apriori
    grouped = data.pivot_table(index="Bulan", columns="Fakultas", values="Jumlah", aggfunc="sum", fill_value=0)
    binary_data = (grouped > 0).astype(int)  # Convert to binary for Apriori

    # Perform Apriori analysis
    frequent_itemsets = apriori(binary_data, min_support=0.2, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

    # Prepare data for frontend
    result = {
        "frequent_itemsets": frequent_itemsets.to_dict(orient="records"),
        "rules": rules.to_dict(orient="records"),
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
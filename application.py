from flask import Flask, render_template, request

application = Flask(__name__)

def calculate_property_tax(build_up_area):
    if build_up_area < 1000:
        return 1000
    elif 1000 <= build_up_area < 5000:
        return 3500
    else:
        return 5000

def calculate_water_tax(months):
    # Considering a fixed water tax of Rs 100 per month
    return 100 * months

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/calculate', methods=['POST'])
def calculate():
    build_up_area = float(request.form['build_up_area'])
    months = int(request.form['months'])  # Get number of months
    property_tax = calculate_property_tax(build_up_area)
    water_tax = calculate_water_tax(months)  # Calculate water tax based on months
    total_tax = property_tax + water_tax  # Calculate total tax
    return render_template('result.html', build_up_area=build_up_area, property_tax=property_tax, water_tax=water_tax, total_tax=total_tax)

if __name__ == '__main__':
    application.run(debug=True, host='127.0.0.1', port=5000)

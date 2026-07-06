from flask import Blueprint
from flask import jsonify

import pandas as pd

internship_bp = Blueprint(
    'internship',
    __name__
)

@internship_bp.route('/internships', methods=['GET'])
def get_internships():

    internships_df = pd.read_csv(
        'datasets/internships.csv'
    )

    internships = internships_df.to_dict(
        orient='records'
    )

    return jsonify(internships)
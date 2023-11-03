from flask import Blueprint, request, jsonify
import os
import cv2
from skimage.feature import hog
import pickle
import pymysql

#path adjusting
def get_path(path):
    change_path = path.replace("\\",'/')
    return change_path

bp = Blueprint('eye', __name__, url_prefix='/')

# eye.pkl의 상대 경로 계산
path = '../eye/SVM-Classifier/eye_model.pkl' 
classify_path = '/app/eye/SVM-Classifier/eye_model.pkl'
#get_path(os.path.abspath(path))

# SVM 모델 로드
with open(classify_path, 'rb') as model_file:
    svm_model = pickle.load(model_file)

categories = ['cataracts', 'cherry_eye', 'normal']


label_to_int = {category: i for i, category in enumerate(categories)}

@bp.route('/eye', methods=['POST'])
def analyze_eye():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part', 'message': 'fail'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file', 'message': 'fail'})

    if file:
        # Create the 'uploads' directory if it doesn't exist
        if not os.path.exists('uploads'):
            os.makedirs('uploads')

        # Save the uploaded image to a temporary location
        image_path = os.path.join('uploads', file.filename)
        file.save(image_path)

        # Load and preprocess the image
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        preprocessed_image = cv2.resize(image, (64, 64))
        hog_features = hog(preprocessed_image, orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1))

        # Predict the eye category using SVM model
        predicted_label = svm_model.predict([hog_features])[0]
        predicted_label = label_to_int[predicted_label]
        predicted_category = categories[predicted_label]

        # Remove the temporary image file
        os.remove(image_path)
        return jsonify({'result': predicted_category, 'message': 'success'})

def db_connector():
    connector = pymysql.connect(host='petconnect.cfqtdjr2iyqh.ap-northeast-2.rds.amazonaws.com',
                                  user='admin',
                                  password='Qwer12345678!',
                                  db='petconnect',
                                  charset='utf8')
    return connector